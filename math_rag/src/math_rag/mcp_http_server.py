"""Remote read-only MCP server over Streamable HTTP.

This entrypoint is separate from :mod:`math_rag.mcp_server`, the local stdio
server used by local agents. It exposes only read-only tools backed by
``rag_service`` and treats retrieved document text as untrusted corpus evidence,
not as instructions.
"""

from __future__ import annotations

import json
import logging
import os
import re
import secrets
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Callable
from urllib.parse import quote, urlparse

from . import __version__
from .config import DEFAULT_INDEX_DIR
from .index_store import INDEX_FILENAME, IndexStore
from .mcp_server import INDEX_DIR_ENV_VAR, WRITE_TOOLS_ENV_FLAG, _resolve_index_dir, resolve_roots
from .rag_service import (
    IndexNotFoundError,
    ask_corpus,
    get_chunk,
    index_stats,
    list_sources,
    search_corpus,
)


API_KEY_ENV_VAR = "MATH_RAG_API_KEY"
API_TOKEN_ENV_VAR = "MATH_RAG_API_TOKEN"
ALLOW_NO_AUTH_ENV_VAR = "MATH_RAG_REMOTE_ALLOW_NO_AUTH"
ALLOW_UNAUTHENTICATED_PUBLIC_ENV_VAR = "MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC"
AUTH_MODE_ENV_VAR = "MATH_RAG_AUTH_MODE"
ALLOWED_ORIGINS_ENV_VAR = "MATH_RAG_ALLOWED_ORIGINS"
FETCH_MAX_CHARS_ENV_VAR = "MATH_RAG_FETCH_MAX_CHARS"
INDEX_FILE_ENV_VAR = "MATH_RAG_INDEX"
LOG_LEVEL_ENV_VAR = "MATH_RAG_LOG_LEVEL"
MAX_TOP_K_ENV_VAR = "MATH_RAG_MAX_TOP_K"
PROTECT_HEALTH_ENV_VAR = "MATH_RAG_PROTECT_HEALTH"
PUBLIC_BASE_URL_ENV_VAR = "MATH_RAG_PUBLIC_BASE_URL"
READY_PATH = "/readyz"
REMOTE_PATH_ENV_VAR = "MATH_RAG_REMOTE_PATH"
REMOTE_PUBLIC_BASE_URL_ENV_VAR = "MATH_RAG_REMOTE_PUBLIC_BASE_URL"
REMOTE_READ_ONLY_ENV_VAR = "MATH_RAG_REMOTE_MCP_READ_ONLY"
REMOTE_SEARCH_TOP_K_ENV_VAR = "MATH_RAG_REMOTE_SEARCH_TOP_K"
REMOTE_TRANSPORT_ENV_VAR = "MATH_RAG_REMOTE_TRANSPORT"
ROOT_ENV_VAR = "MATH_RAG_ROOT"
SEARCH_TOP_K_ENV_VAR = "MATH_RAG_SEARCH_TOP_K"
SERVER_NAME = "math-rag-http"
TOOL_MODE_ENV_VAR = "MATH_RAG_TOOL_MODE"

REMOTE_HOST_ENV_VAR = "MATH_RAG_REMOTE_HOST"
REMOTE_PORT_ENV_VAR = "MATH_RAG_REMOTE_PORT"
HOST_ENV_VAR = "MATH_RAG_HOST"

CHATGPT_TOOL_MODE = "chatgpt"
INTERNAL_TOOL_MODE = "internal"
ALL_TOOL_MODE = "all"
TOOL_MODES = {CHATGPT_TOOL_MODE, INTERNAL_TOOL_MODE, ALL_TOOL_MODE}

CHATGPT_TOOL_NAMES = ("search", "fetch")
INTERNAL_TOOL_NAMES = (
    "rag_search",
    "rag_get_chunk",
    "rag_list_sources",
    "rag_stats",
    "rag_ask",
)

DEFAULT_HTTP_HOST = "127.0.0.1"
DEFAULT_HTTP_PORT = 8000
DEFAULT_HTTP_TRANSPORT = "streamable-http"
DEFAULT_HTTP_PATH = "/mcp"
HEALTH_PATH = "/healthz"
DEFAULT_SEARCH_TOP_K = 8
DEFAULT_MAX_TOP_K = 20
DEFAULT_FETCH_MAX_CHARS = 12000
INDEX_NOT_FOUND_REMOTE_MESSAGE = (
    "Index not found or empty; verify the configured math_rag index is mounted."
)

ABSOLUTE_LOCAL_PATH_RE = re.compile(
    r"(?P<path>(?:file://)?(?:(?<![A-Za-z])[A-Za-z]:[\\/]|/Users|/home|/private|/var|/tmp|/Volumes)"
    r"[^\s\"'<>),;]*)"
)
ARXIV_PATH_RE = re.compile(r"(?:^|/)corpus/arxiv/([^/]+)(?:/|$)")

logger = logging.getLogger(__name__)


class HttpMcpConfigError(RuntimeError):
    """Raised when remote HTTP MCP configuration is unsafe or incomplete."""


@dataclass(frozen=True)
class HttpMcpConfig:
    index_dir: str
    api_key: str | None = None
    allow_no_auth: bool = False
    host: str = DEFAULT_HTTP_HOST
    port: int = DEFAULT_HTTP_PORT
    transport: str = DEFAULT_HTTP_TRANSPORT
    path: str = DEFAULT_HTTP_PATH
    public_base_url: str | None = None
    tool_mode: str = CHATGPT_TOOL_MODE
    search_top_k: int = DEFAULT_SEARCH_TOP_K
    max_top_k: int = DEFAULT_MAX_TOP_K
    fetch_max_chars: int = DEFAULT_FETCH_MAX_CHARS
    auth_mode: str = "none"
    allowed_origins: tuple[str, ...] = field(default_factory=tuple)
    protect_health: bool = False


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
        raise HttpMcpConfigError(f"{name} must be an integer.") from exc
    if value < minimum or value > maximum:
        raise HttpMcpConfigError(f"{name} must be between {minimum} and {maximum}.")
    return value


def _env_int_first(names: tuple[str, ...], default: int, *, minimum: int, maximum: int) -> int:
    for name in names:
        if os.environ.get(name) is not None:
            return _env_int(name, default, minimum=minimum, maximum=maximum)
    return default


def _normalize_tool_mode(value: str | None) -> str:
    mode = str(value or CHATGPT_TOOL_MODE).strip().lower()
    if mode not in TOOL_MODES:
        raise HttpMcpConfigError(
            f"{TOOL_MODE_ENV_VAR} must be one of: {', '.join(sorted(TOOL_MODES))}."
        )
    return mode


def _normalize_transport(value: str | None) -> str:
    transport = str(value or DEFAULT_HTTP_TRANSPORT).strip()
    if transport not in {"streamable-http", "http", "sse"}:
        raise HttpMcpConfigError(
            f"{REMOTE_TRANSPORT_ENV_VAR} must be streamable-http, http, or sse."
        )
    return transport


def _normalize_path(value: str | None) -> str:
    raw = str(value or DEFAULT_HTTP_PATH).strip()
    if not raw:
        return DEFAULT_HTTP_PATH
    return "/" + raw.strip("/")


def _normalize_public_base_url(value: str | None) -> str | None:
    if value is None or not str(value).strip():
        return None
    base_url = str(value).strip().rstrip("/")
    parsed = urlparse(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise HttpMcpConfigError(
            f"{PUBLIC_BASE_URL_ENV_VAR} must be an absolute http(s) URL when set."
        )
    return base_url


def _default_index_dir() -> str:
    index_file = os.environ.get(INDEX_FILE_ENV_VAR)
    if index_file:
        path = Path(index_file).expanduser()
        return str(path.parent if path.name == INDEX_FILENAME else path)
    if os.environ.get(INDEX_DIR_ENV_VAR):
        return os.environ[INDEX_DIR_ENV_VAR]
    if os.environ.get(ROOT_ENV_VAR):
        return str(Path(os.environ[ROOT_ENV_VAR]).expanduser() / DEFAULT_INDEX_DIR)
    try:
        roots = resolve_roots()
    except FileNotFoundError:
        return DEFAULT_INDEX_DIR
    return _resolve_index_dir(roots.workspace_root)


def _normalize_api_key(value: str | None, *, auth_mode: str) -> str | None:
    api_key = str(value or "").strip()
    if auth_mode == "bearer":
        if api_key:
            return api_key
        raise HttpMcpConfigError(
            f"{API_TOKEN_ENV_VAR} is required when {AUTH_MODE_ENV_VAR}=bearer."
        )
    if api_key:
        return api_key
    return None


def _resolve_auth_mode(host: str) -> str:
    explicit = os.environ.get(AUTH_MODE_ENV_VAR)
    if explicit is not None:
        mode = explicit.strip().lower()
    elif os.environ.get(API_TOKEN_ENV_VAR) or os.environ.get(API_KEY_ENV_VAR):
        mode = "bearer"
    elif _truthy(os.environ.get(ALLOW_NO_AUTH_ENV_VAR)):
        mode = "none"
    else:
        mode = "none"
    if mode not in {"none", "bearer", "oauth"}:
        raise HttpMcpConfigError(f"{AUTH_MODE_ENV_VAR} must be none, bearer, or oauth.")
    if mode == "oauth":
        raise HttpMcpConfigError(
            "OAuth resource-server verification is not implemented in math_rag. "
            "Put OAuth/OIDC validation at the deployment gateway, or use bearer mode for local tests."
        )
    if mode == "none":
        is_public_bind = host not in {"127.0.0.1", "localhost", "::1"}
        if is_public_bind and not _truthy(os.environ.get(ALLOW_UNAUTHENTICATED_PUBLIC_ENV_VAR)):
            raise HttpMcpConfigError(
                f"Refusing unauthenticated public bind on {host!r}. "
                f"Set {ALLOW_UNAUTHENTICATED_PUBLIC_ENV_VAR}=true only for an intentional public test."
            )
        sys.stderr.write(
            "math_rag HTTP MCP server: no-auth mode enabled; use only for localhost/dev.\n"
        )
    return mode


def _parse_allowed_origins(value: str | None) -> tuple[str, ...]:
    if value is None or not value.strip():
        return ()
    origins = tuple(origin.strip() for origin in value.split(",") if origin.strip())
    if "*" in origins:
        raise HttpMcpConfigError(
            f"{ALLOWED_ORIGINS_ENV_VAR}=* is not allowed for this private corpus server."
        )
    return origins


def validate_http_read_only_environment() -> None:
    """Reject remote startup if any write-capable MCP setting is enabled."""

    if _truthy(os.environ.get(WRITE_TOOLS_ENV_FLAG)):
        raise HttpMcpConfigError(
            f"Remote MCP refuses to start while {WRITE_TOOLS_ENV_FLAG}=true."
        )
    if _falsey(os.environ.get(REMOTE_READ_ONLY_ENV_VAR)):
        raise HttpMcpConfigError(
            f"Remote MCP is read-only only; do not set {REMOTE_READ_ONLY_ENV_VAR}=false."
        )


def resolve_http_config(*, index_dir: str | None = None) -> HttpMcpConfig:
    """Resolve safe remote HTTP MCP configuration from explicit args and env vars."""

    validate_http_read_only_environment()
    host = os.environ.get(HOST_ENV_VAR) or os.environ.get(REMOTE_HOST_ENV_VAR) or DEFAULT_HTTP_HOST
    port = _env_int_first(
        ("PORT", REMOTE_PORT_ENV_VAR),
        DEFAULT_HTTP_PORT,
        minimum=1,
        maximum=65535,
    )
    tool_mode = _normalize_tool_mode(os.environ.get(TOOL_MODE_ENV_VAR))
    max_top_k = _env_int(MAX_TOP_K_ENV_VAR, DEFAULT_MAX_TOP_K, minimum=1, maximum=100)
    search_top_k = _env_int_first(
        (SEARCH_TOP_K_ENV_VAR, REMOTE_SEARCH_TOP_K_ENV_VAR),
        DEFAULT_SEARCH_TOP_K,
        minimum=1,
        maximum=max_top_k,
    )
    auth_mode = _resolve_auth_mode(host)
    api_key = _normalize_api_key(
        os.environ.get(API_TOKEN_ENV_VAR) or os.environ.get(API_KEY_ENV_VAR),
        auth_mode=auth_mode,
    )
    return HttpMcpConfig(
        index_dir=index_dir or _default_index_dir(),
        api_key=api_key,
        allow_no_auth=auth_mode == "none",
        host=host,
        port=port,
        transport=_normalize_transport(os.environ.get(REMOTE_TRANSPORT_ENV_VAR)),
        path=_normalize_path(os.environ.get(REMOTE_PATH_ENV_VAR)),
        public_base_url=_normalize_public_base_url(
            os.environ.get(PUBLIC_BASE_URL_ENV_VAR)
            or os.environ.get(REMOTE_PUBLIC_BASE_URL_ENV_VAR)
        ),
        tool_mode=tool_mode,
        search_top_k=search_top_k,
        max_top_k=max_top_k,
        fetch_max_chars=_env_int(
            FETCH_MAX_CHARS_ENV_VAR,
            DEFAULT_FETCH_MAX_CHARS,
            minimum=100,
            maximum=100_000,
        ),
        auth_mode=auth_mode,
        allowed_origins=_parse_allowed_origins(os.environ.get(ALLOWED_ORIGINS_ENV_VAR)),
        protect_health=_truthy(os.environ.get(PROTECT_HEALTH_ENV_VAR)),
    )


def _configure_logging() -> None:
    level_name = os.environ.get(LOG_LEVEL_ENV_VAR, "info").strip().upper()
    level = getattr(logging, level_name, logging.INFO)
    logging.basicConfig(level=level, format="%(levelname)s:%(name)s:%(message)s")


def list_http_tool_names(tool_mode: str = ALL_TOOL_MODE) -> tuple[str, ...]:
    mode = _normalize_tool_mode(tool_mode)
    if mode == CHATGPT_TOOL_MODE:
        return CHATGPT_TOOL_NAMES
    if mode == INTERNAL_TOOL_MODE:
        return INTERNAL_TOOL_NAMES
    return CHATGPT_TOOL_NAMES + INTERNAL_TOOL_NAMES


def _safe_source_id(value: Any) -> str:
    source_path = str(value or "").replace("\\", "/")
    if not source_path:
        return ""
    parts = [part for part in PurePosixPath(source_path).parts if part not in {"/", ""}]
    if "arxiv" in parts:
        index = parts.index("arxiv")
        if index + 1 < len(parts):
            return f"arxiv/{parts[index + 1]}"
    if "corpus" in parts:
        return PurePosixPath(source_path).name
    if source_path.startswith("/") or ":" in source_path or source_path.startswith("~"):
        return PurePosixPath(source_path).name
    return source_path


def _scrub_local_paths(value: str) -> str:
    value = re.sub(r"file://[^\s\"'<>),;]+", lambda match: _safe_source_id(match.group(0)), value)
    value = re.sub(r"~[/\\][^\s\"'<>),;]+", lambda match: PurePosixPath(match.group(0)).name, value)
    return ABSOLUTE_LOCAL_PATH_RE.sub(
        lambda match: _safe_source_id(match.group("path")),
        value,
    )


def sanitize_metadata(value: Any, *, key: str = "") -> Any:
    """Return JSON-safe metadata with local/private paths scrubbed."""

    if isinstance(value, dict):
        return {str(k): sanitize_metadata(v, key=str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [sanitize_metadata(item, key=key) for item in value]
    if isinstance(value, str):
        lowered = key.lower()
        scrubbed = _scrub_local_paths(value)
        if any(marker in lowered for marker in ("path", "file", "dir", "root", "cache", "index", "uri")):
            return _safe_source_id(scrubbed)
        return scrubbed
    return value


def _json_dumps(payload: dict[str, Any]) -> str:
    return json.dumps(sanitize_metadata(payload), ensure_ascii=False, sort_keys=True)


def _tool_result(payload: dict[str, Any]) -> Any:
    from fastmcp.tools import ToolResult
    from mcp.types import TextContent

    payload = sanitize_metadata(payload)
    return ToolResult(
        content=[TextContent(type="text", text=_json_dumps(payload))],
        structured_content=payload,
    )


def _error_payload(code: str, message: str, **extra: Any) -> dict[str, Any]:
    payload = dict(extra)
    payload["error"] = {"code": code, "message": _scrub_local_paths(message)}
    return payload


def _service_payload(
    callback: Callable[[], dict[str, Any]],
    *,
    fallback: dict[str, Any] | None = None,
) -> dict[str, Any]:
    try:
        return sanitize_metadata(callback())
    except IndexNotFoundError:
        return _error_payload("index_not_found", INDEX_NOT_FOUND_REMOTE_MESSAGE, **(fallback or {}))
    except KeyError as exc:
        return _error_payload("not_found", str(exc).strip("'"), **(fallback or {}))
    except ValueError as exc:
        return _error_payload("invalid_request", str(exc), **(fallback or {}))
    except Exception as exc:  # pragma: no cover - defensive remote safety
        return _error_payload(type(exc).__name__, str(exc), **(fallback or {}))


def _normalize_source_filter(source_filter: list[str] | None) -> list[str] | None:
    if source_filter is None:
        return None
    if not isinstance(source_filter, list) or not all(isinstance(item, str) for item in source_filter):
        raise ValueError("source_filter must be a list of strings")
    return source_filter


def _bounded_top_k(value: int, config: HttpMcpConfig) -> int:
    return max(1, min(int(value), int(config.max_top_k)))


def _safe_title(item: dict[str, Any]) -> str:
    title = str(item.get("title") or "").strip()
    if title:
        return title
    source_id = _safe_source_id(item.get("source_path"))
    return source_id or "math_rag source"


def _arxiv_id_from_item(item: dict[str, Any]) -> str | None:
    metadata = item.get("metadata") or item.get("chunk_metadata") or {}
    if isinstance(metadata, dict):
        for key in ("arxiv_id", "requested_arxiv_id"):
            value = metadata.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    match = ARXIV_PATH_RE.search(str(item.get("source_path") or ""))
    if match:
        return match.group(1).replace("_", "/")
    return None


def _safe_public_url(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = value.strip()
    parsed = urlparse(candidate)
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        return candidate
    return None


def build_citation_url(item: dict[str, Any], config: HttpMcpConfig, *, chunk_id: str) -> str:
    metadata = item.get("metadata") or item.get("chunk_metadata") or {}
    arxiv_id = _arxiv_id_from_item(item)
    if arxiv_id:
        return f"https://arxiv.org/abs/{quote(arxiv_id, safe='/')}"
    if isinstance(metadata, dict):
        doi = metadata.get("doi")
        if isinstance(doi, str) and doi.strip():
            return f"https://doi.org/{quote(doi.strip(), safe='/')}"
        for key in ("source_url", "pdf_url"):
            safe_url = _safe_public_url(metadata.get(key))
            if safe_url:
                return safe_url
    if config.public_base_url:
        return f"{config.public_base_url.rstrip('/')}/citation/{quote(chunk_id, safe='')}"
    return f"math-rag://{quote(chunk_id, safe='')}"


def _truncate_text(text: str, max_chars: int) -> tuple[str, bool, int]:
    original_char_count = len(text or "")
    if original_char_count <= max_chars:
        return text or "", False, original_char_count
    return (text or "")[:max_chars].rstrip() + "\n... [truncated]", True, original_char_count


def make_search_result(item: dict[str, Any], config: HttpMcpConfig) -> dict[str, Any]:
    chunk_id = str(item.get("chunk_id") or "")
    return {
        "id": chunk_id,
        "title": _safe_title(item),
        "url": build_citation_url(item, config, chunk_id=chunk_id),
    }


def make_fetch_result(item: dict[str, Any], config: HttpMcpConfig, *, requested_id: str) -> dict[str, Any]:
    chunk_id = str(item.get("chunk_id") or requested_id)
    content = str(item.get("content") or "")
    text, truncated_by_http, original_char_count = _truncate_text(content, config.fetch_max_chars)
    section_path = item.get("section_path") or []
    metadata_source = item.get("metadata") or {}
    safe_metadata: dict[str, Any] = {
        "source_id": _safe_source_id(item.get("source_path")),
        "chunk_id": chunk_id,
        "chunk_type": item.get("chunk_type"),
        "arxiv_id": _arxiv_id_from_item(item),
        "section_title": " / ".join(str(part) for part in section_path) if section_path else None,
        "page": item.get("page_number"),
        "line_start": item.get("line_start"),
        "line_end": item.get("line_end"),
        "truncated": bool(item.get("content_truncated", False)) or truncated_by_http,
        "original_char_count": original_char_count,
    }
    if isinstance(metadata_source, dict):
        for key in ("authors", "year", "citation_key", "doi", "source_url"):
            if metadata_source.get(key) is not None:
                safe_metadata[key] = metadata_source.get(key)
    safe_metadata = {k: v for k, v in sanitize_metadata(safe_metadata).items() if v is not None}
    return {
        "id": chunk_id,
        "title": _safe_title(item),
        "text": text,
        "url": build_citation_url({"metadata": metadata_source, **item}, config, chunk_id=chunk_id),
        "metadata": safe_metadata,
    }


def search_payload(query: str, config: HttpMcpConfig) -> dict[str, Any]:
    if not isinstance(query, str) or not query.strip():
        return {"results": []}
    try:
        payload = search_corpus(query, top_k=config.search_top_k, index_dir=config.index_dir)
    except IndexNotFoundError:
        return _error_payload("index_not_found", INDEX_NOT_FOUND_REMOTE_MESSAGE, results=[])
    except Exception as exc:  # pragma: no cover - defensive remote safety
        return _error_payload(type(exc).__name__, str(exc), results=[])
    seen: set[str] = set()
    results: list[dict[str, Any]] = []
    for item in payload.get("results", []):
        chunk_id = str(item.get("chunk_id") or "")
        if not chunk_id or chunk_id in seen:
            continue
        seen.add(chunk_id)
        results.append(make_search_result(item, config))
    return sanitize_metadata({"results": results})


def fetch_payload(id: str, config: HttpMcpConfig) -> dict[str, Any]:
    if not isinstance(id, str) or not id.strip():
        return {
            "id": "",
            "title": "Invalid id",
            "text": "",
            "url": build_citation_url({}, config, chunk_id="invalid"),
            "metadata": {},
            "error": {"code": "invalid_id", "message": "id must be a non-empty string"},
        }
    try:
        payload = get_chunk(id, index_dir=config.index_dir)
    except IndexNotFoundError:
        return {
            "id": id,
            "title": "Index not found",
            "text": "",
            "url": build_citation_url({}, config, chunk_id=id),
            "metadata": {},
            "error": {"code": "index_not_found", "message": INDEX_NOT_FOUND_REMOTE_MESSAGE},
        }
    except KeyError:
        return {
            "id": id,
            "title": "Chunk not found",
            "text": "",
            "url": build_citation_url({}, config, chunk_id=id),
            "metadata": {},
            "error": {"code": "not_found", "message": f"chunk id {id!r} was not found"},
        }
    except Exception as exc:  # pragma: no cover - defensive remote safety
        return {
            "id": id,
            "title": "Fetch error",
            "text": "",
            "url": build_citation_url({}, config, chunk_id=id),
            "metadata": {},
            "error": {"code": type(exc).__name__, "message": _scrub_local_paths(str(exc))},
        }
    return sanitize_metadata(make_fetch_result(payload, config, requested_id=id))


def _authorization_error_payload(message: str) -> dict[str, Any]:
    return {"error": {"code": "unauthorized", "message": message}}


def _extract_bearer_token(authorization_header: str | None) -> tuple[bool, str]:
    if authorization_header is None:
        return False, "Missing Authorization header"
    if not authorization_header.startswith("Bearer "):
        return False, "Malformed Authorization header"
    token = authorization_header[len("Bearer ") :]
    if not token or token.strip() != token:
        return False, "Malformed Authorization header"
    return True, token


def _protected_path_matches(request_path: str, protected_path: str) -> bool:
    normalized = "/" + protected_path.strip("/")
    stripped = "/" + request_path.strip("/")
    return stripped == normalized or stripped.startswith(f"{normalized}/")


class McpBearerAuthMiddleware:
    """Protect MCP HTTP routes with a static bearer token."""

    def __init__(self, app: Any, *, api_key: str, protected_paths: tuple[str, ...]):
        self.app = app
        self.api_key = api_key
        self.protected_paths = protected_paths

    async def __call__(self, scope: Any, receive: Any, send: Any) -> None:
        request_path = str(scope.get("path") or "")
        protected = any(
            _protected_path_matches(request_path, protected_path)
            for protected_path in self.protected_paths
        )
        if scope.get("type") != "http" or not protected:
            await self.app(scope, receive, send)
            return

        authorization_header: str | None = None
        for key, value in scope.get("headers", []):
            if key.decode("latin1").lower() == "authorization":
                authorization_header = value.decode("latin1")
                break

        ok, token_or_message = _extract_bearer_token(authorization_header)
        if not ok or not secrets.compare_digest(token_or_message, self.api_key or ""):
            from starlette.responses import JSONResponse

            message = token_or_message if not ok else "Invalid bearer token"
            response = JSONResponse(
                _authorization_error_payload(message),
                status_code=401,
                headers={"WWW-Authenticate": "Bearer"},
            )
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)


def _health_payload(config: HttpMcpConfig) -> dict[str, Any]:
    store = IndexStore(config.index_dir)
    payload: dict[str, Any] = {
        "status": "ok",
        "server": SERVER_NAME,
        "version": __version__,
        "read_only": True,
        "tool_mode": config.tool_mode,
        "tool_count": len(list_http_tool_names(config.tool_mode)),
        "index_present": store.exists(),
    }
    try:
        stats = index_stats(index_dir=config.index_dir)
    except Exception:
        payload["status"] = "degraded"
        payload["chunk_count"] = None
        payload["source_count"] = None
    else:
        payload["chunk_count"] = stats.get("chunk_count", 0)
        payload["source_count"] = stats.get("source_count", 0)
    return payload


def _ready_payload(config: HttpMcpConfig) -> tuple[dict[str, Any], int]:
    payload = {
        "status": "ready",
        "server": SERVER_NAME,
        "read_only": True,
        "tool_mode": config.tool_mode,
        "index_present": IndexStore(config.index_dir).exists(),
    }
    if not payload["index_present"]:
        payload["status"] = "not_ready"
        return payload, 503
    return payload, 200


def _log_tool_call(tool_name: str, started_at: float, payload: dict[str, Any]) -> None:
    result_count = None
    if isinstance(payload.get("results"), list):
        result_count = len(payload["results"])
    status = "error" if payload.get("error") else "ok"
    latency_ms = int((time.monotonic() - started_at) * 1000)
    logger.info(
        "tool=%s status=%s latency_ms=%s result_count=%s",
        tool_name,
        status,
        latency_ms,
        result_count,
    )


def _register_chatgpt_tools(mcp: Any, config: HttpMcpConfig, annotations: Any) -> None:
    search_output_schema = {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "title": {"type": "string"},
                        "url": {"type": "string"},
                    },
                    "required": ["id", "title", "url"],
                    "additionalProperties": False,
                },
            },
            "error": {"type": "object"},
        },
        "required": ["results"],
        "additionalProperties": True,
    }
    fetch_output_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "title": {"type": "string"},
            "text": {"type": "string"},
            "url": {"type": "string"},
            "metadata": {"type": "object"},
            "error": {"type": "object"},
        },
        "required": ["id", "title", "text", "url", "metadata"],
        "additionalProperties": True,
    }

    @mcp.tool(output_schema=search_output_schema, annotations=annotations)
    def search(query: str) -> Any:
        """Search Xia's math_rag mathematical research corpus for corpus-supported evidence."""

        started = time.monotonic()
        payload = search_payload(query, config)
        _log_tool_call("search", started, payload)
        return _tool_result(payload)

    @mcp.tool(output_schema=fetch_output_schema, annotations=annotations)
    def fetch(id: str) -> Any:
        """Fetch the full corpus evidence text for a result returned by search."""

        started = time.monotonic()
        payload = fetch_payload(id, config)
        _log_tool_call("fetch", started, payload)
        return _tool_result(payload)


def _register_internal_tools(mcp: Any, config: HttpMcpConfig, annotations: Any) -> None:
    @mcp.tool(annotations=annotations)
    def rag_search(query: str, top_k: int = 8, source_filter: list[str] | None = None) -> Any:
        """Search the indexed mathematical corpus and return richer read-only evidence metadata."""

        started = time.monotonic()
        payload = _service_payload(
            lambda: search_corpus(
                query,
                top_k=_bounded_top_k(top_k, config),
                source_filter=_normalize_source_filter(source_filter),
                index_dir=config.index_dir,
            ),
            fallback={"query": query, "results": []},
        )
        _log_tool_call("rag_search", started, payload)
        return _tool_result(payload)

    @mcp.tool(annotations=annotations)
    def rag_get_chunk(chunk_id: str) -> Any:
        """Return one indexed chunk as untrusted evidence for human inspection."""

        started = time.monotonic()
        payload = _service_payload(
            lambda: get_chunk(chunk_id, index_dir=config.index_dir),
            fallback={"chunk_id": chunk_id},
        )
        if "content" in payload:
            text, truncated, original_char_count = _truncate_text(
                str(payload.get("content") or ""),
                config.fetch_max_chars,
            )
            payload["content"] = text
            payload["content_truncated"] = bool(payload.get("content_truncated", False)) or truncated
            payload["original_char_count"] = original_char_count
        _log_tool_call("rag_get_chunk", started, payload)
        return _tool_result(payload)

    @mcp.tool(annotations=annotations)
    def rag_list_sources(source_filter: list[str] | None = None) -> Any:
        """List indexed sources without exposing write or filesystem operations."""

        started = time.monotonic()
        payload = _service_payload(
            lambda: list_sources(
                source_filter=_normalize_source_filter(source_filter),
                index_dir=config.index_dir,
            ),
            fallback={"sources": []},
        )
        _log_tool_call("rag_list_sources", started, payload)
        return _tool_result(payload)

    @mcp.tool(annotations=annotations)
    def rag_stats() -> Any:
        """Return sanitized index statistics without private source content."""

        started = time.monotonic()
        payload = _service_payload(
            lambda: {**index_stats(index_dir=config.index_dir), "read_only": True},
            fallback={},
        )
        _log_tool_call("rag_stats", started, payload)
        return _tool_result(payload)

    @mcp.tool(annotations=annotations)
    def rag_ask(
        question: str,
        top_k: int = 8,
        strict: bool = True,
        source_filter: list[str] | None = None,
    ) -> Any:
        """Answer only from retrieved evidence and never claim proof verification."""

        started = time.monotonic()
        payload = _service_payload(
            lambda: ask_corpus(
                question,
                top_k=_bounded_top_k(top_k, config),
                strict=strict,
                source_filter=_normalize_source_filter(source_filter),
                index_dir=config.index_dir,
            ),
            fallback={"question": question, "retrieved_evidence": []},
        )
        _log_tool_call("rag_ask", started, payload)
        return _tool_result(payload)


def create_mcp_server(config: HttpMcpConfig | None = None) -> Any:
    """Create a FastMCP server exposing read-only tools for the selected mode."""

    config = config or resolve_http_config()
    try:
        from fastmcp import FastMCP
        from mcp.types import ToolAnnotations
    except ImportError as exc:  # pragma: no cover - optional dependency path
        raise RuntimeError(
            "Remote MCP serving requires the optional dependency group: "
            "pip install -e '.[remote-mcp]'"
        ) from exc

    annotations = ToolAnnotations(
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
        openWorldHint=False,
    )
    mcp = FastMCP(name=f"{SERVER_NAME}-{__version__}")
    if config.tool_mode in {CHATGPT_TOOL_MODE, ALL_TOOL_MODE}:
        _register_chatgpt_tools(mcp, config, annotations)
    if config.tool_mode in {INTERNAL_TOOL_MODE, ALL_TOOL_MODE}:
        _register_internal_tools(mcp, config, annotations)
    return mcp


def create_http_app(config: HttpMcpConfig | None = None) -> Any:
    """Create the Streamable HTTP MCP app with configured auth."""

    config = config or resolve_http_config()
    mcp = create_mcp_server(config)

    middleware: list[Any] = []
    if config.allowed_origins:
        from starlette.middleware import Middleware
        from starlette.middleware.cors import CORSMiddleware

        middleware.append(
            Middleware(
                CORSMiddleware,
                allow_origins=list(config.allowed_origins),
                allow_methods=["GET", "POST", "OPTIONS"],
                allow_headers=["authorization", "content-type", "mcp-session-id", "accept"],
            )
        )
    if config.auth_mode == "bearer":
        from starlette.middleware import Middleware

        protected_paths = (config.path, HEALTH_PATH, READY_PATH) if config.protect_health else (config.path,)
        middleware.append(
            Middleware(
                McpBearerAuthMiddleware,
                api_key=config.api_key or "",
                protected_paths=protected_paths,
            )
        )

    app = mcp.http_app(path=config.path, transport=config.transport, middleware=middleware or None)

    async def healthz(request: Any) -> Any:
        from starlette.responses import JSONResponse

        return JSONResponse(_health_payload(config))

    async def readyz(request: Any) -> Any:
        from starlette.responses import JSONResponse

        payload, status_code = _ready_payload(config)
        return JSONResponse(payload, status_code=status_code)

    from starlette.routing import Route

    app.routes.append(Route(HEALTH_PATH, healthz, methods=["GET"]))
    app.routes.append(Route(READY_PATH, readyz, methods=["GET"]))
    return app


def main() -> None:
    """Run the read-only MCP server over Streamable HTTP."""

    try:
        _configure_logging()
        config = resolve_http_config()
        app = create_http_app(config)
        import uvicorn
    except (HttpMcpConfigError, RuntimeError) as exc:
        sys.stderr.write(f"math_rag HTTP MCP server: {exc}\n")
        raise SystemExit(2) from exc

    uvicorn.run(app, host=config.host, port=config.port)


if __name__ == "__main__":  # pragma: no cover - exercised by deployment
    main()
