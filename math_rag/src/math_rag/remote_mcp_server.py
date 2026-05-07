"""Remote read-only MCP server adapter for ChatGPT-style search/fetch tools.

This module is intentionally separate from :mod:`math_rag.mcp_server`, which
serves the local stdio MCP tools used by Codex and Claude Code. The remote
server exposes only two data tools, ``search`` and ``fetch``, and never exposes
ingestion, downloader, discovery, filesystem, or shell operations.
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any
from urllib.parse import quote, urlparse

from . import __version__
from .config import DEFAULT_INDEX_DIR
from .mcp_server import INDEX_DIR_ENV_VAR, WRITE_TOOLS_ENV_FLAG, _resolve_index_dir, resolve_roots
from .rag_service import IndexNotFoundError, get_chunk, search_corpus


REMOTE_READ_ONLY_ENV_VAR = "MATH_RAG_REMOTE_MCP_READ_ONLY"
REMOTE_PUBLIC_BASE_URL_ENV_VAR = "MATH_RAG_REMOTE_PUBLIC_BASE_URL"
REMOTE_HOST_ENV_VAR = "MATH_RAG_REMOTE_HOST"
REMOTE_PORT_ENV_VAR = "MATH_RAG_REMOTE_PORT"
REMOTE_TRANSPORT_ENV_VAR = "MATH_RAG_REMOTE_TRANSPORT"
REMOTE_PATH_ENV_VAR = "MATH_RAG_REMOTE_PATH"
REMOTE_SEARCH_TOP_K_ENV_VAR = "MATH_RAG_REMOTE_SEARCH_TOP_K"

REMOTE_TOOL_NAMES = ("search", "fetch")
DEFAULT_REMOTE_HOST = "0.0.0.0"
DEFAULT_REMOTE_PORT = 8000
DEFAULT_REMOTE_TRANSPORT = "http"
DEFAULT_REMOTE_PATH = "/mcp/"
DEFAULT_REMOTE_SEARCH_TOP_K = 8
MAX_REMOTE_SEARCH_TOP_K = 20
INDEX_NOT_FOUND_REMOTE_MESSAGE = (
    "Index not found or empty; verify MATH_RAG_INDEX_DIR points to a mounted math_rag index."
)
ABSOLUTE_LOCAL_PATH_RE = re.compile(
    r"(?P<path>(?:/Users|/home|/private|/var|/tmp|/Volumes)/[^\s\"'<>),;]+)"
)


class RemoteMcpConfigError(RuntimeError):
    """Raised when remote MCP configuration is unsafe or incomplete."""


@dataclass(frozen=True)
class RemoteMcpConfig:
    index_dir: str
    public_base_url: str
    host: str = DEFAULT_REMOTE_HOST
    port: int = DEFAULT_REMOTE_PORT
    transport: str = DEFAULT_REMOTE_TRANSPORT
    path: str = DEFAULT_REMOTE_PATH
    search_top_k: int = DEFAULT_REMOTE_SEARCH_TOP_K


def _truthy(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "on"}


def _falsey(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"0", "false", "no", "off"}


def _env_int(name: str, default: int, *, minimum: int, maximum: int) -> int:
    raw = os.environ.get(name)
    if raw is None or not raw.strip():
        return default
    try:
        value = int(raw)
    except ValueError as exc:
        raise RemoteMcpConfigError(f"{name} must be an integer.") from exc
    if value < minimum or value > maximum:
        raise RemoteMcpConfigError(f"{name} must be between {minimum} and {maximum}.")
    return value


def _normalize_public_base_url(value: str | None) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RemoteMcpConfigError(
            f"{REMOTE_PUBLIC_BASE_URL_ENV_VAR} is required for remote MCP citation URLs."
        )
    base_url = value.strip().rstrip("/")
    parsed = urlparse(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise RemoteMcpConfigError(
            f"{REMOTE_PUBLIC_BASE_URL_ENV_VAR} must be an absolute http(s) URL."
        )
    return base_url


def _default_index_dir() -> str:
    if os.environ.get(INDEX_DIR_ENV_VAR):
        return os.environ[INDEX_DIR_ENV_VAR]
    try:
        roots = resolve_roots()
    except FileNotFoundError:
        return DEFAULT_INDEX_DIR
    return _resolve_index_dir(roots.workspace_root)


def validate_remote_read_only_environment() -> None:
    """Reject remote startup if any write-capable MCP setting is enabled."""

    if _truthy(os.environ.get(WRITE_TOOLS_ENV_FLAG)):
        raise RemoteMcpConfigError(
            f"Remote MCP refuses to start while {WRITE_TOOLS_ENV_FLAG}=true."
        )
    if _falsey(os.environ.get(REMOTE_READ_ONLY_ENV_VAR)):
        raise RemoteMcpConfigError(
            f"Remote MCP is read-only only; do not set {REMOTE_READ_ONLY_ENV_VAR}=false."
        )


def resolve_remote_config(
    *,
    index_dir: str | None = None,
    public_base_url: str | None = None,
) -> RemoteMcpConfig:
    """Resolve safe remote MCP configuration from explicit args and env vars."""

    validate_remote_read_only_environment()
    return RemoteMcpConfig(
        index_dir=index_dir or _default_index_dir(),
        public_base_url=_normalize_public_base_url(
            public_base_url or os.environ.get(REMOTE_PUBLIC_BASE_URL_ENV_VAR)
        ),
        host=os.environ.get(REMOTE_HOST_ENV_VAR, DEFAULT_REMOTE_HOST),
        port=_env_int(REMOTE_PORT_ENV_VAR, DEFAULT_REMOTE_PORT, minimum=1, maximum=65535),
        transport=os.environ.get(REMOTE_TRANSPORT_ENV_VAR, DEFAULT_REMOTE_TRANSPORT),
        path=os.environ.get(REMOTE_PATH_ENV_VAR, DEFAULT_REMOTE_PATH),
        search_top_k=_env_int(
            REMOTE_SEARCH_TOP_K_ENV_VAR,
            DEFAULT_REMOTE_SEARCH_TOP_K,
            minimum=1,
            maximum=MAX_REMOTE_SEARCH_TOP_K,
        ),
    )


def chunk_url(chunk_id: str, public_base_url: str) -> str:
    """Return a stable public identifier URL without exposing local file paths."""

    return f"{public_base_url.rstrip('/')}/chunks/{quote(chunk_id, safe='')}"


def list_remote_tool_names() -> tuple[str, ...]:
    return REMOTE_TOOL_NAMES


def _safe_title(item: dict[str, Any]) -> str:
    title = str(item.get("title") or "").strip()
    if not title:
        title = str(item.get("source_path") or "math_rag source").split("/")[-1]
    chunk_type = str(item.get("chunk_type") or "").strip()
    if chunk_type and chunk_type != "text":
        return f"{title} ({chunk_type})"
    return title


def _safe_source_path(value: Any) -> str:
    source_path = str(value or "").replace("\\", "/")
    if not source_path:
        return ""
    parts = [part for part in PurePosixPath(source_path).parts if part not in {"/", ""}]
    for marker in ("corpus", "agent_logs", "eval", "metadata"):
        if marker in parts:
            return "/".join(parts[parts.index(marker) :])
    if source_path.startswith("/") or ":" in source_path:
        return PurePosixPath(source_path).name
    return source_path


def _scrub_local_paths(value: str) -> str:
    return ABSOLUTE_LOCAL_PATH_RE.sub(
        lambda match: _safe_source_path(match.group("path")),
        value,
    )


def _sanitize_metadata(value: Any, *, key: str = "") -> Any:
    if isinstance(value, dict):
        return {str(k): _sanitize_metadata(v, key=str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize_metadata(item, key=key) for item in value]
    if isinstance(value, str) and "path" in key.lower():
        return _safe_source_path(_scrub_local_paths(value))
    if isinstance(value, str):
        return _scrub_local_paths(value)
    return value


def _remote_citation(item: dict[str, Any]) -> str:
    source_path = _safe_source_path(item.get("source_path"))
    line_start = item.get("line_start")
    line_end = item.get("line_end")
    page_number = item.get("page_number")
    if line_start and line_end:
        return f"{source_path}:lines {line_start}-{line_end}"
    if line_start:
        return f"{source_path}:line {line_start}"
    if page_number:
        return f"{source_path}:page {page_number}"
    return source_path


def _search_result_for_remote(item: dict[str, Any], public_base_url: str) -> dict[str, Any]:
    chunk_id = str(item.get("chunk_id") or "")
    metadata = {
        "source_path": _safe_source_path(item.get("source_path")),
        "chunk_type": item.get("chunk_type"),
        "section_path": item.get("section_path") or [],
        "page_number": item.get("page_number"),
        "line_start": item.get("line_start"),
        "line_end": item.get("line_end"),
        "citation": _remote_citation(item),
        "score": item.get("score"),
        "rank": item.get("rank"),
    }
    return {
        "id": chunk_id,
        "title": _safe_title(item),
        "url": chunk_url(chunk_id, public_base_url),
        "text": item.get("snippet") or "",
        "metadata": metadata,
    }


def search_payload(
    query: str,
    *,
    index_dir: str,
    public_base_url: str,
    top_k: int = DEFAULT_REMOTE_SEARCH_TOP_K,
) -> dict[str, Any]:
    """Return a ChatGPT-compatible ``search`` payload."""

    if not isinstance(query, str) or not query.strip():
        return {
            "results": [],
            "error": {"code": "invalid_query", "message": "query must be a non-empty string"},
        }
    try:
        payload = search_corpus(
            query,
            top_k=max(1, min(int(top_k), MAX_REMOTE_SEARCH_TOP_K)),
            index_dir=index_dir,
        )
    except IndexNotFoundError:
        return {
            "results": [],
            "error": {"code": "index_not_found", "message": INDEX_NOT_FOUND_REMOTE_MESSAGE},
        }
    except Exception as exc:  # pragma: no cover - defensive remote safety
        return {
            "results": [],
            "error": {"code": type(exc).__name__, "message": _scrub_local_paths(str(exc))},
        }

    return {
        "results": [
            _search_result_for_remote(item, public_base_url)
            for item in payload.get("results", [])
            if item.get("chunk_id")
        ]
    }


def fetch_payload(
    id: str,
    *,
    index_dir: str,
    public_base_url: str,
) -> dict[str, Any]:
    """Return a ChatGPT-compatible ``fetch`` payload."""

    chunk_id = id
    if not isinstance(chunk_id, str) or not chunk_id.strip():
        return {
            "id": "",
            "title": "Invalid chunk id",
            "text": "",
            "url": chunk_url("invalid", public_base_url),
            "metadata": {},
            "error": {"code": "invalid_id", "message": "id must be a non-empty string"},
        }
    try:
        item = get_chunk(chunk_id, index_dir=index_dir)
    except IndexNotFoundError:
        return {
            "id": chunk_id,
            "title": "Index not found",
            "text": "",
            "url": chunk_url(chunk_id, public_base_url),
            "metadata": {},
            "error": {"code": "index_not_found", "message": INDEX_NOT_FOUND_REMOTE_MESSAGE},
        }
    except KeyError:
        return {
            "id": chunk_id,
            "title": "Chunk not found",
            "text": "",
            "url": chunk_url(chunk_id, public_base_url),
            "metadata": {},
            "error": {"code": "not_found", "message": f"chunk id {chunk_id!r} was not found"},
        }
    except Exception as exc:  # pragma: no cover - defensive remote safety
        return {
            "id": chunk_id,
            "title": "Fetch error",
            "text": "",
            "url": chunk_url(chunk_id, public_base_url),
            "metadata": {},
            "error": {"code": type(exc).__name__, "message": _scrub_local_paths(str(exc))},
        }

    metadata = {
        "source_path": _safe_source_path(item.get("source_path")),
        "chunk_type": item.get("chunk_type"),
        "section_path": item.get("section_path") or [],
        "section_path_string": item.get("section_path_string"),
        "page_number": item.get("page_number"),
        "line_start": item.get("line_start"),
        "line_end": item.get("line_end"),
        "citation": _remote_citation(item),
        "symbols": item.get("symbols") or [],
        "topics": item.get("topics") or [],
        "content_truncated": item.get("content_truncated", False),
        "chunk_metadata": _sanitize_metadata(item.get("metadata") or {}),
    }
    return {
        "id": item.get("chunk_id") or chunk_id,
        "title": _safe_title(item),
        "text": item.get("content") or "",
        "url": chunk_url(chunk_id, public_base_url),
        "metadata": metadata,
    }


def _json_dumps(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def search_json(
    query: str,
    *,
    index_dir: str,
    public_base_url: str,
    top_k: int = DEFAULT_REMOTE_SEARCH_TOP_K,
) -> str:
    return _json_dumps(
        search_payload(query, index_dir=index_dir, public_base_url=public_base_url, top_k=top_k)
    )


def fetch_json(id: str, *, index_dir: str, public_base_url: str) -> str:
    return _json_dumps(fetch_payload(id, index_dir=index_dir, public_base_url=public_base_url))


def _json_text_content(json_text: str) -> dict[str, Any]:
    return {"content": [{"type": "text", "text": json_text}]}


def search_tool_response(
    query: str,
    *,
    index_dir: str,
    public_base_url: str,
    top_k: int = DEFAULT_REMOTE_SEARCH_TOP_K,
) -> dict[str, Any]:
    """Return the exact one-text-content-item shape required by MCP clients."""

    return _json_text_content(
        search_json(query, index_dir=index_dir, public_base_url=public_base_url, top_k=top_k)
    )


def fetch_tool_response(id: str, *, index_dir: str, public_base_url: str) -> dict[str, Any]:
    """Return the exact one-text-content-item shape required by MCP clients."""

    return _json_text_content(fetch_json(id, index_dir=index_dir, public_base_url=public_base_url))


def create_mcp_server(config: RemoteMcpConfig | None = None) -> Any:
    """Create a FastMCP server exposing only ``search`` and ``fetch``."""

    config = config or resolve_remote_config()
    try:
        from fastmcp import FastMCP
    except ImportError as exc:  # pragma: no cover - optional dependency path
        raise RuntimeError(
            "Remote MCP serving requires the optional dependency group: "
            "pip install -e '.[remote-mcp]'"
        ) from exc

    mcp = FastMCP(name=f"math-rag-remote-{__version__}")

    @mcp.tool
    def search(query: str) -> str:
        """Search the indexed math_rag corpus and return JSON text with results."""

        return search_json(
            query,
            index_dir=config.index_dir,
            public_base_url=config.public_base_url,
            top_k=config.search_top_k,
        )

    @mcp.tool
    def fetch(id: str) -> str:
        """Fetch one indexed math_rag chunk by id and return JSON text."""

        return fetch_json(id, index_dir=config.index_dir, public_base_url=config.public_base_url)

    return mcp


def main() -> None:
    """Run the remote MCP server over FastMCP HTTP transport."""

    try:
        config = resolve_remote_config()
        mcp = create_mcp_server(config)
    except (RemoteMcpConfigError, RuntimeError) as exc:
        sys.stderr.write(f"math_rag remote MCP server: {exc}\n")
        raise SystemExit(2) from exc

    mcp.run(
        transport=config.transport,
        host=config.host,
        port=config.port,
        path=config.path,
    )


if __name__ == "__main__":  # pragma: no cover - exercised by deployment
    main()
