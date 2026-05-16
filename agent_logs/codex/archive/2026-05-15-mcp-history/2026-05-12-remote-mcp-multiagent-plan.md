# Agent Log: Remote MCP Multi-Agent Plan

Date: 2026-05-12
Agent: Codex Orchestrator
Branch: master; attempted `codex/remote-mcp-chatgpt-connector`, but Git could not create the slash-prefixed ref in this worktree.
Commit: Not committed
Related files:

- `math_rag/src/math_rag/rag_service.py`
- `math_rag/src/math_rag/mcp_server.py`
- `math_rag/src/math_rag/mcp_http_server.py`
- `math_rag/src/math_rag/remote_mcp_server.py`
- `math_rag/tests/test_mcp_http_server.py`
- `deploy/azure/`
- `docs/remote_mcp_server.md`

## Status Before

- `rag_service.py` already provides `search_corpus`, `get_chunk`, `list_sources`, `index_stats`, and conservative `ask_corpus`.
- `mcp_server.py` is the existing local stdio MCP server and must remain unchanged.
- `mcp_http_server.py` exists from the prior pass, but exposes `rag_*` tools by default.
- `remote_mcp_server.py` contains the older ChatGPT-style `search`/`fetch` adapter.
- The worktree was already dirty with unrelated retrieval/docs changes before this pass.

## Goal of This Task

Make `python -m math_rag.mcp_http_server` the remote read-only MCP server that defaults to ChatGPT-compatible `search` and `fetch`, with optional internal read-only `rag_*` tools selected by `MATH_RAG_TOOL_MODE`.

## Agent Boundaries

Agents may inspect all files, but implementation edits are limited to:

- `math_rag/src/math_rag/mcp_http_server.py`
- `math_rag/tests/test_mcp_http_server.py`
- `deploy/azure/local_remote_mcp_smoke_test.py`
- `deploy/azure/Dockerfile`
- `deploy/azure/env.example`
- `deploy/azure/README.md`
- `deploy/azure/azure-container-apps.sample.bicep`
- `docs/remote_mcp_server.md`
- `docs/azure_remote_mcp_readiness.md`
- `math_rag/.env.example`
- `README.md`
- `agent_logs/codex/*.md`

Do not edit:

- `math_rag/src/math_rag/mcp_server.py`
- retrieval/ranking/chunking/downloader modules
- `corpus/`
- `eval/`
- `.math_rag_index/index.json`
- stable gold/candidate eval files

## Handoff Summary

- Architecture: reuse `rag_service`; keep stable chunk ids; sanitize metadata and local paths; do not encode paths into ids.
- MCP implementation: add `MATH_RAG_TOOL_MODE=chatgpt|internal|all`; default `chatgpt`; keep `/healthz`; keep stdio untouched.
- ChatGPT compatibility: return true `structuredContent`, not `{"result": "<json>"}`; JSON text fallback must equal structured payload.
- Security: keep read-only surface, bearer/no-auth dev modes, localhost defaults, public no-auth guard, result/fetch caps, and no path/secret leakage.
- QA: add tool-mode, auth, output-shape, no-path-leakage, and stdio-regression tests.
- Docs/deploy: update remote docs, Docker/env examples, APIM/Entra guidance, and smoke helper.

## Recommended Next Step

Implement the scoped changes, run full tests, smoke the local HTTP server, and write the final release log.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
