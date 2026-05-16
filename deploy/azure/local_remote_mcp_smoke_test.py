"""Local no-secrets smoke test for the Azure remote MCP preparation path."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import shutil
import subprocess
from pathlib import Path

from fastmcp import Client

from math_rag.mcp_http_server import (
    CHATGPT_TOOL_NAMES,
    INTERNAL_TOOL_NAMES,
    HttpMcpConfig,
    create_mcp_server,
)


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FIXTURE_CORPUS = WORKSPACE_ROOT / "deploy" / "azure" / "test_corpus"
DEFAULT_TEST_INDEX = WORKSPACE_ROOT / ".tmp-azure-test-index"
DEFAULT_API_KEY = "test-secret"


def _run(cmd: list[str], *, env: dict[str, str] | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=WORKSPACE_ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=check,
    )


def _python() -> str:
    return str(WORKSPACE_ROOT / "math_rag" / ".venv" / "bin" / "python")


def build_test_index(corpus_path: Path, index_dir: Path) -> None:
    if index_dir.exists():
        shutil.rmtree(index_dir)
    _run(
        [
            _python(),
            "-m",
            "math_rag.cli",
            "ingest",
            str(corpus_path),
            "--index-dir",
            str(index_dir),
        ]
    )


def verify_index_sources(index_dir: Path, expected_suffix: str) -> list[str]:
    index_path = index_dir / "index.json"
    payload = json.loads(index_path.read_text())
    sources = sorted({chunk["source_path"] for chunk in payload.get("chunks", [])})
    if not sources:
        raise RuntimeError("test index contains no sources")
    if any(expected_suffix not in source.replace("\\", "/") for source in sources):
        raise RuntimeError(f"unexpected source paths in test index: {sources}")
    return sources


def safe_source_ids(sources: list[str]) -> list[str]:
    return sorted(source.replace("\\", "/").split("deploy/azure/test_corpus/", 1)[-1] for source in sources)


def safe_stats_text(stats_text: str, index_dir: Path) -> str:
    return stats_text.replace(str(index_dir), "<fixture-index>")


def verify_failure_modes(index_dir: Path) -> None:
    public_no_auth = _run(
        [_python(), "-m", "math_rag.mcp_http_server"],
        env={
            **os.environ,
            "MATH_RAG_INDEX_DIR": str(index_dir),
            "MATH_RAG_HOST": "0.0.0.0",
            "MATH_RAG_AUTH_MODE": "none",
            "MATH_RAG_API_TOKEN": "",
            "MATH_RAG_API_KEY": "",
            "MATH_RAG_MCP_ALLOW_WRITE_TOOLS": "false",
            "MATH_RAG_REMOTE_MCP_READ_ONLY": "true",
            "MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC": "false",
        },
        check=False,
    )
    if public_no_auth.returncode == 0 or "Refusing unauthenticated public" not in public_no_auth.stderr:
        raise RuntimeError("public-no-auth failure check did not behave as expected")

    missing_bearer_token = _run(
        [_python(), "-m", "math_rag.mcp_http_server"],
        env={
            **os.environ,
            "MATH_RAG_INDEX_DIR": str(index_dir),
            "MATH_RAG_AUTH_MODE": "bearer",
            "MATH_RAG_API_TOKEN": "",
            "MATH_RAG_API_KEY": "",
            "MATH_RAG_MCP_ALLOW_WRITE_TOOLS": "false",
            "MATH_RAG_REMOTE_MCP_READ_ONLY": "true",
        },
        check=False,
    )
    if missing_bearer_token.returncode == 0 or "MATH_RAG_API_TOKEN" not in missing_bearer_token.stderr:
        raise RuntimeError("missing-bearer-token failure check did not behave as expected")

    read_only_false = _run(
        [_python(), "-m", "math_rag.mcp_http_server"],
        env={
            **os.environ,
            "MATH_RAG_INDEX_DIR": str(index_dir),
            "MATH_RAG_AUTH_MODE": "bearer",
            "MATH_RAG_API_TOKEN": DEFAULT_API_KEY,
            "MATH_RAG_MCP_ALLOW_WRITE_TOOLS": "false",
            "MATH_RAG_REMOTE_MCP_READ_ONLY": "false",
        },
        check=False,
    )
    if read_only_false.returncode == 0 or "read-only only" not in read_only_false.stderr:
        raise RuntimeError("read-only-false failure check did not behave as expected")

    write_enabled = _run(
        [_python(), "-m", "math_rag.mcp_http_server"],
        env={
            **os.environ,
            "MATH_RAG_INDEX_DIR": str(index_dir),
            "MATH_RAG_AUTH_MODE": "bearer",
            "MATH_RAG_API_TOKEN": DEFAULT_API_KEY,
            "MATH_RAG_REMOTE_MCP_READ_ONLY": "true",
            "MATH_RAG_MCP_ALLOW_WRITE_TOOLS": "true",
        },
        check=False,
    )
    if write_enabled.returncode == 0 or "refuses to start" not in write_enabled.stderr:
        raise RuntimeError("write-enabled remote failure check did not behave as expected")


async def verify_inprocess_mcp(index_dir: Path) -> dict[str, object]:
    chatgpt_config = HttpMcpConfig(
        index_dir=str(index_dir),
        host="127.0.0.1",
        port=8000,
        transport="streamable-http",
        path="/mcp",
        public_base_url="http://127.0.0.1:8000",
        tool_mode="chatgpt",
        auth_mode="none",
    )
    server = create_mcp_server(chatgpt_config)
    async with Client(server) as client:
        tools = sorted(tool.name for tool in await client.list_tools())
        expected_tools = sorted(CHATGPT_TOOL_NAMES)
        if tools != expected_tools:
            raise RuntimeError(f"unexpected remote tools: {tools}")

        search_result = await client.call_tool(
            "search",
            {"query": "dummy read-only search fetch"},
        )
        search_payload = json.loads(search_result.content[0].text)
        if search_payload != search_result.structured_content:
            raise RuntimeError("search content fallback did not match structured content")
        results = search_payload.get("results", [])
        if not results:
            raise RuntimeError("remote search returned no results for test corpus")

        fetch_result = await client.call_tool("fetch", {"id": results[0]["id"]})
        fetch_payload = json.loads(fetch_result.content[0].text)
        if fetch_payload != fetch_result.structured_content:
            raise RuntimeError("fetch content fallback did not match structured content")
        fetch_json = json.dumps(fetch_payload)
        if any(marker in fetch_json for marker in ("/Users/", "/private/", "corpus/")):
            raise RuntimeError("remote fetch payload leaked a private path")

    internal_config = HttpMcpConfig(
        index_dir=str(index_dir),
        host="127.0.0.1",
        port=8000,
        transport="streamable-http",
        path="/mcp",
        tool_mode="internal",
        auth_mode="none",
    )
    internal_server = create_mcp_server(internal_config)
    async with Client(internal_server) as client:
        internal_tools = sorted(tool.name for tool in await client.list_tools())
        if internal_tools != sorted(INTERNAL_TOOL_NAMES):
            raise RuntimeError(f"unexpected internal tools: {internal_tools}")
        stats_result = await client.call_tool("rag_stats", {})
        stats_payload = json.loads(stats_result.content[0].text)
        if stats_payload.get("chunk_count", 0) < 1:
            raise RuntimeError(f"unexpected stats payload: {stats_payload}")

    return {
        "tools": tools,
        "search_results": len(results),
        "stats_chunk_count": stats_payload["chunk_count"],
        "first_fetch_id": fetch_payload["id"],
        "internal_tools": internal_tools,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a harmless test index and smoke-test the remote MCP server locally."
    )
    parser.add_argument(
        "--corpus-path",
        default=str(DEFAULT_FIXTURE_CORPUS),
        help="Fixture corpus path for the tiny test index.",
    )
    parser.add_argument(
        "--index-dir",
        default=str(DEFAULT_TEST_INDEX),
        help="Temporary index directory used for smoke testing.",
    )
    args = parser.parse_args()

    corpus_path = Path(args.corpus_path)
    index_dir = Path(args.index_dir)
    if not corpus_path.exists():
        raise SystemExit(f"fixture corpus does not exist: {corpus_path}")

    build_test_index(corpus_path, index_dir)
    sources = verify_index_sources(index_dir, "deploy/azure/test_corpus/")
    verify_failure_modes(index_dir)
    mcp_result = asyncio.run(verify_inprocess_mcp(index_dir))

    stats = _run(
        [
            _python(),
            "-m",
            "math_rag.cli",
            "stats",
            "--index-dir",
            str(index_dir),
        ]
    )

    summary = {
        "index_dir": "<fixture-index>",
        "sources": safe_source_ids(sources),
        "stats": safe_stats_text(stats.stdout.strip(), index_dir),
        "mcp": mcp_result,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
