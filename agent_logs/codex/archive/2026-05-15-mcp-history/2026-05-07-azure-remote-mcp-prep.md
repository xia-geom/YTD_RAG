# Agent Log: Azure remote read-only MCP preparation

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: not committed at log time
Related files:
- `math_rag/src/math_rag/remote_mcp_server.py`
- `math_rag/tests/test_remote_mcp_server.py`
- `deploy/azure/`
- `.dockerignore`
- `math_rag/pyproject.toml`
- `README.md`
- `math_rag/README.md`

## Goal

Prepare, but do not deploy, a remote read-only MCP server that ChatGPT can connect to as a custom MCP connector.

The existing local stdio MCP server remains unchanged. The remote server is a separate adapter over the existing local index and exposes only ChatGPT-compatible `search` and `fetch` tools.

## Files Created

- `math_rag/src/math_rag/remote_mcp_server.py`
- `math_rag/tests/test_remote_mcp_server.py`
- `.dockerignore`
- `deploy/azure/README.md`
- `deploy/azure/Dockerfile`
- `deploy/azure/env.example`
- `deploy/azure/azure-container-apps.sample.bicep`

## Files Modified

- `math_rag/pyproject.toml`
- `README.md`
- `math_rag/README.md`

## Commands Run

```bash
math_rag/.venv/bin/python -m pytest math_rag/tests/test_remote_mcp_server.py
math_rag/.venv/bin/python -m pytest math_rag/tests
math_rag/.venv/bin/python -m math_rag.cli stats
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
git status --short
```

No Azure resources were created. No `az` commands were run. No corpus, index, or secrets were uploaded.

## Test Results

Focused remote MCP tests:

```text
10 passed
```

Full package test suite:

```text
151 passed
```

## Eval Results

Core source-level eval:

```text
Total questions: 42
Evaluated positive questions: 39
Negative questions: 3
hits@1: 17/39 = 0.436
hits@3: 28/39 = 0.718
hits@5: 31/39 = 0.795
Missing expected sources: none
```

Index stats:

```text
Sources: 80
Chunks: 13870
```

## Important Decisions

- Remote MCP is a separate entrypoint, not a change to `math_rag.mcp_server`.
- Remote tool surface is limited to `search` and `fetch`.
- `rag_ingest`, downloader/discovery tools, shell access, filesystem reads, and write tools are not exposed remotely.
- Remote server refuses startup when `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true` or `MATH_RAG_REMOTE_MCP_READ_ONLY=false`.
- `MATH_RAG_REMOTE_PUBLIC_BASE_URL` is required so returned URLs are stable and do not expose local file paths.
- Deployment prep targets Azure Container Apps, with the index mounted at runtime rather than baked into the image.

## Known Limitations

- OAuth/authentication is documented as required but not implemented inside `math_rag`.
- Azure artifacts are preparation only and need security review before real deployment.
- The remote server serves whatever is present in the mounted `.math_rag_index`; indexed content should be treated as private data.

## Recommended Next Step

Before deployment work, commit the current stable baseline in sensible commits, then do a focused security review of remote MCP authentication options for Azure.

## Raw Notes / Transcript Excerpts

Review found and fixed path-leak risks in remote responses:

- raw `citation` values could leak absolute local paths;
- raw `chunk_metadata` could contain arbitrary path-like strings;
- index-not-found errors could reveal local index paths.

The remote adapter now sanitizes path-like values in response metadata and returns generic missing-index messages.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
