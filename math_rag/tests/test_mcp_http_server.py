"""Tests for the remote read-only MCP Streamable HTTP server."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from starlette.testclient import TestClient

from math_rag import mcp_http_server
from math_rag.index_store import IndexStore
from math_rag.models import Chunk


TEST_TOKEN = "test-secret"


@pytest.fixture
def http_chunks() -> list[Chunk]:
    return [
        Chunk(
            chunk_id="chunk-http-1",
            source_path="/Users/example/private/YTD_RAG/corpus/arxiv/1711.08424/source/main.tex",
            title="Extremal Kahler Poincare type metrics on toric varieties",
            chunk_type="theorem",
            section_path=["Existence"],
            line_start=12,
            line_end=30,
            content=(
                "This theorem discusses toric Poincare type extremal metrics "
                "and coercivity of a Mabuchi-type functional."
            ),
            metadata={
                "source_format": "latex",
                "local_path": "/Users/example/private/YTD_RAG/corpus/arxiv/1711.08424/source/main.tex",
                "source_url": "https://example.org/paper",
                "authors": ["Author A"],
                "year": 2024,
            },
            symbols=["\\omega"],
            topics=["toric", "poincare"],
        ),
        Chunk(
            chunk_id="chunk-http-2",
            source_path="corpus/my_notes/project_paper_index.md",
            title="Project Paper Index",
            chunk_type="text",
            section_path=["Highest Priority"],
            line_start=1,
            line_end=8,
            content="A navigation note listing exact toric YTD papers.",
            metadata={"source_format": "markdown", "cache_file": "/tmp/private/cache.json"},
            symbols=[],
            topics=["toric_ytd"],
        ),
    ]


@pytest.fixture
def http_index(tmp_path: Path, http_chunks: list[Chunk]) -> str:
    index_dir = tmp_path / ".math_rag_index"
    IndexStore(index_dir).save_chunks(http_chunks)
    return str(index_dir)


def _config(http_index: str, **overrides):
    values = {
        "index_dir": http_index,
        "api_key": TEST_TOKEN,
        "host": "127.0.0.1",
        "port": 8000,
        "transport": "streamable-http",
        "path": "/mcp",
        "public_base_url": "https://rag.example.test",
        "tool_mode": "chatgpt",
        "search_top_k": 5,
        "max_top_k": 20,
        "fetch_max_chars": 12000,
        "auth_mode": "bearer",
    }
    values.update(overrides)
    return mcp_http_server.HttpMcpConfig(**values)


@pytest.fixture
def chatgpt_client(http_index: str):
    app = mcp_http_server.create_http_app(_config(http_index))
    with TestClient(app) as client:
        yield client


def _http_headers(*, token: str | None = TEST_TOKEN, session_id: str | None = None) -> dict[str, str]:
    headers = {"Accept": "application/json, text/event-stream"}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    if session_id is not None:
        headers["mcp-session-id"] = session_id
    return headers


def _sse_payload(response) -> dict:
    assert response.status_code == 200
    assert "data: " in response.text
    return json.loads(response.text.split("data: ", 1)[1].strip())


def _initialize_session(client: TestClient, *, token: str | None = TEST_TOKEN) -> str:
    response = client.post(
        "/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2025-03-26",
                "capabilities": {},
                "clientInfo": {"name": "pytest", "version": "1.0"},
            },
        },
        headers=_http_headers(token=token),
    )
    _sse_payload(response)
    return response.headers["mcp-session-id"]


def _post_initialized(client: TestClient, session_id: str, *, token: str | None = TEST_TOKEN) -> None:
    response = client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}},
        headers=_http_headers(token=token, session_id=session_id),
    )
    assert response.status_code == 202


def _tools_list(client: TestClient, session_id: str, *, token: str | None = TEST_TOKEN):
    return client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
        headers=_http_headers(token=token, session_id=session_id),
    )


def _call_tool(
    client: TestClient,
    session_id: str,
    *,
    name: str,
    arguments: dict,
    token: str | None = TEST_TOKEN,
):
    return client.post(
        "/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments},
        },
        headers=_http_headers(token=token, session_id=session_id),
    )


def _tool_payload(response) -> dict:
    payload = _sse_payload(response)
    assert "structuredContent" in payload["result"]
    structured = payload["result"]["structuredContent"]
    content = payload["result"]["content"]
    assert len(content) == 1
    assert content[0]["type"] == "text"
    assert json.loads(content[0]["text"]) == structured
    return structured


def test_chatgpt_mode_tools_list_exposes_only_search_fetch(chatgpt_client: TestClient):
    session_id = _initialize_session(chatgpt_client)
    _post_initialized(chatgpt_client, session_id)

    tools_payload = _sse_payload(_tools_list(chatgpt_client, session_id))
    tools = tools_payload["result"]["tools"]
    tool_names = [tool["name"] for tool in tools]

    assert tool_names == ["search", "fetch"]
    assert not any(name.startswith("rag_") for name in tool_names)
    assert "rag_ingest" not in tool_names
    for tool in tools:
        assert tool["inputSchema"]["type"] == "object"
        assert tool["inputSchema"]["additionalProperties"] is False
        assert tool["annotations"]["readOnlyHint"] is True
        assert tool["annotations"]["destructiveHint"] is False

    search_schema = tools[0]["inputSchema"]
    assert search_schema["required"] == ["query"]
    assert set(search_schema["properties"]) == {"query"}
    fetch_schema = tools[1]["inputSchema"]
    assert fetch_schema["required"] == ["id"]
    assert set(fetch_schema["properties"]) == {"id"}


def test_chatgpt_search_returns_structured_results_without_text_leak(chatgpt_client: TestClient):
    session_id = _initialize_session(chatgpt_client)
    _post_initialized(chatgpt_client, session_id)

    payload = _tool_payload(
        _call_tool(
            chatgpt_client,
            session_id,
            name="search",
            arguments={"query": "toric Poincare extremal"},
        )
    )

    assert set(payload) == {"results"}
    assert payload["results"]
    first = payload["results"][0]
    assert set(first) == {"id", "title", "url"}
    assert first["id"] == "chunk-http-1"
    assert first["url"] == "https://arxiv.org/abs/1711.08424"
    payload_text = json.dumps(payload)
    assert "toric Poincare type extremal metrics" not in payload_text
    assert "/Users/" not in payload_text
    assert "corpus/" not in payload_text


def test_chatgpt_fetch_returns_structured_evidence_and_safe_metadata(chatgpt_client: TestClient):
    session_id = _initialize_session(chatgpt_client)
    _post_initialized(chatgpt_client, session_id)

    payload = _tool_payload(
        _call_tool(
            chatgpt_client,
            session_id,
            name="fetch",
            arguments={"id": "chunk-http-1"},
        )
    )

    assert {"id", "title", "text", "url", "metadata"}.issubset(payload)
    assert payload["id"] == "chunk-http-1"
    assert "toric Poincare type extremal metrics" in payload["text"]
    assert payload["url"] == "https://arxiv.org/abs/1711.08424"
    assert payload["metadata"]["chunk_id"] == "chunk-http-1"
    assert payload["metadata"]["source_id"] == "arxiv/1711.08424"
    assert payload["metadata"]["truncated"] is False
    payload_text = json.dumps(payload)
    for forbidden in ("/Users/", "/private/", "/tmp/", "/Volumes/", "local_path", "corpus/"):
        assert forbidden not in payload_text


def test_chatgpt_search_invalid_query_returns_empty_results(chatgpt_client: TestClient):
    session_id = _initialize_session(chatgpt_client)
    _post_initialized(chatgpt_client, session_id)

    payload = _tool_payload(
        _call_tool(chatgpt_client, session_id, name="search", arguments={"query": ""})
    )

    assert payload == {"results": []}


def test_chatgpt_fetch_unknown_id_returns_clean_not_found(chatgpt_client: TestClient):
    session_id = _initialize_session(chatgpt_client)
    _post_initialized(chatgpt_client, session_id)

    payload = _tool_payload(
        _call_tool(chatgpt_client, session_id, name="fetch", arguments={"id": "missing-id"})
    )

    assert payload["id"] == "missing-id"
    assert payload["text"] == ""
    assert payload["metadata"] == {}
    assert payload["error"]["code"] == "not_found"
    assert "/Users/" not in json.dumps(payload)


def test_internal_mode_exposes_only_read_only_rag_tools(http_index: str):
    app = mcp_http_server.create_http_app(_config(http_index, tool_mode="internal"))
    with TestClient(app) as client:
        session_id = _initialize_session(client)
        _post_initialized(client, session_id)
        tools_payload = _sse_payload(_tools_list(client, session_id))

    tool_names = [tool["name"] for tool in tools_payload["result"]["tools"]]
    assert tool_names == list(mcp_http_server.INTERNAL_TOOL_NAMES)
    assert "search" not in tool_names
    assert "fetch" not in tool_names


def test_all_mode_exposes_chatgpt_and_internal_tools(http_index: str):
    app = mcp_http_server.create_http_app(_config(http_index, tool_mode="all"))
    with TestClient(app) as client:
        session_id = _initialize_session(client)
        _post_initialized(client, session_id)
        tools_payload = _sse_payload(_tools_list(client, session_id))

    tool_names = [tool["name"] for tool in tools_payload["result"]["tools"]]
    assert tool_names == list(mcp_http_server.CHATGPT_TOOL_NAMES + mcp_http_server.INTERNAL_TOOL_NAMES)


def test_internal_rag_tools_still_work_and_are_capped(http_index: str):
    app = mcp_http_server.create_http_app(
        _config(http_index, tool_mode="internal", max_top_k=1, fetch_max_chars=20)
    )
    with TestClient(app) as client:
        session_id = _initialize_session(client)
        _post_initialized(client, session_id)
        search_payload = _tool_payload(
            _call_tool(
                client,
                session_id,
                name="rag_search",
                arguments={"query": "toric Poincare extremal", "top_k": 50},
            )
        )
        chunk_payload = _tool_payload(
            _call_tool(
                client,
                session_id,
                name="rag_get_chunk",
                arguments={"chunk_id": "chunk-http-1"},
            )
        )

    assert len(search_payload["results"]) == 1
    assert len(chunk_payload["content"]) <= 36
    assert chunk_payload["content_truncated"] is True


def test_bearer_auth_rejects_missing_wrong_and_malformed_tokens(chatgpt_client: TestClient):
    response = chatgpt_client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
        headers=_http_headers(token=None),
    )
    assert response.status_code == 401
    assert response.headers["www-authenticate"] == "Bearer"

    response = chatgpt_client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
        headers={"Accept": "application/json, text/event-stream", "Authorization": "Token nope"},
    )
    assert response.status_code == 401

    response = chatgpt_client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
        headers=_http_headers(token="wrong"),
    )
    assert response.status_code == 401


def test_no_auth_localhost_mode_allows_dev_access(http_index: str):
    app = mcp_http_server.create_http_app(_config(http_index, api_key=None, auth_mode="none"))
    with TestClient(app) as client:
        session_id = _initialize_session(client, token=None)
        _post_initialized(client, session_id, token=None)
        tools_payload = _sse_payload(_tools_list(client, session_id, token=None))

    assert [tool["name"] for tool in tools_payload["result"]["tools"]] == ["search", "fetch"]


def test_public_no_auth_configuration_refuses_startup(http_index: str, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv(mcp_http_server.HOST_ENV_VAR, "0.0.0.0")
    monkeypatch.setenv(mcp_http_server.AUTH_MODE_ENV_VAR, "none")
    monkeypatch.delenv(mcp_http_server.ALLOW_UNAUTHENTICATED_PUBLIC_ENV_VAR, raising=False)
    monkeypatch.delenv(mcp_http_server.API_TOKEN_ENV_VAR, raising=False)
    monkeypatch.delenv(mcp_http_server.API_KEY_ENV_VAR, raising=False)

    with pytest.raises(mcp_http_server.HttpMcpConfigError, match="Refusing unauthenticated public"):
        mcp_http_server.resolve_http_config(index_dir=http_index)


def test_resolve_config_supports_bearer_token_and_alias_envs(
    http_index: str,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setenv(mcp_http_server.HOST_ENV_VAR, "127.0.0.1")
    monkeypatch.setenv("PORT", "9000")
    monkeypatch.setenv(mcp_http_server.AUTH_MODE_ENV_VAR, "bearer")
    monkeypatch.setenv(mcp_http_server.API_TOKEN_ENV_VAR, TEST_TOKEN)
    monkeypatch.setenv(mcp_http_server.TOOL_MODE_ENV_VAR, "all")
    monkeypatch.setenv(mcp_http_server.SEARCH_TOP_K_ENV_VAR, "3")
    monkeypatch.setenv(mcp_http_server.MAX_TOP_K_ENV_VAR, "4")
    monkeypatch.setenv(mcp_http_server.FETCH_MAX_CHARS_ENV_VAR, "500")
    monkeypatch.setenv(mcp_http_server.PUBLIC_BASE_URL_ENV_VAR, "https://rag.example.test")
    monkeypatch.setenv(mcp_http_server.PROTECT_HEALTH_ENV_VAR, "true")

    config = mcp_http_server.resolve_http_config(index_dir=http_index)

    assert config.port == 9000
    assert config.auth_mode == "bearer"
    assert config.api_key == TEST_TOKEN
    assert config.tool_mode == "all"
    assert config.search_top_k == 3
    assert config.max_top_k == 4
    assert config.fetch_max_chars == 500
    assert config.protect_health is True


def test_config_refuses_write_enabled_environment(http_index: str, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv(mcp_http_server.API_TOKEN_ENV_VAR, TEST_TOKEN)
    monkeypatch.setenv(mcp_http_server.AUTH_MODE_ENV_VAR, "bearer")
    monkeypatch.setenv(mcp_http_server.WRITE_TOOLS_ENV_FLAG, "true")

    with pytest.raises(mcp_http_server.HttpMcpConfigError, match="refuses to start"):
        mcp_http_server.resolve_http_config(index_dir=http_index)


def test_health_and_ready_endpoints_do_not_expose_content(chatgpt_client: TestClient):
    health = chatgpt_client.get("/healthz")
    ready = chatgpt_client.get("/readyz")

    assert health.status_code == 200
    assert ready.status_code == 200
    health_payload = health.json()
    assert health_payload["status"] == "ok"
    assert health_payload["tool_mode"] == "chatgpt"
    assert health_payload["tool_count"] == 2
    for payload in (health_payload, ready.json()):
        payload_text = json.dumps(payload)
        assert "sources" not in payload
        assert "content" not in payload
        assert "/Users/" not in payload_text
        assert "corpus/" not in payload_text


def test_protected_health_and_ready_reject_missing_and_wrong_bearer(http_index: str):
    app = mcp_http_server.create_http_app(_config(http_index, protect_health=True))
    with TestClient(app) as client:
        for path in ("/healthz", "/readyz"):
            missing = client.get(path)
            wrong = client.get(path, headers={"Authorization": "Bearer wrong"})

            assert missing.status_code == 401
            assert wrong.status_code == 401
            assert missing.headers["www-authenticate"] == "Bearer"


def test_protected_health_and_ready_accept_correct_bearer(http_index: str):
    app = mcp_http_server.create_http_app(_config(http_index, protect_health=True))
    with TestClient(app) as client:
        health = client.get("/healthz", headers={"Authorization": f"Bearer {TEST_TOKEN}"})
        ready = client.get("/readyz", headers={"Authorization": f"Bearer {TEST_TOKEN}"})

    assert health.status_code == 200
    assert ready.status_code == 200
    assert health.json()["status"] == "ok"
    assert ready.json()["status"] == "ready"
