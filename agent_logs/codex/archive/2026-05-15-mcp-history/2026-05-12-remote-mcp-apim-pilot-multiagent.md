# Agent Log: Remote MCP APIM Pilot Multiagent

Date: 2026-05-12
Agent: Codex orchestrator with security/auth, MCP compatibility, privacy, docs/deployment, and release hygiene subagents
Branch: release/remote-mcp-apim-pilot
Commit: none; working tree HEAD was e76d995

## Goal

Move the already implemented read-only ChatGPT-compatible MCP server toward a safe APIM/Entra-fronted Azure pilot using the harmless fixture index first. Do not expose the real research index until fixture-index APIM/Entra, direct-ingress, ChatGPT tool-list, search/fetch, and path-leak checks pass.

## Status Before

- `math_rag.mcp_http_server` already existed and local/Docker smoke tests had passed.
- Default ChatGPT mode exposed only `search` and `fetch`.
- Python OAuth/JWT validation was intentionally not implemented.
- A prior harmless Azure Container App pilot existed with app-layer bearer auth, but it was not behind APIM/Entra.
- The working tree was dirty before this sprint, including unrelated retrieval/ranking and legacy adapter changes.

## Agents Involved

- Orchestrator / Release Manager: ran release hygiene, Azure inspection, local/Docker checks, docs edits, staging, and final log.
- Security / Auth / Identity Agent: reviewed APIM/Entra, bearer, direct-ingress, and real-index blockers.
- MCP Protocol / ChatGPT Compatibility Agent: reviewed Streamable HTTP, session headers, tool-list, `search`, and `fetch` shape.
- Data Privacy / Path-Leak Auditor: reviewed forbidden strings, helper output, fixture gating, and real-index blockers.
- Docs / Deployment Agent: reviewed APIM/Entra docs and identified runbook gaps.

## Files Created

- `agent_logs/codex/2026-05-12-remote-mcp-apim-pilot-multiagent.md`

## Files Modified

- `README.md`
  - Added the fixture-first remote deployment gate and real-index block.
- `deploy/azure/README.md`
  - Added APIM/Entra runbook steps and clarified backend bearer-token forwarding/injection.
- `deploy/azure/env.example`
  - Reworded the API token placeholder as a secret-store value.
- `deploy/azure/azure-container-apps.sample.bicep`
  - Strengthened the warning that `external: true` is fixture-only and unsafe for real-index use unless direct bypass is blocked.
- `docs/azure_remote_mcp_readiness.md`
  - Added an operator-oriented APIM/Entra pilot runbook.
  - Replaced local absolute temp path examples with workspace `.tmp-*` paths.
- `docs/remote_mcp_server.md`
  - Reworded the Docker token placeholder to avoid implying committed secrets.
- `deploy/azure/local_remote_mcp_smoke_test.py`
  - Changed the default fixture index path to workspace `.tmp-azure-test-index`.
  - Sanitized the JSON summary so it reports `sample_note.md`, `sample_paper.tex`, and `<fixture-index>` instead of absolute local paths.

## Files Intentionally Not Modified

- Retrieval, ranking, chunking, ingestion, downloader, corpus, eval files, `.math_rag_index/index.json`, and local stdio MCP behavior.
- Real research index deployment was not attempted.
- Azure Container App was not updated.
- APIM/Entra resources were not created.

## Azure Resources Created / Updated

None.

Read-only inspection after Azure login confirmed:

- Subscription: Azure for Students, UQAM tenant.
- Existing resource group `rg-math-rag-mcp-test` contains:
  - Container Apps environment `env-math-rag-mcp-test`
  - ACR `ca3ae23477c8acr`
  - Container App `math-rag-mcp-test`
  - a managed workspace resource
- Existing Container App:
  - FQDN: `math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io`
  - image: `ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot3-amd64`
  - external ingress: `true`
  - status: `Running`
  - legacy envs include `MATH_RAG_API_KEY`, `MATH_RAG_REMOTE_TRANSPORT=http`, and `MATH_RAG_REMOTE_PATH=/mcp/`
- No Azure API Management resources were found by the subscription-wide resource query.

## Commands Run

Release hygiene:

```bash
pwd
git branch --show-current
git rev-parse --short HEAD
git status --short
git diff --stat
git diff --name-only
git switch -c release/remote-mcp-apim-pilot
git diff --name-only --staged
git diff --name-only -- math_rag/src/math_rag/chunker.py math_rag/src/math_rag/ingest.py math_rag/src/math_rag/downloader.py math_rag/src/math_rag/mcp_server.py math_rag/src/math_rag/rag_service.py .math_rag_index/index.json eval/
```

Azure inspection:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az login --use-device-code
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az account show --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --resource-group rg-math-rag-mcp-test --query "[].{name:name,type:type,location:location}" --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp show --name math-rag-mcp-test --resource-group rg-math-rag-mcp-test --query "{name:name,provisioningState:properties.provisioningState,runningStatus:properties.runningStatus,fqdn:properties.configuration.ingress.fqdn,external:properties.configuration.ingress.external,latestRevisionName:properties.latestRevisionName,image:properties.template.containers[0].image,env:properties.template.containers[0].env}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --query "[?contains(type, 'Microsoft.ApiManagement')].{name:name,type:type,resourceGroup:resourceGroup,location:location}" --output table
```

Remote public endpoint checks:

```bash
curl -i https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp/
curl -i https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/healthz
```

Local tests:

```bash
math_rag/.venv/bin/python -m compileall math_rag/src/math_rag/mcp_http_server.py
math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py -q
math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py math_rag/tests/test_remote_mcp_server.py math_rag/tests/test_mcp_server.py -q
math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py
math_rag/.venv/bin/python -m pytest math_rag/tests
```

Docker fixture smoke:

```bash
docker build -f deploy/azure/Dockerfile -t math-rag-mcp-http:apim-pilot .
docker run -d --rm --name math-rag-mcp-apim-smoke -p 8002:8000 -e MATH_RAG_INDEX_DIR=/data/.math_rag_index -e MATH_RAG_AUTH_MODE=bearer -e MATH_RAG_API_TOKEN=test-secret -e MATH_RAG_TOOL_MODE=chatgpt -e MATH_RAG_REMOTE_MCP_READ_ONLY=true -e MATH_RAG_HOST=0.0.0.0 -e PORT=8000 -e MATH_RAG_REMOTE_TRANSPORT=streamable-http -e MATH_RAG_REMOTE_PATH=/mcp -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false -e MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=false -v /Users/xiaxiao/Desktop/Projects/YTD_RAG/.tmp-azure-test-index:/data/.math_rag_index:ro math-rag-mcp-http:apim-pilot
curl -sS http://127.0.0.1:8002/healthz
curl -i -sS -H 'Accept: application/json, text/event-stream' http://127.0.0.1:8002/mcp
curl -i -sS -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' --data '<initialize JSON-RPC>' http://127.0.0.1:8002/mcp
curl -sS -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -H 'Mcp-Session-Id: <session-id>' --data '<tools/list JSON-RPC>' http://127.0.0.1:8002/mcp
curl -sS -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -H 'Mcp-Session-Id: <session-id>' --data '<search JSON-RPC>' http://127.0.0.1:8002/mcp
curl -sS -H 'Authorization: Bearer test-secret' -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' -H 'Mcp-Session-Id: <session-id>' --data '<fetch JSON-RPC>' http://127.0.0.1:8002/mcp
docker stop math-rag-mcp-apim-smoke
```

## Local Test Results

- `compileall`: passed.
- `test_mcp_http_server.py -q`: `14 passed`.
- Targeted MCP tests: `64 passed`.
- Full test suite: `194 passed in 4.18s`.
- Local fixture smoke: passed.
  - ChatGPT tools: `fetch`, `search`.
  - Internal tools: `rag_ask`, `rag_get_chunk`, `rag_list_sources`, `rag_search`, `rag_stats`.
  - Fixture sources reported as `sample_note.md` and `sample_paper.tex`.
  - Fixture stats: 2 sources, 4 chunks.

## Docker Test Results

- Docker build succeeded.
- Docker emitted a generic warning about `ENV "MATH_RAG_AUTH_MODE"` under the `SecretsUsedInArgOrEnv` rule; no token value is baked into the image.
- Container smoke passed:
  - `/healthz`: ok, `tool_mode=chatgpt`, `tool_count=2`, 2 fixture sources, 4 chunks.
  - unauthenticated `/mcp`: `401` with `WWW-Authenticate: Bearer`.
  - authenticated initialize: passed.
  - `tools/list`: exactly `search`, `fetch`.
  - `search`: returned 4 fixture results.
  - `fetch`: returned fixture note content with `source_id: sample_note.md`, no absolute local path.
  - container stopped after test.

## Remote Smoke Results

- Existing direct Container App `/mcp/` without auth returned `401` with bearer challenge.
- Existing direct Container App `/healthz` also returned `401`; this older pilot is not the newly documented `/healthz` behavior from `mcp_http_server.py`.
- Authenticated remote initialize/search/fetch was not rerun because the app-layer bearer secret value is stored in Azure and was not retrieved or printed.
- APIM endpoint smoke was not run because no APIM resource exists.

## ChatGPT Draft App Result

Not run. No APIM/Entra endpoint exists yet, and the existing direct Container App is not suitable for ChatGPT real-index use.

## Auth Architecture

Chosen architecture remains:

```text
ChatGPT / MCP client
  -> HTTPS
  -> Azure API Management with Entra validate-jwt / validate-azure-ad-token
  -> Container App
  -> app-layer bearer token as backend defense
  -> read-only fixture index first
```

Recommended backend-auth pattern:

- APIM validates the user's Entra JWT.
- APIM injects the private backend `Authorization: Bearer <MATH_RAG_API_TOKEN>` for the Container App.
- The Container App keeps `MATH_RAG_AUTH_MODE=bearer`.
- Do not use public no-auth.

## Direct Ingress Status

Existing Container App direct ingress is public (`external: true`). This is acceptable only for the harmless fixture pilot with app-layer bearer auth. It blocks any real-index rollout until APIM or network policy prevents direct bypass.

## Fixture-Index Status

Allowed for local/Docker pilot. The local smoke helper verifies fixture sources only and now reports sanitized source IDs.

Remote Azure fixture status:

- Existing remote pilot appears to be fixture-only based on prior logs and current image/env history.
- APIM/Entra protection is not configured.
- The current remote endpoint remains `SAFE_FOR_HARMLESS_REMOTE_FIXTURE` only.

## Real-Index Status

Not attempted. Real-index rollout is blocked.

Required before real-index rollout:

- APIM or equivalent gateway deployed.
- Entra/OIDC/JWT validation configured and tested.
- Direct Container App bypass blocked or otherwise judged safe by network policy.
- ChatGPT draft app sees only `search` and `fetch`.
- Remote `search` and `fetch` pass through the gateway.
- Path/secret leak scans pass through the gateway.
- Logs avoid full corpus text and tokens.

## Security / Path-Leak Results

- Local helper summary path leak was fixed.
- Docker `fetch` payload used `source_id: sample_note.md`.
- Search returned only ids, titles, and `math-rag://...` URLs.
- The code/tests still contain deliberate fake path strings to test sanitization.
- Documentation still necessarily references `.math_rag_index` as a mount concept, but no private absolute research path is required for the pilot workflow.

## Remaining Limitations

- APIM/Entra was not deployed.
- No ChatGPT draft app was created.
- Existing Container App remains directly reachable.
- Existing remote Container App appears to run the older pilot image/env rather than the new `mcp_http_server.py` image.
- Authenticated remote MCP calls through Azure were not rerun because the app-layer bearer secret value was not exposed.
- No real-index deployment was attempted.

## Cleanup / Cost Notes

- Docker container `math-rag-mcp-apim-smoke` was stopped.
- Workspace temporary fixture directory `.tmp-azure-test-index/` remains local and must not be staged.
- Existing Azure resources were only inspected, not modified.
- Creating APIM may have cost and quota implications; no APIM resource was created in this sprint.

## Go / No-Go Decision

- `SAFE_FOR_LOCAL_DEV`: yes.
- `SAFE_FOR_HARMLESS_REMOTE_FIXTURE`: yes, with app-layer bearer and direct-public caveat.
- `SAFE_FOR_PRIVATE_REAL_INDEX`: no.
- `NOT_SAFE_FOR_REAL_INDEX`: yes.
- `NOT_PRODUCTION_READY`: yes.

## Recommended Next Step

Create a cost-reviewed APIM/Entra fixture pilot, update the Container App to the new `mcp_http_server.py` image/env, and verify gateway-only `tools/list`, `search`, `fetch`, and path-leak scans before any real-index discussion.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
