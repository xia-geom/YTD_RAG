# Agent Log: Extended Verification Scope

Date: 2026-05-13
Agent: Codex
Branch: `release/remote-mcp-extended-verification`
Commit: none; working tree HEAD was `e76d995`

## Chosen Path

`PUBLIC-SAFE`

This sprint targets extended verification for the low-cost public/semi-public
connector path. The real private research index is forbidden for this sprint
because the user has not explicitly approved exposing it and direct Container
App ingress remains public.

## Scope Guard

Allowed edits:

- deployment documentation
- Azure readiness documentation
- remote MCP documentation
- agent logs

Forbidden edits:

- retrieval, ranking, chunking, ingestion, downloader logic
- corpus files
- `.math_rag_index/index.json`
- eval files
- local stdio MCP behavior
- candidate/gold mathematical evaluation files

Azure changes allowed:

- verification and inspection only by default
- no deletion
- no private endpoints, VNets, premium SKUs, or cost-increasing resources
- no real-index deployment

Azure changes already present before this scope log:

- APIM `/mcp` was switched to the low-cost no-auth façade strategy in the prior
  step, while keeping backend bearer injection.

## Dirty File Classification

CONNECTOR / DEPLOYMENT:

- `.dockerignore`
- `deploy/azure/Dockerfile`
- `deploy/azure/azure-container-apps.sample.bicep`
- `deploy/azure/env.example`
- `deploy/azure/local_remote_mcp_smoke_test.py`
- `deploy/azure/test_corpus/sample_note.md`
- `deploy/azure/test_corpus/sample_paper.tex`
- `math_rag/src/math_rag/mcp_http_server.py`
- `math_rag/tests/test_mcp_http_server.py`
- `math_rag/pyproject.toml`
- `math_rag/.env.example`

DOCS:

- `README.md`
- `deploy/azure/README.md`
- `docs/azure_remote_mcp_readiness.md`
- `docs/remote_mcp_server.md`
- `docs/roadmap.md`

AGENT_LOGS:

- `agent_logs/codex/2026-05-12-remote-mcp-apim-entra-fixture-pilot.md`
- `agent_logs/codex/2026-05-12-remote-mcp-apim-pilot-multiagent.md`
- `agent_logs/codex/2026-05-12-remote-mcp-chatgpt-connector-multiagent.md`
- `agent_logs/codex/2026-05-12-remote-mcp-multiagent-plan.md`
- `agent_logs/codex/2026-05-12-low-cost-public-mcp.md`
- `agent_logs/codex/2026-05-12-remote-mcp-direct-ingress-hardening.md`
- older untracked 2026-05 logs
- this scope log

RETRIEVAL_RANKING_UNRELATED:

- `math_rag/src/math_rag/hybrid_search.py`
- `math_rag/src/math_rag/keyword_search.py`
- `math_rag/src/math_rag/vector_search.py`
- `math_rag/src/math_rag/query_expansion.py`
- `math_rag/tests/test_hybrid_search.py`

LEGACY_ADAPTER / REVIEW_SEPARATELY:

- `math_rag/src/math_rag/remote_mcp_server.py`
- `math_rag/tests/test_remote_mcp_server.py`

TEMP_DO_NOT_STAGE:

- `.tmp-azure-deploy/`
- `.tmp-azure-test-index/`
- `.tmp-docker-test-index-auth/`

CORPUS_OR_INDEX_DO_NOT_TOUCH:

- `corpus/`
- `.math_rag_index/`

EVAL_DO_NOT_TOUCH:

- `eval/`

## Staging State

There were already staged deployment/connector/doc files from prior work. This
verification sprint did not stage or commit anything.

Retrieval/ranking files are dirty but out of scope. `corpus/`, `.math_rag_index`,
and `eval/` showed no diff in the explicit check.

## Real-Index Gate

`PRIVATE_REAL_INDEX_GO=false`

Reason: direct Container App ingress remains public and no equivalent private
backend control was verified.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
