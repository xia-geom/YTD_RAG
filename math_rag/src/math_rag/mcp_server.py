"""Local MCP stdio server for math_rag.

This server speaks the Model Context Protocol over stdio so that agentic
coding tools such as Codex and Claude Code can call the local RAG system
directly. By default only read-only tools are exposed.

The implementation uses JSON-RPC 2.0 over stdio with line-delimited JSON, the
same wire format Codex and Claude Code expect for ``mcp add --transport stdio``.
It deliberately does not depend on the ``mcp`` Python SDK so that the server
runs in any project Python environment.

Run:

    python -m math_rag.mcp_server
"""

from __future__ import annotations

import json
import os
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from . import __version__
from .config import DEFAULT_INDEX_DIR
from .rag_service import (
    IndexNotFoundError,
    ask_corpus,
    get_chunk,
    ingest_path,
    list_sources,
    search_corpus,
)


PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "math-rag"
WRITE_TOOLS_ENV_FLAG = "MATH_RAG_MCP_ALLOW_WRITE_TOOLS"
ROOT_ENV_VAR = "MATH_RAG_ROOT"
PACKAGE_ROOT_ENV_VAR = "MATH_RAG_PACKAGE_ROOT"
WORKSPACE_ROOT_ENV_VAR = "MATH_RAG_WORKSPACE_ROOT"
INDEX_DIR_ENV_VAR = "MATH_RAG_INDEX_DIR"
MAX_RESPONSE_BYTES = 256 * 1024  # 256 KiB safety cap on a single tool response


# ---------------------------------------------------------------------------
# Project root resolution
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ResolvedRoots:
    package_root: Path
    workspace_root: Path


def _looks_like_package_root(path: Path) -> bool:
    return (path / "pyproject.toml").exists() and (path / "src" / "math_rag").exists()


def _looks_like_workspace_root(path: Path) -> bool:
    return (
        (path / "corpus").exists()
        or (path / "eval").exists()
        or (path / DEFAULT_INDEX_DIR).exists()
        or _looks_like_package_root(path / "math_rag")
    )


def _module_package_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _resolve_existing_env_path(name: str) -> Path | None:
    value = os.environ.get(name)
    if not value:
        return None
    candidate = Path(value).expanduser().resolve()
    if not candidate.exists():
        raise FileNotFoundError(f"{name} points to {candidate}, which does not exist.")
    return candidate


def resolve_package_root() -> Path:
    env_package_root = _resolve_existing_env_path(PACKAGE_ROOT_ENV_VAR)
    if env_package_root:
        if not _looks_like_package_root(env_package_root):
            raise FileNotFoundError(
                f"{PACKAGE_ROOT_ENV_VAR} points to {env_package_root}, but it does not contain "
                "pyproject.toml and src/math_rag/."
            )
        return env_package_root

    legacy_root = _resolve_existing_env_path(ROOT_ENV_VAR)
    if legacy_root and _looks_like_package_root(legacy_root):
        return legacy_root

    cwd = Path.cwd().resolve()
    candidates = [cwd, cwd / "math_rag", _module_package_root()]
    for candidate in candidates:
        if _looks_like_package_root(candidate):
            return candidate.resolve()

    raise FileNotFoundError(
        "Could not locate the math_rag package root. "
        f"Set {PACKAGE_ROOT_ENV_VAR}=/absolute/path/to/YTD_RAG/math_rag."
    )


def resolve_workspace_root(package_root: Path | None = None) -> Path:
    package_root = package_root or resolve_package_root()

    env_workspace_root = _resolve_existing_env_path(WORKSPACE_ROOT_ENV_VAR)
    if env_workspace_root:
        return env_workspace_root

    legacy_root = _resolve_existing_env_path(ROOT_ENV_VAR)
    if legacy_root:
        if _looks_like_package_root(legacy_root) and _looks_like_workspace_root(legacy_root.parent):
            return legacy_root.parent.resolve()
        return legacy_root

    candidates = [Path.cwd().resolve(), package_root.parent, package_root]
    for candidate in candidates:
        if _looks_like_workspace_root(candidate):
            return candidate.resolve()
    return package_root.resolve()


def resolve_roots() -> ResolvedRoots:
    package_root = resolve_package_root()
    workspace_root = resolve_workspace_root(package_root)
    return ResolvedRoots(package_root=package_root, workspace_root=workspace_root)


def resolve_project_root() -> Path:
    """Resolve the workspace root used for path validation.

    ``MATH_RAG_ROOT`` is kept as a legacy alias. Prefer explicit
    ``MATH_RAG_WORKSPACE_ROOT`` and ``MATH_RAG_PACKAGE_ROOT``.

    Raises:
        FileNotFoundError: with a clear message if neither method works.
    """

    return resolve_roots().workspace_root


def _resolve_index_dir(workspace_root: Path) -> str:
    override = os.environ.get(INDEX_DIR_ENV_VAR)
    if override:
        return override
    return str(workspace_root / DEFAULT_INDEX_DIR)


def _write_tools_enabled() -> bool:
    return os.environ.get(WRITE_TOOLS_ENV_FLAG, "").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


# ---------------------------------------------------------------------------
# Tool registry
# ---------------------------------------------------------------------------


READ_ONLY_TOOLS: list[dict[str, Any]] = [
    {
        "name": "rag_search",
        "description": (
            "Search the indexed mathematical corpus using hybrid retrieval "
            "(keyword + sparse vector). Returns ranked chunks with source "
            "metadata and snippets. Read-only."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query."},
                "top_k": {
                    "type": "integer",
                    "description": "Number of results to return.",
                    "default": 8,
                    "minimum": 1,
                    "maximum": 50,
                },
                "source_filter": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of substrings; only sources whose path contains one of these is searched.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "rag_ask",
        "description": (
            "Answer a mathematical research question using ONLY retrieved "
            "corpus evidence. The output keeps evidence, inference, and "
            "not-established claims separated, and never claims to verify a "
            "proof. Read-only."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {"type": "string", "description": "The research question."},
                "top_k": {
                    "type": "integer",
                    "description": "Number of evidence chunks to inspect.",
                    "default": 8,
                    "minimum": 1,
                    "maximum": 50,
                },
                "strict": {
                    "type": "boolean",
                    "description": "If true (default), refuse to speculate beyond retrieved evidence.",
                    "default": True,
                },
            },
            "required": ["question"],
        },
    },
    {
        "name": "rag_get_chunk",
        "description": (
            "Return the full content and metadata for one indexed chunk. "
            "Use after rag_search when a snippet is not enough. Read-only."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "chunk_id": {"type": "string", "description": "Chunk id from rag_search."},
            },
            "required": ["chunk_id"],
        },
    },
    {
        "name": "rag_list_sources",
        "description": (
            "List indexed sources in the corpus, optionally filtered by "
            "substring. Read-only."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "source_filter": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of substrings.",
                },
            },
        },
    },
]


WRITE_TOOLS: list[dict[str, Any]] = [
    {
        "name": "rag_ingest",
        "description": (
            "Re-ingest a local corpus path into the math_rag index. Disabled "
            f"unless {WRITE_TOOLS_ENV_FLAG}=true."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Corpus path relative to the workspace root.", "default": "corpus/"},
                "metadata": {"type": "string", "description": "Optional metadata YAML path relative to the workspace root."},
            },
        },
    },
]


class ToolError(Exception):
    """Raised by tool handlers to return a structured error."""


def _truncate_text(text: str, limit: int | None = None) -> tuple[str, bool]:
    if limit is None:
        limit = MAX_RESPONSE_BYTES
    encoded = text.encode("utf-8")
    if len(encoded) <= limit:
        return text, False
    headroom = max(64, min(256, limit // 4))
    cropped = encoded[: max(0, limit - headroom)].decode("utf-8", errors="ignore")
    return cropped + "\n... [truncated to fit MCP response size limit]", True


def _json_text_payload(data: Any) -> dict[str, Any]:
    text = json.dumps(data, indent=2, ensure_ascii=False, default=str)
    truncated_text, was_truncated = _truncate_text(text)
    if was_truncated and isinstance(data, dict):
        data = dict(data)
        data["_response_truncated"] = True
        data["_hint"] = (
            "Response too large; use rag_get_chunk for a specific chunk_id "
            "or rerun with a smaller top_k."
        )
        text = json.dumps(data, indent=2, ensure_ascii=False, default=str)
        truncated_text, _ = _truncate_text(text)
    return {"content": [{"type": "text", "text": truncated_text}]}


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------


def _safe_path_under_root(path: str, root: Path) -> Path:
    raw = Path(path)
    if raw.is_absolute():
        raise ToolError(
            f"Refusing absolute path argument {path!r}; paths must be relative to the workspace root."
        )
    candidate = (root / raw).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ToolError(
            f"Refusing to operate on path outside the workspace root: {candidate}"
        ) from exc
    return candidate


def _handle_rag_search(args: dict[str, Any], index_dir: str, root: Path) -> dict[str, Any]:
    query = args.get("query")
    if not isinstance(query, str) or not query.strip():
        raise ToolError("query must be a non-empty string")
    top_k = int(args.get("top_k", 8))
    source_filter = args.get("source_filter") or None
    if source_filter is not None and not isinstance(source_filter, list):
        raise ToolError("source_filter must be a list of strings")
    try:
        return search_corpus(query, top_k=top_k, source_filter=source_filter, index_dir=index_dir)
    except IndexNotFoundError as exc:
        raise ToolError(str(exc)) from exc


def _handle_rag_ask(args: dict[str, Any], index_dir: str, root: Path) -> dict[str, Any]:
    question = args.get("question")
    if not isinstance(question, str) or not question.strip():
        raise ToolError("question must be a non-empty string")
    top_k = int(args.get("top_k", 8))
    strict = bool(args.get("strict", True))
    try:
        return ask_corpus(question, top_k=top_k, strict=strict, index_dir=index_dir)
    except IndexNotFoundError as exc:
        raise ToolError(str(exc)) from exc


def _handle_rag_get_chunk(args: dict[str, Any], index_dir: str, root: Path) -> dict[str, Any]:
    chunk_id = args.get("chunk_id")
    if not isinstance(chunk_id, str) or not chunk_id.strip():
        raise ToolError("chunk_id must be a non-empty string")
    try:
        return get_chunk(chunk_id, index_dir=index_dir)
    except IndexNotFoundError as exc:
        raise ToolError(str(exc)) from exc
    except KeyError as exc:
        raise ToolError(str(exc).strip("'")) from exc


def _handle_rag_list_sources(args: dict[str, Any], index_dir: str, root: Path) -> dict[str, Any]:
    source_filter = args.get("source_filter") or None
    if source_filter is not None and not isinstance(source_filter, list):
        raise ToolError("source_filter must be a list of strings")
    try:
        return list_sources(source_filter=source_filter, index_dir=index_dir)
    except IndexNotFoundError as exc:
        raise ToolError(str(exc)) from exc


def _handle_rag_ingest(args: dict[str, Any], index_dir: str, root: Path) -> dict[str, Any]:
    if not _write_tools_enabled():
        raise ToolError(
            f"rag_ingest is disabled. Set {WRITE_TOOLS_ENV_FLAG}=true to enable write tools."
        )
    path = args.get("path", "corpus/")
    metadata = args.get("metadata")
    safe_path = _safe_path_under_root(str(path), root)
    safe_metadata: str | None = None
    if metadata is not None:
        if not isinstance(metadata, str) or not metadata.strip():
            raise ToolError("metadata must be a non-empty string when provided")
        safe_metadata = str(_safe_path_under_root(metadata, root))
    return ingest_path(str(safe_path), index_dir=index_dir, metadata=safe_metadata)


HandlerFn = Callable[[dict[str, Any], str, Path], dict[str, Any]]

TOOL_HANDLERS: dict[str, HandlerFn] = {
    "rag_search": _handle_rag_search,
    "rag_ask": _handle_rag_ask,
    "rag_get_chunk": _handle_rag_get_chunk,
    "rag_list_sources": _handle_rag_list_sources,
    "rag_ingest": _handle_rag_ingest,
}


def list_tools() -> list[dict[str, Any]]:
    tools = list(READ_ONLY_TOOLS)
    if _write_tools_enabled():
        tools.extend(WRITE_TOOLS)
    return tools


# ---------------------------------------------------------------------------
# JSON-RPC dispatch
# ---------------------------------------------------------------------------


def _make_error(code: int, message: str, *, request_id: Any = None, data: Any = None) -> dict[str, Any]:
    error: dict[str, Any] = {"code": code, "message": message}
    if data is not None:
        error["data"] = data
    return {"jsonrpc": "2.0", "id": request_id, "error": error}


def _make_result(result: Any, *, request_id: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def handle_request(request: dict[str, Any], *, index_dir: str, root: Path) -> dict[str, Any] | None:
    """Dispatch a single JSON-RPC request. Returns a response, or None for notifications."""

    method = request.get("method")
    request_id = request.get("id")
    params = request.get("params") or {}
    is_notification = "id" not in request

    if method == "initialize":
        return _make_result(
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": SERVER_NAME, "version": __version__},
            },
            request_id=request_id,
        )
    if method in {"notifications/initialized", "initialized"}:
        return None
    if method == "ping":
        return _make_result({}, request_id=request_id)
    if method == "tools/list":
        return _make_result({"tools": list_tools()}, request_id=request_id)
    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments") or {}
        if name not in TOOL_HANDLERS:
            return _make_error(-32601, f"Unknown tool: {name!r}", request_id=request_id)
        if name in {tool["name"] for tool in WRITE_TOOLS} and not _write_tools_enabled():
            return _make_result(
                {
                    "isError": True,
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                f"Tool {name!r} is disabled. Set "
                                f"{WRITE_TOOLS_ENV_FLAG}=true to enable write tools."
                            ),
                        }
                    ],
                },
                request_id=request_id,
            )
        try:
            handler = TOOL_HANDLERS[name]
            payload = handler(arguments, index_dir, root)
            response_payload = _json_text_payload(payload)
            return _make_result(response_payload, request_id=request_id)
        except ToolError as exc:
            return _make_result(
                {"isError": True, "content": [{"type": "text", "text": str(exc)}]},
                request_id=request_id,
            )
        except Exception as exc:  # pragma: no cover - defensive
            traceback.print_exc(file=sys.stderr)
            return _make_result(
                {
                    "isError": True,
                    "content": [{"type": "text", "text": f"{type(exc).__name__}: {exc}"}],
                },
                request_id=request_id,
            )

    if is_notification:
        return None
    return _make_error(-32601, f"Method not found: {method!r}", request_id=request_id)


# ---------------------------------------------------------------------------
# Stdio loop
# ---------------------------------------------------------------------------


def _send(message: dict[str, Any], stream=sys.stdout) -> None:
    text = json.dumps(message, ensure_ascii=False, default=str)
    stream.write(text + "\n")
    stream.flush()


def serve_stdio(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr) -> int:
    try:
        roots = resolve_roots()
    except FileNotFoundError as exc:
        stderr.write(f"math_rag MCP server: {exc}\n")
        stderr.flush()
        return 2
    index_dir = _resolve_index_dir(roots.workspace_root)
    stderr.write(
        f"math_rag MCP server v{__version__} starting; package_root={roots.package_root}; "
        f"workspace_root={roots.workspace_root}; index_dir={index_dir}; "
        f"write_tools_enabled={_write_tools_enabled()}\n"
    )
    stderr.flush()

    for raw_line in stdin:
        line = raw_line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError as exc:
            _send(_make_error(-32700, f"Parse error: {exc}"), stream=stdout)
            continue
        if not isinstance(request, dict):
            _send(_make_error(-32600, "Invalid Request: expected JSON object"), stream=stdout)
            continue
        response = handle_request(request, index_dir=index_dir, root=roots.workspace_root)
        if response is not None:
            _send(response, stream=stdout)
    return 0


def main() -> int:
    return serve_stdio()


if __name__ == "__main__":
    raise SystemExit(main())
