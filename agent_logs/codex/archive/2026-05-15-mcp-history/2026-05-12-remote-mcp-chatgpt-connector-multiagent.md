# Agent Log: Remote MCP ChatGPT Connector Multiagent

Date: 2026-05-12
Agent: Codex orchestrator with architecture, implementation, compatibility, security, QA, docs/deployment, and final-review subagents
Branch: master
Commit: none; working tree HEAD was e76d995
Related files:
- `math_rag/src/math_rag/mcp_http_server.py`
- `math_rag/tests/test_mcp_http_server.py`
- `deploy/azure/local_remote_mcp_smoke_test.py`
- `docs/remote_mcp_server.md`
- `deploy/azure/Dockerfile`
- `deploy/azure/env.example`
- `deploy/azure/README.md`
- `deploy/azure/azure-container-apps.sample.bicep`
- `docs/azure_remote_mcp_readiness.md`
- `math_rag/.env.example`
- `math_rag/pyproject.toml`
- `.dockerignore`
- `README.md`

## Status Before

- The repository already had a working local `math_rag.mcp_server` stdio MCP server and `rag_service.py` service layer.
- The working tree was already dirty, including retrieval/ranking-related files and prior deployment/auth work.
- Recent project state indicated 17,718 chunks from 101 sources and a previously passing full test suite.
- Recent logs explicitly said no MCP changes had been made in that pass.

## Goal of This Task

Finish the online read-only MCP server so it can be connected to ChatGPT as a data-only connector, without changing retrieval, ranking, chunking, ingestion, downloader behavior, corpus files, eval files, `.math_rag_index/index.json`, or existing stdio MCP behavior.

## Agents Involved

- Orchestrator / Integration Lead: coordinated scope, implementation, validation, and final log.
- Architecture Agent: reviewed adapter policy, ID/URL strategy, metadata sanitization, and service reuse.
- MCP Server Implementation Agent: reviewed HTTP server entrypoint, tool modes, health endpoint, and startup behavior.
- ChatGPT Compatibility Agent: reviewed `search`/`fetch` structured output and JSON fallback requirements.
- Security / Auth Agent: reviewed auth modes, path leakage, caps, read-only tool surface, and deployment caveats.
- Test / QA Agent: reviewed required test coverage and smoke flows.
- Docs / Deployment Agent: reviewed Docker, Azure, and connector documentation needs.
- Final Review / Release Agent: performed read-only release review and found no blocking issues.

## Changes Made

### Files Created

- `math_rag/src/math_rag/mcp_http_server.py`
  - New separate remote Streamable HTTP MCP entrypoint.
  - Default tool mode is `chatgpt` and exposes only `search` and `fetch`.
  - Internal mode exposes read-only `rag_search`, `rag_get_chunk`, `rag_list_sources`, `rag_stats`, and conservative `rag_ask`.
  - Reuses `rag_service.py`; no retrieval logic is duplicated.
  - Adds `/healthz` and `/readyz`.
  - Adds bearer auth for `/mcp`, localhost no-auth dev mode, public no-auth guard, result caps, fetch text cap, metadata sanitization, and read-only annotations.
- `math_rag/tests/test_mcp_http_server.py`
  - Covers ChatGPT tool exposure, strict schemas, structured content/fallback equivalence, `search`, `fetch`, internal tools, auth, health/readiness, caps, and path-sanitization behavior.
- `deploy/azure/local_remote_mcp_smoke_test.py`
  - Builds an isolated fixture index and smokes ChatGPT `search`/`fetch` plus internal read-only tool mode.
- `docs/remote_mcp_server.md`
  - Documents architecture, tools, environment, local run, curl MCP flow, ChatGPT connection, Docker, security model, and limitations.
- `docs/azure_remote_mcp_readiness.md`
  - Documents Azure readiness around the new HTTP MCP server and ChatGPT `search`/`fetch` mode.
- `agent_logs/codex/2026-05-12-remote-mcp-multiagent-plan.md`
  - Discovery and edit-boundary note for the multi-agent run.
- `agent_logs/codex/2026-05-12-remote-mcp-chatgpt-connector-multiagent.md`
  - This release log.

### Files Modified

- `.dockerignore`
  - Excludes temporary `.tmp-*` build/test directories.
- `README.md`
  - Updates remote MCP summary for ChatGPT `search`/`fetch`, bearer auth, and local no-auth caveat.
- `deploy/azure/Dockerfile`
  - Starts `python -m math_rag.mcp_http_server` with HTTP MCP defaults.
- `deploy/azure/README.md`
  - Updates Azure deployment notes for ChatGPT mode, bearer app-layer auth, APIM/OAuth recommendation, and no direct public bypass.
- `deploy/azure/azure-container-apps.sample.bicep`
  - Adds bearer/token, ChatGPT mode, host/port/path, read-only, and no-unauth-public environment settings.
- `deploy/azure/env.example`
  - Adds current HTTP MCP and ChatGPT connector environment defaults.
- `math_rag/.env.example`
  - Adds local HTTP MCP development defaults and bearer example.
- `math_rag/pyproject.toml`
  - Registers `math-rag-mcp-http = "math_rag.mcp_http_server:main"`.

### Files Intentionally Not Modified

- `math_rag/src/math_rag/mcp_server.py`
- `math_rag/src/math_rag/rag_service.py`
- chunking logic
- ingestion logic
- downloader logic
- corpus files
- stable gold eval files
- candidate eval files
- `.math_rag_index/index.json`

The working tree still contains pre-existing dirty retrieval/ranking-related files (`hybrid_search.py`, `keyword_search.py`, `vector_search.py`) and legacy remote adapter changes (`remote_mcp_server.py`, `test_remote_mcp_server.py`). They were not part of this HTTP MCP connector implementation and should be reviewed separately before staging.

### Files Removed / Renamed

- None.

## Tool Lists Verified

ChatGPT mode:

```text
search
fetch
```

Internal mode:

```text
rag_ask
rag_get_chunk
rag_list_sources
rag_search
rag_stats
```

## Auth Modes Implemented

- `MATH_RAG_AUTH_MODE=none`
  - Local/dev only.
  - Defaults to localhost.
  - Public bind is refused unless `MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=true` is explicitly set.
- `MATH_RAG_AUTH_MODE=bearer`
  - Protects `/mcp`.
  - Requires `MATH_RAG_API_TOKEN`; `MATH_RAG_API_KEY` is accepted as a legacy alias.
  - Rejects missing, malformed, and wrong bearer tokens.
- `MATH_RAG_AUTH_MODE=oauth`
  - Not implemented inside Python.
  - Startup fails with a clear message.
  - Production OAuth/OIDC is documented as a deployment gateway responsibility.

## Commands Run

Discovery and review:

```bash
pwd
git status --short
find . -maxdepth 3 -type f | sort | sed 's#^\./##' | head -200
git checkout -b codex/remote-mcp-chatgpt-connector
git branch --show-current
git rev-parse --short HEAD
git diff --name-only -- math_rag/src/math_rag/chunker.py math_rag/src/math_rag/ingest.py math_rag/src/math_rag/downloader.py math_rag/src/math_rag/mcp_server.py .math_rag_index/index.json eval/candidate_evidence_questions.yaml eval/candidate_source_suggestions.yaml
```

Implementation checks:

```bash
math_rag/.venv/bin/python -m compileall math_rag/src/math_rag/mcp_http_server.py
math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py -q
math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py math_rag/tests/test_remote_mcp_server.py math_rag/tests/test_mcp_server.py -q
math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py
math_rag/.venv/bin/python -m pytest math_rag/tests
math_rag/.venv/bin/python -m math_rag.cli stats
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
```

Local HTTP smoke:

```bash
MATH_RAG_INDEX_DIR=.math_rag_index \
MATH_RAG_AUTH_MODE=none \
MATH_RAG_TOOL_MODE=chatgpt \
MATH_RAG_REMOTE_MCP_READ_ONLY=true \
MATH_RAG_HOST=127.0.0.1 \
PORT=8000 \
MATH_RAG_REMOTE_TRANSPORT=streamable-http \
MATH_RAG_REMOTE_PATH=/mcp \
math_rag/.venv/bin/python -m math_rag.mcp_http_server

curl http://127.0.0.1:8000/healthz
curl http://127.0.0.1:8000/readyz
curl -i -H 'Accept: application/json, text/event-stream' -H 'Content-Type: application/json' --data '<initialize JSON-RPC>' http://127.0.0.1:8000/mcp
curl -i -H 'Accept: application/json, text/event-stream' -H 'Content-Type: application/json' -H 'Mcp-Session-Id: <session-id>' --data '<tools/list JSON-RPC>' http://127.0.0.1:8000/mcp
curl -i -H 'Accept: application/json, text/event-stream' -H 'Content-Type: application/json' -H 'Mcp-Session-Id: <session-id>' --data '<search JSON-RPC>' http://127.0.0.1:8000/mcp
curl -i -H 'Accept: application/json, text/event-stream' -H 'Content-Type: application/json' -H 'Mcp-Session-Id: <session-id>' --data '<fetch JSON-RPC>' http://127.0.0.1:8000/mcp
```

Docker smoke:

```bash
docker build -f deploy/azure/Dockerfile -t math-rag-mcp-http:local .
docker run -d --rm --name math-rag-mcp-http-smoke -p 8001:8000 -e MATH_RAG_INDEX_DIR=/data/.math_rag_index -e MATH_RAG_AUTH_MODE=bearer -e MATH_RAG_API_TOKEN=test-secret -e MATH_RAG_TOOL_MODE=chatgpt -e MATH_RAG_REMOTE_MCP_READ_ONLY=true -e MATH_RAG_HOST=0.0.0.0 -e PORT=8000 -e MATH_RAG_REMOTE_TRANSPORT=streamable-http -e MATH_RAG_REMOTE_PATH=/mcp -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false -v /Users/xiaxiao/Desktop/Projects/YTD_RAG/.tmp-docker-test-index-auth:/data/.math_rag_index:ro math-rag-mcp-http:local
curl http://127.0.0.1:8001/healthz
curl -i -H 'Accept: application/json, text/event-stream' http://127.0.0.1:8001/mcp
curl -i -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' --data '<initialize JSON-RPC>' http://127.0.0.1:8001/mcp
curl -i -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -H 'Mcp-Session-Id: <session-id>' --data '<tools/list JSON-RPC>' http://127.0.0.1:8001/mcp
curl -sS -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -H 'Mcp-Session-Id: <session-id>' --data '<search JSON-RPC>' http://127.0.0.1:8001/mcp
curl -sS -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -H 'Mcp-Session-Id: <session-id>' --data '<fetch JSON-RPC>' http://127.0.0.1:8001/mcp
docker stop math-rag-mcp-http-smoke
```

Cleanup/status checks:

```bash
pgrep -fl math_rag.mcp_http_server
docker ps --filter name=math-rag-mcp-http-smoke --format '{{.ID}} {{.Names}} {{.Status}}'
git status --short
```

## Test Results

- `math_rag/.venv/bin/python -m compileall math_rag/src/math_rag/mcp_http_server.py`: passed.
- `math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py -q`: `14 passed`.
- `math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py math_rag/tests/test_remote_mcp_server.py math_rag/tests/test_mcp_server.py -q`: `64 passed`.
- `math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py`: passed.
- `math_rag/.venv/bin/python -m pytest math_rag/tests`: `194 passed in 4.36s` on the final run.
- Existing stdio MCP tests are included in the full suite and in the targeted MCP run.

## Eval Results

- `math_rag/.venv/bin/python -m math_rag.cli stats`: passed.
  - Index: `.math_rag_index/index.json`
  - Sources: 101
  - Chunks: 17,718
- `math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml`: started but did not complete after several minutes and was interrupted/killed. No eval result is claimed.

## Smoke-Test Results

- In-process fixture smoke passed.
  - ChatGPT tools: `fetch`, `search`
  - Internal tools: `rag_ask`, `rag_get_chunk`, `rag_list_sources`, `rag_search`, `rag_stats`
  - Fixture search returned 4 results.
  - Fixture fetch returned the first result with matching structured content and JSON fallback.
- Local HTTP smoke against the real index passed.
  - `/healthz`: ok, read-only, `tool_mode=chatgpt`, `tool_count=2`, 17,718 chunks, 101 sources.
  - `/readyz`: ready.
  - `initialize`, `notifications/initialized`, `tools/list`, `search`, and `fetch` worked.
  - `tools/list` returned exactly `search` and `fetch`.
  - `search` returned 8 results for `Apostolov Auvray Sektnan Poincare type toric metrics`.
  - `fetch` returned one evidence passage with safe metadata.
- Docker smoke passed.
  - Docker image built.
  - Container health endpoint returned ok on port 8001.
  - Unauthenticated `/mcp` returned 401 with bearer challenge.
  - Authenticated initialize/list/search/fetch worked.
  - Container was stopped after the smoke test.

## Exact Local Startup Command

Local no-auth development command:

```bash
MATH_RAG_INDEX_DIR=.math_rag_index \
MATH_RAG_AUTH_MODE=none \
MATH_RAG_TOOL_MODE=chatgpt \
MATH_RAG_REMOTE_MCP_READ_ONLY=true \
MATH_RAG_HOST=127.0.0.1 \
PORT=8000 \
MATH_RAG_REMOTE_TRANSPORT=streamable-http \
MATH_RAG_REMOTE_PATH=/mcp \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

Bearer-protected local command:

```bash
MATH_RAG_INDEX_DIR=.math_rag_index \
MATH_RAG_AUTH_MODE=bearer \
MATH_RAG_API_TOKEN=test-secret \
MATH_RAG_TOOL_MODE=chatgpt \
MATH_RAG_REMOTE_MCP_READ_ONLY=true \
MATH_RAG_HOST=127.0.0.1 \
PORT=8000 \
MATH_RAG_REMOTE_TRANSPORT=streamable-http \
MATH_RAG_REMOTE_PATH=/mcp \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

## Exact Local MCP Endpoint

```text
http://127.0.0.1:8000/mcp
```

## Deployment Notes

- Docker build from the workspace root works with `deploy/azure/Dockerfile`.
- Mount the built index read-only; do not bake private corpus data or secrets into the image.
- For ChatGPT or public deployment, expose only HTTPS through a gateway.
- Use `MATH_RAG_TOOL_MODE=chatgpt` and allow only `search` and `fetch`.
- Use gateway OAuth/OIDC for production ChatGPT connectors. The Python app does not implement OAuth token verification.
- Keep bearer auth enabled at the app layer as a second line of defense.
- Avoid direct public Container App ingress unless network policy or APIM prevents bypass.

## Current Status After Task

- Implemented:
  - New read-only Streamable HTTP MCP server.
  - ChatGPT-compatible `search` and `fetch` mode.
  - Internal read-only tool mode.
  - Bearer auth, localhost no-auth dev mode, public no-auth guard.
  - Health and readiness endpoints.
  - Sanitized metadata, capped result count, capped fetch text.
  - Docker and Azure deployment skeleton updates.
- Tested:
  - Focused HTTP MCP tests.
  - Targeted MCP tests including stdio tests.
  - Full `math_rag/tests`.
  - Local fixture smoke.
  - Real-index local HTTP smoke.
  - Docker smoke.
- Working:
  - Remote server starts locally.
  - `/mcp` initializes, lists tools, calls `search`, and calls `fetch`.
  - `/healthz` and `/readyz` expose no private corpus content.
- Not implemented:
  - In-app OAuth/JWT resource-server verification.
  - Actual remote cloud deployment.
- Blocked:
  - No current blocker for guarded local/Docker pilot.
- Risk / caveat:
  - Working tree contains unrelated pre-existing dirty retrieval/ranking and legacy remote adapter files.
  - Eval command did not complete, so no eval result is claimed.

## Known Limitations / Open Issues

- OAuth/OIDC is documented as a gateway responsibility, not implemented in Python.
- ChatGPT production connection has not been deployed or verified against a live ChatGPT connector.
- Retrieved passages remain untrusted evidence and must not be treated as instructions or mathematical proof verification.
- `rag_ask` is exposed only outside default ChatGPT mode; it relies on the existing conservative service behavior.
- Temporary fixture directories such as `.tmp-docker-test-index-auth/` must not be staged.

## Recommended Next Step

Deploy a small APIM-fronted Container App pilot using the fixture index first, then switch to the real mounted index only after gateway OAuth and direct-ingress restrictions are verified.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
