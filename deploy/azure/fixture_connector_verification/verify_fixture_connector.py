#!/usr/bin/env python3
"""Deterministic APIM-only verification for the fixture ChatGPT MCP connector."""

from __future__ import annotations

import argparse
import json
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_BACKOFF_SECONDS = (2.0, 5.0, 15.0)


@dataclass
class HttpResult:
    status: int | None
    headers: dict[str, str]
    body: str
    error: str | None = None


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def http_request(
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    payload: Any | None = None,
    timeout: float = 30.0,
) -> HttpResult:
    data = None
    request_headers = dict(headers or {})
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        request_headers.setdefault("Content-Type", "application/json")

    request = urllib.request.Request(url, data=data, headers=request_headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            return HttpResult(
                status=response.status,
                headers={k.lower(): v for k, v in response.headers.items()},
                body=body,
            )
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return HttpResult(
            status=exc.code,
            headers={k.lower(): v for k, v in exc.headers.items()},
            body=body,
            error=f"HTTPError: {exc.code}",
        )
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        return HttpResult(status=None, headers={}, body="", error=f"{type(exc).__name__}: {exc}")


def request_with_retries(
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    payload: Any | None = None,
    retry_statuses: set[int] | None = None,
) -> tuple[HttpResult, int]:
    retry_statuses = retry_statuses or {500, 502, 503, 504}
    attempts = 0
    for index, delay in enumerate((0.0, *DEFAULT_BACKOFF_SECONDS)):
        if delay:
            time.sleep(delay)
        attempts = index + 1
        result = http_request(method, url, headers=headers, payload=payload)
        if result.status is None:
            continue
        if result.status in retry_statuses:
            continue
        return result, attempts
    return result, attempts


def parse_sse_json(body: str) -> dict[str, Any]:
    events: list[dict[str, Any]] = []
    for block in body.split("\n\n"):
        data_lines: list[str] = []
        for line in block.splitlines():
            if line.startswith("data:"):
                data_lines.append(line[len("data:") :].strip())
        if not data_lines:
            continue
        try:
            events.append(json.loads("\n".join(data_lines)))
        except json.JSONDecodeError:
            continue
    if not events:
        raise ValueError("SSE response did not contain a JSON data event")
    return events[-1]


def parse_mcp_body(result: HttpResult) -> dict[str, Any]:
    content_type = result.headers.get("content-type", "")
    if "text/event-stream" in content_type:
        return parse_sse_json(result.body)
    return json.loads(result.body)


def mcp_post(
    url: str,
    payload: dict[str, Any],
    *,
    session_id: str | None = None,
) -> tuple[HttpResult, dict[str, Any], int]:
    headers = {
        "Accept": "application/json, text/event-stream",
        "Content-Type": "application/json",
    }
    if session_id:
        headers["Mcp-Session-Id"] = session_id
    result, attempts = request_with_retries("POST", url, headers=headers, payload=payload)
    parsed = parse_mcp_body(result) if result.body else {}
    return result, parsed, attempts


def content_fallback_matches(tool_result: dict[str, Any]) -> bool:
    result = tool_result.get("result", {})
    structured = result.get("structuredContent")
    if structured is None:
        structured = result.get("structured_content")
    content = result.get("content", [])
    text_values = [item.get("text") for item in content if isinstance(item, dict) and item.get("type") == "text"]
    if structured is None or not text_values:
        return False
    try:
        return json.loads(text_values[0]) == structured
    except json.JSONDecodeError:
        return False


def structured_content(tool_result: dict[str, Any]) -> dict[str, Any]:
    result = tool_result.get("result", {})
    structured = result.get("structuredContent")
    if structured is None:
        structured = result.get("structured_content")
    return structured if isinstance(structured, dict) else {}


def forbidden_hits(value: Any, forbidden: list[str]) -> list[str]:
    if isinstance(value, str):
        blob = value
    else:
        blob = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return sorted({marker for marker in forbidden if marker and marker in blob})


def url_host(url: str) -> str:
    return urllib.parse.urlparse(url).hostname or ""


def validate_apim_urls(config: dict[str, Any]) -> tuple[bool, str]:
    allowed_host = config.get("allowed_apim_host") or url_host(config["apim_url"])
    urls = {
        "apim_url": config["apim_url"],
        "healthz_url": config["healthz_url"],
        "readyz_url": config["readyz_url"],
    }
    observed = {name: url_host(url) for name, url in urls.items()}
    bad = {name: host for name, host in observed.items() if host != allowed_host}
    if bad:
        return False, f"expected all URLs on {allowed_host}; observed {observed}"
    return True, f"all configured URLs use {allowed_host}"


def append_check(
    report: dict[str, Any],
    *,
    check_id: str,
    status: str,
    expected: str,
    observed: str,
    http_status: int | None = None,
    attempts: int | None = None,
    artifact_ref: str | None = None,
) -> None:
    check: dict[str, Any] = {
        "id": check_id,
        "status": status,
        "http_status": http_status,
        "expected": expected,
        "observed": observed,
    }
    if attempts is not None:
        check["attempts"] = attempts
    if artifact_ref is not None:
        check["artifact_ref"] = artifact_ref
    report["checks"].append(check)
    if status == "fail":
        report["overall"] = "fail"


def scan_payload(report: dict[str, Any], label: str, payload: Any, forbidden: list[str]) -> None:
    hits = forbidden_hits(payload, forbidden)
    if hits:
        report["secret_scan"]["status"] = "fail"
        report["secret_scan"]["hits"].extend(f"{label}:{hit}" for hit in hits)
        report["overall"] = "fail"


def run_preflight(config: dict[str, Any], output_dir: Path, manual_transcript: Path | None) -> dict[str, Any]:
    forbidden = config["forbidden_strings"]
    expected_tools = sorted(config["tool_allowlist"])
    fetch_max_chars = int(config.get("fetch_max_chars", 12000))
    report: dict[str, Any] = {
        "run_id": config["run_id"],
        "created_at": now_iso(),
        "scope": "fixture_only",
        "endpoint_under_test": "apim_only",
        "overall": "pass",
        "checks": [],
        "session_id_present": False,
        "tool_names_observed": [],
        "search_result_count": 0,
        "fetch_text_length": None,
        "fetch_max_chars": fetch_max_chars,
        "search_result_id": None,
        "secret_scan": {"status": "pass", "hits": []},
        "manual_chatgpt": {"status": "blocked", "reason": "manual transcript not provided"},
        "decision": "blocked_pending_operator",
        "private_real_index_status": "blocked_not_tested",
    }

    apim_urls_ok, apim_urls_observed = validate_apim_urls(config)
    append_check(
        report,
        check_id="apim_url_host_policy",
        status="pass" if apim_urls_ok else "fail",
        http_status=None,
        expected=f"all URLs use {config.get('allowed_apim_host') or url_host(config['apim_url'])}",
        observed=apim_urls_observed,
    )
    if report["overall"] == "fail":
        return finalize_report(report, manual_transcript, forbidden)

    for check_id, url in (("healthz", config["healthz_url"]), ("readyz", config["readyz_url"])):
        result, attempts = request_with_retries("GET", url, headers={"Accept": "application/json"})
        status = "pass" if result.status == 200 else "fail"
        observed = result.body[:1000] if result.body else (result.error or "")
        append_check(
            report,
            check_id=check_id,
            status=status,
            http_status=result.status,
            attempts=attempts,
            expected="200 OK and no private content",
            observed=observed,
        )
        scan_payload(report, check_id, result.body, forbidden)

    if report["overall"] == "fail":
        return finalize_report(report, manual_transcript, forbidden)

    initialize = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "fixture-verifier", "version": "1.0.0"},
        },
    }
    try:
        response, parsed, attempts = mcp_post(config["apim_url"], initialize)
        session_id = response.headers.get("mcp-session-id")
        report["session_id_present"] = bool(session_id)
        ok = response.status == 200 and "result" in parsed
        append_check(
            report,
            check_id="mcp_initialize",
            status="pass" if ok else "fail",
            http_status=response.status,
            attempts=attempts,
            expected="200 with initialize result",
            observed=json.dumps(parsed, ensure_ascii=False)[:1200],
        )
        scan_payload(report, "mcp_initialize", parsed, forbidden)
    except Exception as exc:
        session_id = None
        append_check(
            report,
            check_id="mcp_initialize",
            status="fail",
            http_status=None,
            expected="200 with initialize result",
            observed=f"{type(exc).__name__}: {exc}",
        )

    if report["overall"] == "fail":
        return finalize_report(report, manual_transcript, forbidden)

    initialized_headers = {
        "Accept": "application/json, text/event-stream",
        "Content-Type": "application/json",
    }
    if session_id:
        initialized_headers["Mcp-Session-Id"] = session_id
    initialized_payload = {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}
    initialized_response, initialized_attempts = request_with_retries(
        "POST",
        config["apim_url"],
        headers=initialized_headers,
        payload=initialized_payload,
    )
    initialized_ok = initialized_response.status in {200, 202, 204}
    append_check(
        report,
        check_id="notifications_initialized",
        status="pass" if initialized_ok else "fail",
        http_status=initialized_response.status,
        attempts=initialized_attempts,
        expected="200, 202, or 204",
        observed=initialized_response.body[:1000] if initialized_response.body else (initialized_response.error or ""),
    )
    scan_payload(report, "notifications_initialized", initialized_response.body, forbidden)

    if report["overall"] == "fail":
        return finalize_report(report, manual_transcript, forbidden)

    try:
        response, parsed, attempts = mcp_post(
            config["apim_url"],
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
            session_id=session_id,
        )
        tools = parsed.get("result", {}).get("tools", [])
        tool_names = [tool.get("name") for tool in tools if isinstance(tool, dict)]
        report["tool_names_observed"] = tool_names
        has_denied_prefix = any(
            name.startswith(prefix)
            for name in tool_names
            for prefix in config.get("tool_deny_prefixes", [])
            if isinstance(name, str)
        )
        ok = sorted(tool_names) == expected_tools and not has_denied_prefix
        append_check(
            report,
            check_id="tools_list_exact",
            status="pass" if ok else "fail",
            http_status=response.status,
            attempts=attempts,
            expected=str(config["tool_allowlist"]),
            observed=str(tool_names),
        )
        scan_payload(report, "tools_list", parsed, forbidden)
    except Exception as exc:
        append_check(
            report,
            check_id="tools_list_exact",
            status="fail",
            http_status=None,
            expected=str(config["tool_allowlist"]),
            observed=f"{type(exc).__name__}: {exc}",
        )

    if report["overall"] == "fail":
        return finalize_report(report, manual_transcript, forbidden)

    query = config["fixture_queries"][0]
    try:
        response, parsed, attempts = mcp_post(
            config["apim_url"],
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {"name": "search", "arguments": {"query": query}},
            },
            session_id=session_id,
        )
        structured = structured_content(parsed)
        results = structured.get("results", [])
        report["search_result_count"] = len(results) if isinstance(results, list) else 0
        first_result = results[0] if isinstance(results, list) and results else {}
        report["search_result_id"] = first_result.get("id") if isinstance(first_result, dict) else None
        no_raw_text = not any(isinstance(item, dict) and "text" in item for item in results)
        result_fields_ok = all(
            isinstance(item, dict) and all(key in item for key in ("id", "title", "url"))
            for item in results
        )
        ok = bool(results) and no_raw_text and result_fields_ok and content_fallback_matches(parsed)
        append_check(
            report,
            check_id="search_fixture_query",
            status="pass" if ok else "fail",
            http_status=response.status,
            attempts=attempts,
            expected="at least one result with id/title/url, no raw text, matching JSON fallback",
            observed=json.dumps(structured, ensure_ascii=False)[:1200],
        )
        scan_payload(report, "search", parsed, forbidden)
    except Exception as exc:
        append_check(
            report,
            check_id="search_fixture_query",
            status="fail",
            http_status=None,
            expected="at least one result with id/title/url",
            observed=f"{type(exc).__name__}: {exc}",
        )

    if report["overall"] == "fail" or not report.get("search_result_id"):
        return finalize_report(report, manual_transcript, forbidden)

    try:
        response, parsed, attempts = mcp_post(
            config["apim_url"],
            {
                "jsonrpc": "2.0",
                "id": 4,
                "method": "tools/call",
                "params": {"name": "fetch", "arguments": {"id": report["search_result_id"]}},
            },
            session_id=session_id,
        )
        structured = structured_content(parsed)
        text = structured.get("text")
        report["fetch_text_length"] = len(text) if isinstance(text, str) else None
        text_length = len(text) if isinstance(text, str) else None
        ok = (
            all(key in structured for key in ("id", "title", "text", "url", "metadata"))
            and isinstance(text, str)
            and bool(text)
            and text_length <= fetch_max_chars
            and content_fallback_matches(parsed)
        )
        append_check(
            report,
            check_id="fetch_fixture_result",
            status="pass" if ok else "fail",
            http_status=response.status,
            attempts=attempts,
            expected=f"id/title/text/url/metadata present, text <= {fetch_max_chars} chars, matching JSON fallback",
            observed=json.dumps(
                {
                    "id": structured.get("id"),
                    "title": structured.get("title"),
                    "url": structured.get("url"),
                    "metadata": structured.get("metadata"),
                    "text_length": report["fetch_text_length"],
                },
                ensure_ascii=False,
            )[:1200],
        )
        scan_payload(report, "fetch", parsed, forbidden)
    except Exception as exc:
        append_check(
            report,
            check_id="fetch_fixture_result",
            status="fail",
            http_status=None,
            expected="id/title/text/url/metadata present",
            observed=f"{type(exc).__name__}: {exc}",
        )

    return finalize_report(report, manual_transcript, forbidden)


def finalize_report(report: dict[str, Any], manual_transcript: Path | None, forbidden: list[str]) -> dict[str, Any]:
    report["secret_scan"]["hits"] = sorted(set(report["secret_scan"]["hits"]))
    if manual_transcript:
        try:
            transcript = load_json(manual_transcript)
            hits = forbidden_hits(transcript, forbidden)
            observed_tools = transcript.get("tool_list_observed")
            transcript_ok = (
                transcript.get("created_app") is True
                and transcript.get("auth_mode") == "No Authentication"
                and sorted(observed_tools or []) == ["fetch", "search"]
                and not hits
            )
            report["manual_chatgpt"] = {
                "status": "pass" if transcript_ok else "fail",
                "path": "<manual-transcript>",
                "tool_list_observed": observed_tools,
                "forbidden_hits": hits,
            }
            if not transcript_ok:
                report["overall"] = "fail"
        except Exception as exc:
            report["manual_chatgpt"] = {
                "status": "fail",
                "path": "<manual-transcript>",
                "reason": f"{type(exc).__name__}: {exc}",
            }
            report["overall"] = "fail"

    if report["overall"] == "fail":
        report["decision"] = "no_go"
    elif report["manual_chatgpt"]["status"] == "pass":
        report["decision"] = "go_fixture_only"
    else:
        report["decision"] = "blocked_pending_operator"

    return report


def make_summary(config: dict[str, Any], report: dict[str, Any]) -> dict[str, Any]:
    return {
        "run_id": config["run_id"],
        "created_at": now_iso(),
        "decision": report["decision"],
        "scope": "fixture_only_apim_only",
        "preflight_overall": report["overall"],
        "manual_chatgpt_status": report["manual_chatgpt"]["status"],
        "tool_names_observed": report["tool_names_observed"],
        "search_result_count": report["search_result_count"],
        "fetch_text_length": report["fetch_text_length"],
        "fetch_max_chars": report["fetch_max_chars"],
        "secret_scan_status": report["secret_scan"]["status"],
        "secret_scan_hits": report["secret_scan"]["hits"],
        "private_real_index_status": report["private_real_index_status"],
        "next_step": (
            "Create a sanitized ChatGPT Developer Mode transcript using the APIM /mcp URL."
            if report["decision"] == "blocked_pending_operator"
            else "Investigate failed checks before any connector sign-off."
            if report["decision"] == "no_go"
            else "Fixture-only ChatGPT connector verification can be recorded as complete."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to verification_input.json.")
    parser.add_argument(
        "--output-dir",
        default=".tmp-fixture-verification-artifacts",
        help="Directory for sanitized verification artifacts.",
    )
    parser.add_argument(
        "--manual-transcript",
        default=None,
        help="Optional sanitized manual ChatGPT transcript JSON.",
    )
    args = parser.parse_args()

    config = load_json(Path(args.input))
    output_dir = Path(args.output_dir)
    manual_transcript = Path(args.manual_transcript) if args.manual_transcript else None

    report = run_preflight(config, output_dir, manual_transcript)
    summary = make_summary(config, report)

    save_json(output_dir / "preflight_report.json", report)
    save_json(output_dir / "verification_summary.json", summary)

    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["decision"] in {"go_fixture_only", "blocked_pending_operator"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
