# Agent Log: Remote Streamable HTTP MCP Server

Date: 2026-05-11
Agent: Codex
Branch: master
Commit: Not committed
Related files:

- `math_rag/src/math_rag/mcp_http_server.py`
- `math_rag/tests/test_mcp_http_server.py`
- `math_rag/pyproject.toml`
- `deploy/azure/Dockerfile`
- `deploy/azure/env.example`
- `deploy/azure/local_remote_mcp_smoke_test.py`
- `deploy/azure/README.md`
- `deploy/azure/azure-container-apps.sample.bicep`
- `docs/remote_mcp_server.md`
- `docs/azure_remote_mcp_readiness.md`
- `math_rag/.env.example`
- `.dockerignore`
- `README.md`

## Status Before

The repository already had a local stdio MCP server and a separate legacy remote `search`/`fetch` adapter. The working tree was dirty before this task, including unrelated retrieval and documentation changes.

## Goal of This Task

Add a separate remote read-only MCP server over Streamable HTTP exposing only `rag_*` read tools, with bearer-token authentication, deployment docs/config, tests, and a local smoke path. Do not change retrieval, ranking, chunking, ingestion, eval, corpus data, or the local stdio MCP server behavior.

## Changes Made

### Files Created

- `math_rag/src/math_rag/mcp_http_server.py`
- `math_rag/tests/test_mcp_http_server.py`
- `docs/remote_mcp_server.md`
- `agent_logs/codex/2026-05-11-remote-streamable-http-mcp-server.md`

### Files Modified

- `math_rag/pyproject.toml`: added `math-rag-mcp-http` console script.
- `deploy/azure/Dockerfile`: switched default transport to `streamable-http` and command to `math_rag.mcp_http_server`.
- `deploy/azure/env.example`: added API key/read-only HTTP envs and Streamable HTTP transport default.
- `math_rag/.env.example`: added local HTTP MCP example envs.
- `deploy/azure/local_remote_mcp_smoke_test.py`: updated smoke helper to call `rag_stats`, `rag_search`, and `rag_get_chunk`.
- `deploy/azure/README.md`: updated remote tool surface and auth/deployment notes.
- `deploy/azure/azure-container-apps.sample.bicep`: updated envs for the new HTTP server and API key secret reference.
- `docs/azure_remote_mcp_readiness.md`: updated local/container smoke commands and expected tool names.
- `.dockerignore`: ignored `.tmp-*/` build/smoke directories.
- `README.md`: updated remote MCP summary and bearer-token note.

### Files Removed / Renamed

None.

## Commands Run

- `math_rag/.venv/bin/python -m compileall math_rag/src/math_rag/mcp_http_server.py deploy/azure/local_remote_mcp_smoke_test.py`
- `math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py math_rag/tests/test_remote_mcp_server.py math_rag/tests/test_mcp_server.py`
- `math_rag/.venv/bin/python -m pytest math_rag/tests`
- `math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py`
- Documented local server smoke command:

```bash
MATH_RAG_INDEX_DIR=.math_rag_index \
MATH_RAG_API_KEY=test-secret \
MATH_RAG_REMOTE_MCP_READ_ONLY=true \
MATH_RAG_REMOTE_HOST=127.0.0.1 \
MATH_RAG_REMOTE_PORT=8000 \
MATH_RAG_REMOTE_TRANSPORT=streamable-http \
MATH_RAG_REMOTE_PATH=/mcp/ \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

- Actual fixture-index server smoke command run:

```bash
MATH_RAG_INDEX_DIR=/private/tmp/math-rag-azure-test-index \
MATH_RAG_API_KEY=test-secret \
MATH_RAG_REMOTE_MCP_READ_ONLY=true \
MATH_RAG_REMOTE_HOST=127.0.0.1 \
MATH_RAG_REMOTE_PORT=8000 \
MATH_RAG_REMOTE_TRANSPORT=streamable-http \
MATH_RAG_REMOTE_PATH=/mcp/ \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

- `curl -s -i http://127.0.0.1:8000/healthz`
- `curl -s -i http://127.0.0.1:8000/mcp/ ...` without auth, expecting 401
- `curl -s -i http://127.0.0.1:8000/mcp/ ... initialize`
- `curl -s -i http://127.0.0.1:8000/mcp/ ... notifications/initialized`
- `curl -s -i http://127.0.0.1:8000/mcp/ ... tools/list`
- `curl -s -i http://127.0.0.1:8000/mcp/ ... tools/call rag_search`

The first local server bind attempt failed inside the sandbox with `operation not permitted`; rerunning the same command with approval succeeded. The server process was stopped after the smoke test.

## Test Results

- Compile check: passed.
- Targeted MCP tests: `58 passed in 1.47s`.
- Full package tests: `188 passed in 4.19s`.
- Smoke helper: passed. It built `/private/tmp/math-rag-azure-test-index`, found 2 sources and 4 chunks, listed `rag_ask`, `rag_get_chunk`, `rag_list_sources`, `rag_search`, `rag_stats`, and returned 4 `rag_search` results.
- Local HTTP smoke: passed. `/healthz` returned status ok with no content, unauthenticated `/mcp/` returned 401, authenticated initialize/list/call worked, and `rag_search` returned results.

## Eval Results

Not run. This task did not change retrieval, ranking, chunking, ingestion, candidate eval, or gold eval behavior. The smoke helper ran fixture index stats only.

## Current Status After Task

- Implemented: separate Streamable HTTP `rag_*` MCP server with bearer auth and health endpoint.
- Tested: full pytest suite, focused MCP tests, fixture smoke helper, actual local HTTP server smoke.
- Working: local stdio MCP tests still pass; legacy `remote_mcp_server.py` tests still pass.
- Not implemented: production OAuth/JWT validation inside Python.
- Blocked: none.
- Risk / caveat: app-layer static bearer auth is suitable as a second line of defense; production deployment should still use HTTPS and gateway/OAuth validation.

## Known Limitations / Open Issues

- Docker image build and Azure deployment were not run in this task.
- Health exposes only counts/status, but count visibility should still be acceptable for the deployment context.
- The legacy `search`/`fetch` adapter remains separate for compatibility and is not the new default Docker entrypoint.

## Recommended Next Step

Build the Docker image and run it against the harmless test index behind the intended Azure/API gateway authentication path.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
