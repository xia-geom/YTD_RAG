# Agent Log: pre-Azure remote MCP readiness

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: 6b773d1
Related files:
- `docs/azure_remote_mcp_readiness.md`
- `deploy/azure/README.md`
- `deploy/azure/test_corpus/sample_note.md`
- `deploy/azure/test_corpus/sample_paper.tex`

## Status Before

Remote MCP code and Azure deployment-prep artifacts already existed. The documented target architecture was Azure API Management in front of Azure Container Apps, with Microsoft Entra ID as the OAuth/JWT issuer. The project did not yet have a single no-secrets readiness checklist or a harmless test corpus for the first Azure pilot.

## Goal of This Task

Prepare the repository so the next Azure task can create resources using a tiny test index, without exposing the private research corpus or real `.math_rag_index`.

## Changes Made

### Files Created

- `docs/azure_remote_mcp_readiness.md`
- `deploy/azure/test_corpus/sample_note.md`
- `deploy/azure/test_corpus/sample_paper.tex`
- `agent_logs/codex/2026-05-07-pre-azure-readiness.md`

### Files Modified

- `deploy/azure/README.md`

### Files Removed / Renamed

- None.

## Commands Run

```bash
git status --short
docker --version
math_rag/.venv/bin/python -m math_rag.cli --help
math_rag/.venv/bin/python -m math_rag.cli ingest --help
math_rag/.venv/bin/python -m math_rag.cli stats --help
math_rag/.venv/bin/python -m pytest math_rag/tests/test_remote_mcp_server.py
math_rag/.venv/bin/python -m pytest math_rag/tests
rm -rf /private/tmp/math-rag-azure-test-index
math_rag/.venv/bin/python -m math_rag.cli ingest deploy/azure/test_corpus --index-dir /private/tmp/math-rag-azure-test-index
math_rag/.venv/bin/python -m math_rag.cli stats --index-dir /private/tmp/math-rag-azure-test-index
jq -r '.chunks[].source_path' /private/tmp/math-rag-azure-test-index/index.json | sort -u
MATH_RAG_INDEX_DIR=/private/tmp/math-rag-azure-test-index math_rag/.venv/bin/python -m math_rag.remote_mcp_server
MATH_RAG_INDEX_DIR=/private/tmp/math-rag-azure-test-index MATH_RAG_REMOTE_PUBLIC_BASE_URL=http://127.0.0.1:8000 MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true math_rag/.venv/bin/python -m math_rag.remote_mcp_server
MATH_RAG_INDEX_DIR=/private/tmp/math-rag-azure-test-index MATH_RAG_REMOTE_MCP_READ_ONLY=true MATH_RAG_REMOTE_PUBLIC_BASE_URL=http://127.0.0.1:8000 MATH_RAG_REMOTE_HOST=127.0.0.1 MATH_RAG_REMOTE_PORT=8000 MATH_RAG_REMOTE_TRANSPORT=http MATH_RAG_REMOTE_PATH=/mcp/ MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false math_rag/.venv/bin/python -m math_rag.remote_mcp_server
```

The final command started the local HTTP server; a FastMCP client then connected to `http://127.0.0.1:8000/mcp/` and called `search` and `fetch`.

## Test Results

- Focused remote MCP tests: `10 passed`.
- Full package tests: `151 passed`.

## Eval Results

Not run / Reason: This task did not change retrieval, ranking, eval logic, or the real corpus index.

## Current Status After Task

- Implemented: A pre-Azure readiness checklist now records the architecture, env vars, resource placeholders, test-index workflow, container commands, auth preflight, and go/no-go criteria.
- Tested: Remote MCP tests passed, full package tests passed, and the tiny test corpus ingested into `/private/tmp/math-rag-azure-test-index`.
- Working: The temporary test index reported 2 sources and 4 chunks, all from `deploy/azure/test_corpus/`. A FastMCP client connected to the local HTTP endpoint at `/mcp/`, listed exactly `fetch,search`, called `search`, called `fetch`, and found no `/Users/` path leakage in the fetch payload.
- Not implemented: Azure resources were not created, and no real index was uploaded.
- Blocked: Docker was not available in the current shell, so local image build/run validation could not be completed here.
- Risk / caveat: API Management compatibility with MCP HTTP transport still needs to be tested during the Azure pilot.

## Known Limitations / Open Issues

- Docker readiness commands are documented but not executable in this environment until Docker is installed or available on `PATH`.
- The real research index remains local-only and should not be exposed until the tiny test-index deployment proves authentication and transport behavior.

## Recommended Next Step

- Make Docker available locally and run the documented container test with `/private/tmp/math-rag-azure-test-index`.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
