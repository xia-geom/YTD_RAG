"""Tests for the math_rag MCP stdio server and the shared service layer."""

from __future__ import annotations

import io
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from math_rag import mcp_server, rag_service
from math_rag.index_store import IndexStore
from math_rag.models import Chunk


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def sample_chunks() -> list[Chunk]:
    return [
        Chunk(
            chunk_id="chunk-1",
            source_path="corpus/notes_chen_cheng.tex",
            title="Chen-Cheng notes",
            chunk_type="theorem",
            section_path=["Estimates"],
            page_number=3,
            line_start=10,
            line_end=20,
            content=(
                "These notes discuss Chen-Cheng a priori estimates for cscK metrics "
                "on toric Fano manifolds. The argument relies on weighted Mabuchi "
                "energy convexity and Berman-Darvas-Lu uniqueness."
            ),
            metadata={"source_format": "tex"},
            symbols=["Chen-Cheng", "Mabuchi"],
            topics=["cscK", "toric"],
        ),
        Chunk(
            chunk_id="chunk-2",
            source_path="corpus/poincare_cusp.tex",
            title="Poincaré cusp limits",
            chunk_type="proposition",
            section_path=["Cusp limits"],
            page_number=7,
            line_start=42,
            line_end=58,
            content=(
                "The Poincaré-type cscK metrics arise as cusp limits of conic Kahler "
                "metrics. Lahdili and Apostolov-Auvray-Sektnan studied related "
                "weighted variants."
            ),
            metadata={"source_format": "tex"},
            symbols=["Poincaré", "cscK"],
            topics=["cscK", "conic"],
        ),
        Chunk(
            chunk_id="chunk-3",
            source_path="corpus/unrelated.md",
            title="Unrelated note",
            chunk_type="text",
            section_path=[],
            line_start=1,
            line_end=4,
            content="A short generic note about scheduling that has no math content.",
            metadata={"source_format": "md"},
            symbols=[],
            topics=[],
        ),
    ]


@pytest.fixture
def populated_index(tmp_path, sample_chunks):
    index_dir = tmp_path / ".math_rag_index"
    IndexStore(index_dir).save_chunks(sample_chunks)
    return str(index_dir)


@pytest.fixture
def empty_index(tmp_path):
    index_dir = tmp_path / "empty_index"
    index_dir.mkdir()
    return str(index_dir)


# ---------------------------------------------------------------------------
# Service-layer tests (the layer the MCP server exposes)
# ---------------------------------------------------------------------------


def test_search_corpus_returns_expected_schema(populated_index):
    payload = rag_service.search_corpus("Chen-Cheng cscK", top_k=3, index_dir=populated_index)

    assert payload["query"] == "Chen-Cheng cscK"
    assert payload["top_k"] == 3
    assert isinstance(payload["results"], list)
    assert payload["results"], "expected at least one match"
    first = payload["results"][0]
    expected_keys = {
        "chunk_id",
        "source_path",
        "title",
        "chunk_type",
        "section_path",
        "page_number",
        "line_start",
        "line_end",
        "score",
        "snippet",
    }
    assert expected_keys.issubset(first.keys())
    assert first["chunk_id"] == "chunk-1"
    assert "Chen-Cheng" in first["snippet"]


def test_search_corpus_source_filter(populated_index):
    payload = rag_service.search_corpus(
        "Mabuchi", top_k=5, source_filter=["poincare"], index_dir=populated_index
    )
    assert all("poincare" in r["source_path"] for r in payload["results"])


def test_ask_corpus_preserves_evidence_inference_separation(populated_index):
    payload = rag_service.ask_corpus(
        "What does the corpus say about Chen-Cheng estimates?",
        top_k=3,
        index_dir=populated_index,
    )
    for key in (
        "question",
        "short_answer",
        "retrieved_evidence",
        "what_corpus_supports",
        "reasonable_inference",
        "not_established_by_retrieved_sources",
        "sources_inspected",
    ):
        assert key in payload, f"missing field: {key}"
    assert payload["retrieval_confidence"] in {"low", "usable"}
    assert isinstance(payload["retrieved_evidence"], list)
    assert isinstance(payload["what_corpus_supports"], list)
    assert isinstance(payload["reasonable_inference"], list)
    assert isinstance(payload["not_established_by_retrieved_sources"], list)
    joined = " ".join(payload["not_established_by_retrieved_sources"]).lower()
    assert "proof" in joined  # never claims to verify a proof
    assert payload["warning"].startswith("math_rag never verifies a proof")


def test_ask_corpus_low_confidence_for_irrelevant_question(populated_index):
    payload = rag_service.ask_corpus(
        "Prove the Riemann hypothesis using cohomology of motives.",
        top_k=3,
        index_dir=populated_index,
    )
    assert payload["retrieval_confidence"] == "low"
    assert "do not find enough evidence" in payload["short_answer"]


def test_get_chunk_returns_full_content(populated_index):
    payload = rag_service.get_chunk("chunk-2", index_dir=populated_index)
    assert payload["chunk_id"] == "chunk-2"
    assert payload["source_path"] == "corpus/poincare_cusp.tex"
    assert payload["page_number"] == 7
    assert payload["line_start"] == 42
    assert payload["line_end"] == 58
    assert "Poincaré-type cscK metrics" in payload["content"]
    assert "metadata" in payload


def test_get_chunk_missing_id_raises(populated_index):
    with pytest.raises(KeyError):
        rag_service.get_chunk("nope", index_dir=populated_index)


def test_list_sources_returns_summary(populated_index):
    payload = rag_service.list_sources(index_dir=populated_index)
    assert payload["number_of_chunks"] == 3
    assert payload["number_of_sources"] == 3
    paths = [s["source_path"] for s in payload["sources"]]
    assert "corpus/notes_chen_cheng.tex" in paths


def test_list_sources_filtering(populated_index):
    payload = rag_service.list_sources(source_filter=["poincare"], index_dir=populated_index)
    assert payload["number_of_sources"] == 1
    assert payload["sources"][0]["source_path"].endswith("poincare_cusp.tex")


def test_missing_index_gives_helpful_error(empty_index):
    with pytest.raises(rag_service.IndexNotFoundError) as exc_info:
        rag_service.search_corpus("anything", index_dir=empty_index)
    msg = str(exc_info.value)
    assert "No index found" in msg
    assert "math_rag.cli ingest" in msg


# ---------------------------------------------------------------------------
# MCP server tests (in-process)
# ---------------------------------------------------------------------------


def _request(method: str, params: dict | None = None, request_id: int | None = 1) -> dict:
    body: dict = {"jsonrpc": "2.0", "method": method}
    if request_id is not None:
        body["id"] = request_id
    if params is not None:
        body["params"] = params
    return body


def test_mcp_initialize_advertises_protocol(populated_index, tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    response = mcp_server.handle_request(
        _request("initialize", {"protocolVersion": mcp_server.PROTOCOL_VERSION}),
        index_dir=populated_index,
        root=tmp_path,
    )
    assert response["result"]["protocolVersion"] == mcp_server.PROTOCOL_VERSION
    assert response["result"]["serverInfo"]["name"] == mcp_server.SERVER_NAME


def test_mcp_tools_list_read_only_by_default(populated_index, tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    response = mcp_server.handle_request(
        _request("tools/list"), index_dir=populated_index, root=tmp_path
    )
    names = [tool["name"] for tool in response["result"]["tools"]]
    assert names == ["rag_search", "rag_ask", "rag_get_chunk", "rag_list_sources"]
    assert "rag_ingest" not in names


def test_mcp_tools_list_includes_write_tools_when_flag_set(populated_index, tmp_path, monkeypatch):
    monkeypatch.setenv(mcp_server.WRITE_TOOLS_ENV_FLAG, "true")
    response = mcp_server.handle_request(
        _request("tools/list"), index_dir=populated_index, root=tmp_path
    )
    names = [tool["name"] for tool in response["result"]["tools"]]
    assert "rag_ingest" in names


def test_mcp_rag_search_returns_text_content_with_metadata(populated_index, tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    response = mcp_server.handle_request(
        _request(
            "tools/call",
            {"name": "rag_search", "arguments": {"query": "Chen-Cheng", "top_k": 2}},
        ),
        index_dir=populated_index,
        root=tmp_path,
    )
    result = response["result"]
    assert result.get("isError") is not True
    text = result["content"][0]["text"]
    payload = json.loads(text)
    assert payload["query"] == "Chen-Cheng"
    first = payload["results"][0]
    # provenance is preserved in every result
    for key in ("source_path", "page_number", "line_start", "line_end", "chunk_type"):
        assert key in first


def test_mcp_rag_ask_keeps_conservative_fields(populated_index, tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    response = mcp_server.handle_request(
        _request(
            "tools/call",
            {"name": "rag_ask", "arguments": {"question": "Chen-Cheng cscK", "top_k": 2}},
        ),
        index_dir=populated_index,
        root=tmp_path,
    )
    payload = json.loads(response["result"]["content"][0]["text"])
    assert "retrieved_evidence" in payload
    assert "not_established_by_retrieved_sources" in payload
    assert "reasonable_inference" in payload


def test_mcp_rag_get_chunk_returns_full_content(populated_index, tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    response = mcp_server.handle_request(
        _request("tools/call", {"name": "rag_get_chunk", "arguments": {"chunk_id": "chunk-1"}}),
        index_dir=populated_index,
        root=tmp_path,
    )
    payload = json.loads(response["result"]["content"][0]["text"])
    assert payload["chunk_id"] == "chunk-1"
    assert "Chen-Cheng" in payload["content"]


def test_mcp_rag_list_sources(populated_index, tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    response = mcp_server.handle_request(
        _request("tools/call", {"name": "rag_list_sources", "arguments": {}}),
        index_dir=populated_index,
        root=tmp_path,
    )
    payload = json.loads(response["result"]["content"][0]["text"])
    assert payload["number_of_sources"] == 3
    assert payload["number_of_chunks"] == 3


def test_mcp_write_tool_disabled_by_default(populated_index, tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)
    response = mcp_server.handle_request(
        _request("tools/call", {"name": "rag_ingest", "arguments": {"path": "corpus/"}}),
        index_dir=populated_index,
        root=tmp_path,
    )
    result = response["result"]
    assert result["isError"] is True
    assert "disabled" in result["content"][0]["text"].lower()


def test_mcp_unknown_tool_returns_error(populated_index, tmp_path):
    response = mcp_server.handle_request(
        _request("tools/call", {"name": "rag_evil_shell", "arguments": {}}),
        index_dir=populated_index,
        root=tmp_path,
    )
    assert "error" in response


def test_mcp_missing_index_error_is_helpful(empty_index, tmp_path):
    response = mcp_server.handle_request(
        _request("tools/call", {"name": "rag_search", "arguments": {"query": "anything"}}),
        index_dir=empty_index,
        root=tmp_path,
    )
    text = response["result"]["content"][0]["text"]
    assert response["result"]["isError"] is True
    assert "No index found" in text


def test_mcp_response_size_is_capped(populated_index, tmp_path, monkeypatch):
    monkeypatch.setattr(mcp_server, "MAX_RESPONSE_BYTES", 512)
    response = mcp_server.handle_request(
        _request(
            "tools/call",
            {"name": "rag_search", "arguments": {"query": "Chen-Cheng cscK Mabuchi", "top_k": 5}},
        ),
        index_dir=populated_index,
        root=tmp_path,
    )
    text = response["result"]["content"][0]["text"]
    assert len(text.encode("utf-8")) <= 768
    assert "truncated" in text.lower()


def test_mcp_notifications_are_dropped(populated_index, tmp_path):
    response = mcp_server.handle_request(
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        index_dir=populated_index,
        root=tmp_path,
    )
    assert response is None


def test_mcp_ingest_rejects_path_traversal(populated_index, tmp_path, monkeypatch):
    monkeypatch.setenv(mcp_server.WRITE_TOOLS_ENV_FLAG, "true")
    response = mcp_server.handle_request(
        _request("tools/call", {"name": "rag_ingest", "arguments": {"path": "../../etc"}}),
        index_dir=populated_index,
        root=tmp_path,
    )
    result = response["result"]
    assert result["isError"] is True
    assert "outside the workspace root" in result["content"][0]["text"]


def test_mcp_ingest_rejects_absolute_path(populated_index, tmp_path, monkeypatch):
    monkeypatch.setenv(mcp_server.WRITE_TOOLS_ENV_FLAG, "true")
    response = mcp_server.handle_request(
        _request("tools/call", {"name": "rag_ingest", "arguments": {"path": "/etc/passwd"}}),
        index_dir=populated_index,
        root=tmp_path,
    )
    result = response["result"]
    assert result["isError"] is True
    assert "absolute path" in result["content"][0]["text"].lower()


def test_mcp_serve_stdio_handles_malformed_json(populated_index, tmp_path, monkeypatch):
    monkeypatch.setenv(mcp_server.ROOT_ENV_VAR, str(tmp_path))
    monkeypatch.setenv(mcp_server.INDEX_DIR_ENV_VAR, populated_index)
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)

    stdin = io.StringIO("not-json\n")
    stdout = io.StringIO()
    stderr = io.StringIO()
    rc = mcp_server.serve_stdio(stdin=stdin, stdout=stdout, stderr=stderr)
    assert rc == 0
    line = stdout.getvalue().strip().splitlines()[0]
    response = json.loads(line)
    assert response["error"]["code"] == -32700


def test_mcp_serve_stdio_drops_notifications(populated_index, tmp_path, monkeypatch):
    monkeypatch.setenv(mcp_server.ROOT_ENV_VAR, str(tmp_path))
    monkeypatch.setenv(mcp_server.INDEX_DIR_ENV_VAR, populated_index)
    monkeypatch.delenv(mcp_server.WRITE_TOOLS_ENV_FLAG, raising=False)

    stdin = io.StringIO(
        json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n"
    )
    stdout = io.StringIO()
    stderr = io.StringIO()
    rc = mcp_server.serve_stdio(stdin=stdin, stdout=stdout, stderr=stderr)
    assert rc == 0
    assert stdout.getvalue().strip() == ""


def test_resolve_project_root_uses_env_var(tmp_path, monkeypatch):
    monkeypatch.setenv(mcp_server.WORKSPACE_ROOT_ENV_VAR, str(tmp_path))
    monkeypatch.setenv(mcp_server.PACKAGE_ROOT_ENV_VAR, str(PROJECT_ROOT))
    assert mcp_server.resolve_project_root() == tmp_path.resolve()


def test_resolve_roots_supports_separated_workspace_and_package_roots(tmp_path, monkeypatch):
    workspace_root = tmp_path / "workspace"
    package_root = workspace_root / "math_rag"
    (package_root / "src" / "math_rag").mkdir(parents=True)
    (workspace_root / "corpus").mkdir()
    (workspace_root / "eval").mkdir()
    (package_root / "pyproject.toml").write_text("[project]\nname='math-rag'\n", encoding="utf-8")

    monkeypatch.setenv(mcp_server.PACKAGE_ROOT_ENV_VAR, str(package_root))
    monkeypatch.setenv(mcp_server.WORKSPACE_ROOT_ENV_VAR, str(workspace_root))
    monkeypatch.delenv(mcp_server.ROOT_ENV_VAR, raising=False)

    roots = mcp_server.resolve_roots()

    assert roots.package_root == package_root.resolve()
    assert roots.workspace_root == workspace_root.resolve()
    assert mcp_server._resolve_index_dir(roots.workspace_root) == str(workspace_root / ".math_rag_index")


def test_legacy_mcp_root_at_package_root_uses_parent_workspace(tmp_path, monkeypatch):
    workspace_root = tmp_path / "workspace"
    package_root = workspace_root / "math_rag"
    (package_root / "src" / "math_rag").mkdir(parents=True)
    (workspace_root / "corpus").mkdir()
    (package_root / "pyproject.toml").write_text("[project]\nname='math-rag'\n", encoding="utf-8")

    monkeypatch.setenv(mcp_server.ROOT_ENV_VAR, str(package_root))
    monkeypatch.delenv(mcp_server.PACKAGE_ROOT_ENV_VAR, raising=False)
    monkeypatch.delenv(mcp_server.WORKSPACE_ROOT_ENV_VAR, raising=False)

    roots = mcp_server.resolve_roots()

    assert roots.package_root == package_root.resolve()
    assert roots.workspace_root == workspace_root.resolve()


def test_resolve_project_root_errors_when_missing(tmp_path, monkeypatch):
    monkeypatch.delenv(mcp_server.ROOT_ENV_VAR, raising=False)
    monkeypatch.delenv(mcp_server.PACKAGE_ROOT_ENV_VAR, raising=False)
    monkeypatch.delenv(mcp_server.WORKSPACE_ROOT_ENV_VAR, raising=False)
    monkeypatch.setattr(mcp_server, "_module_package_root", lambda: tmp_path / "missing-package")
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError) as exc_info:
        mcp_server.resolve_project_root()
    assert mcp_server.PACKAGE_ROOT_ENV_VAR in str(exc_info.value)


# ---------------------------------------------------------------------------
# End-to-end stdio test: launches the server and exchanges JSON-RPC messages.
# ---------------------------------------------------------------------------


def test_mcp_server_starts_via_stdio(populated_index, monkeypatch):
    env = os.environ.copy()
    env["MATH_RAG_PACKAGE_ROOT"] = str(PROJECT_ROOT)
    env["MATH_RAG_WORKSPACE_ROOT"] = str(PROJECT_ROOT)
    env["MATH_RAG_INDEX_DIR"] = populated_index
    env["PYTHONPATH"] = str(PROJECT_ROOT / "src")
    env.pop("MATH_RAG_ROOT", None)
    env.pop("MATH_RAG_MCP_ALLOW_WRITE_TOOLS", None)

    proc = subprocess.Popen(
        [sys.executable, "-m", "math_rag.mcp_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        bufsize=1,
    )
    try:
        request_lines = (
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "initialize",
                    "params": {"protocolVersion": mcp_server.PROTOCOL_VERSION},
                }
            )
            + "\n"
            + json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
            + "\n"
        )
        stdout, stderr = proc.communicate(input=request_lines, timeout=15)
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.wait(timeout=5)

    lines = [line for line in stdout.splitlines() if line.strip()]
    assert len(lines) >= 2, f"expected at least two JSON-RPC responses; got {lines!r}\nstderr={stderr}"
    init_response = json.loads(lines[0])
    list_response = json.loads(lines[1])
    assert init_response["result"]["serverInfo"]["name"] == mcp_server.SERVER_NAME
    names = [tool["name"] for tool in list_response["result"]["tools"]]
    assert "rag_search" in names
    assert "rag_ingest" not in names  # write tools disabled by default
