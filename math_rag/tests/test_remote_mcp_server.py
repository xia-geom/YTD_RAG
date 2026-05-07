"""Tests for the remote read-only ChatGPT-compatible MCP adapter."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from math_rag import remote_mcp_server
from math_rag.index_store import IndexStore
from math_rag.models import Chunk


PUBLIC_BASE_URL = "https://rag.example.test"


@pytest.fixture
def remote_chunks() -> list[Chunk]:
    return [
        Chunk(
            chunk_id="chunk-remote-1",
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
                "notes": "Derived from /Users/example/private/YTD_RAG/corpus/private_notes/raw.tex",
                "enrichment": {"source_role": "primary_paper"},
            },
            symbols=["\\omega"],
            topics=["toric", "poincare"],
        ),
        Chunk(
            chunk_id="chunk-remote-2",
            source_path="corpus/my_notes/project_paper_index.md",
            title="Project Paper Index",
            chunk_type="text",
            section_path=["Highest Priority"],
            line_start=1,
            line_end=8,
            content="A navigation note listing exact toric YTD papers.",
            metadata={"source_format": "markdown", "enrichment": {"source_role": "navigation_note"}},
            symbols=[],
            topics=["toric_ytd"],
        ),
    ]


@pytest.fixture
def remote_index(tmp_path: Path, remote_chunks: list[Chunk]) -> str:
    index_dir = tmp_path / ".math_rag_index"
    IndexStore(index_dir).save_chunks(remote_chunks)
    return str(index_dir)


def _payload_from_response(response: dict) -> dict:
    assert set(response) == {"content"}
    assert len(response["content"]) == 1
    item = response["content"][0]
    assert item["type"] == "text"
    return json.loads(item["text"])


def test_remote_search_returns_one_text_item_with_results(remote_index: str):
    response = remote_mcp_server.search_tool_response(
        "toric Poincare extremal",
        index_dir=remote_index,
        public_base_url=PUBLIC_BASE_URL,
    )

    payload = _payload_from_response(response)
    assert set(payload) == {"results"}
    assert payload["results"]
    first = payload["results"][0]
    assert {"id", "title", "url"}.issubset(first)
    assert first["id"] == "chunk-remote-1"
    assert first["url"] == f"{PUBLIC_BASE_URL}/chunks/chunk-remote-1"
    assert "/Users/" not in first["url"]
    assert first["metadata"]["source_path"].startswith("corpus/")
    assert "/Users/" not in first["metadata"]["citation"]


def test_remote_fetch_returns_one_text_item_with_required_shape(remote_index: str):
    response = remote_mcp_server.fetch_tool_response(
        "chunk-remote-1",
        index_dir=remote_index,
        public_base_url=PUBLIC_BASE_URL,
    )

    payload = _payload_from_response(response)
    assert {"id", "title", "text", "url", "metadata"}.issubset(payload)
    assert payload["id"] == "chunk-remote-1"
    assert "toric Poincare type extremal metrics" in payload["text"]
    assert payload["url"] == f"{PUBLIC_BASE_URL}/chunks/chunk-remote-1"
    assert payload["metadata"]["source_path"].startswith("corpus/")
    assert "/Users/" not in payload["metadata"]["source_path"]
    assert "/Users/" not in payload["metadata"]["chunk_metadata"]["local_path"]
    assert "/Users/" not in payload["metadata"]["chunk_metadata"]["notes"]
    assert payload["metadata"]["chunk_metadata"]["notes"].endswith("corpus/private_notes/raw.tex")
    assert "/Users/" not in payload["metadata"]["citation"]
    assert payload["metadata"]["chunk_metadata"]["enrichment"]["source_role"] == "primary_paper"


def test_remote_fetch_unknown_id_returns_safe_error(remote_index: str):
    response = remote_mcp_server.fetch_tool_response(
        "missing-id",
        index_dir=remote_index,
        public_base_url=PUBLIC_BASE_URL,
    )

    payload = _payload_from_response(response)
    assert payload["id"] == "missing-id"
    assert payload["title"] == "Chunk not found"
    assert payload["text"] == ""
    assert payload["metadata"] == {}
    assert payload["error"]["code"] == "not_found"


def test_remote_search_invalid_query_returns_safe_error(remote_index: str):
    payload = json.loads(
        remote_mcp_server.search_json(
            "",
            index_dir=remote_index,
            public_base_url=PUBLIC_BASE_URL,
        )
    )

    assert payload["results"] == []
    assert payload["error"]["code"] == "invalid_query"


def test_remote_missing_index_error_does_not_leak_local_path():
    payload = json.loads(
        remote_mcp_server.search_json(
            "toric",
            index_dir="/Users/example/private/YTD_RAG/.math_rag_index",
            public_base_url=PUBLIC_BASE_URL,
        )
    )

    assert payload["results"] == []
    assert payload["error"]["code"] == "index_not_found"
    assert "/Users/" not in payload["error"]["message"]


def test_remote_registers_only_search_and_fetch():
    assert remote_mcp_server.list_remote_tool_names() == ("search", "fetch")
    assert "rag_ingest" not in remote_mcp_server.list_remote_tool_names()
    assert "download" not in " ".join(remote_mcp_server.list_remote_tool_names())


def test_remote_config_requires_public_base_url(remote_index: str, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv(remote_mcp_server.REMOTE_PUBLIC_BASE_URL_ENV_VAR, raising=False)
    monkeypatch.delenv(remote_mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)

    with pytest.raises(remote_mcp_server.RemoteMcpConfigError, match="PUBLIC_BASE_URL"):
        remote_mcp_server.resolve_remote_config(index_dir=remote_index)


def test_remote_startup_refuses_write_enabled_configuration(
    remote_index: str, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setenv(remote_mcp_server.WRITE_TOOLS_ENV_FLAG, "true")

    with pytest.raises(remote_mcp_server.RemoteMcpConfigError, match="refuses to start"):
        remote_mcp_server.resolve_remote_config(
            index_dir=remote_index,
            public_base_url=PUBLIC_BASE_URL,
        )


def test_remote_startup_refuses_read_only_false(remote_index: str, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv(remote_mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    monkeypatch.setenv(remote_mcp_server.REMOTE_READ_ONLY_ENV_VAR, "false")

    with pytest.raises(remote_mcp_server.RemoteMcpConfigError, match="read-only only"):
        remote_mcp_server.resolve_remote_config(
            index_dir=remote_index,
            public_base_url=PUBLIC_BASE_URL,
        )


def test_remote_config_accepts_safe_explicit_values(remote_index: str, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv(remote_mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    monkeypatch.setenv(remote_mcp_server.REMOTE_READ_ONLY_ENV_VAR, "true")
    monkeypatch.setenv(remote_mcp_server.REMOTE_PORT_ENV_VAR, "9000")
    monkeypatch.setenv(remote_mcp_server.REMOTE_SEARCH_TOP_K_ENV_VAR, "3")

    config = remote_mcp_server.resolve_remote_config(
        index_dir=remote_index,
        public_base_url=PUBLIC_BASE_URL,
    )

    assert config.index_dir == remote_index
    assert config.public_base_url == PUBLIC_BASE_URL
    assert config.port == 9000
    assert config.search_top_k == 3
