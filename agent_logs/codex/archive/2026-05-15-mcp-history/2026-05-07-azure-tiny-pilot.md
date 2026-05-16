# Agent Log: Azure tiny remote MCP pilot

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: 6b773d1
Related files:
- `deploy/azure/README.md`
- `deploy/azure/env.example`
- `deploy/azure/test_corpus/sample_note.md`
- `deploy/azure/test_corpus/sample_paper.tex`
- `docs/azure_remote_mcp_readiness.md`
- `math_rag/src/math_rag/remote_mcp_server.py`

## Status Before

The remote read-only MCP server was working locally with app-layer bearer auth, Docker smoke tests had passed against the harmless test index, and Azure account access had been verified. No Azure resources had been created yet.

## Goal of This Task

Create the first tiny Azure pilot in `canadacentral` using only the harmless test index, verify app-layer auth remotely, and confirm that only `search` and `fetch` are exposed without path leaks.

## Changes Made

### Files Created

- `agent_logs/codex/2026-05-07-azure-tiny-pilot.md`

### Files Modified

- None in the repository for the deployment itself.

### Files Removed / Renamed

- None.

## Commands Run

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az group create --name rg-math-rag-mcp-test --location canadacentral
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az provider register -n Microsoft.OperationalInsights --wait --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az provider register -n Microsoft.ContainerRegistry --wait --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp env create --name env-math-rag-mcp-test --resource-group rg-math-rag-mcp-test --location canadacentral
math_rag/.venv/bin/python -m math_rag.cli ingest deploy/azure/test_corpus --index-dir /private/tmp/math-rag-azure-test-index
math_rag/.venv/bin/python -m math_rag.cli stats --index-dir /private/tmp/math-rag-azure-test-index
python3 -c 'import secrets; print(secrets.token_urlsafe(48))'  # stored privately in /private/tmp/math-rag-azure-pilot-api-key.txt
docker build -f .tmp-azure-deploy/Dockerfile -t ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot1 .tmp-azure-deploy
docker login ca3ae23477c8acr.azurecr.io
docker push ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot1
brew install docker-buildx
docker buildx build --builder colima --platform linux/amd64 -f .tmp-azure-deploy/Dockerfile -t ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot3-amd64 --push .tmp-azure-deploy
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp create --name math-rag-mcp-test --resource-group rg-math-rag-mcp-test --environment env-math-rag-mcp-test --image ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot1 --ingress external --target-port 8000 --transport http --registry-server ca3ae23477c8acr.azurecr.io --registry-username ... --registry-password ... --secrets mathragapikey=... --env-vars MATH_RAG_API_KEY=secretref:mathragapikey MATH_RAG_REMOTE_PUBLIC_BASE_URL=https://bootstrap.invalid MATH_RAG_REMOTE_MCP_READ_ONLY=true MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false MATH_RAG_INDEX_DIR=/app/.math_rag_index MATH_RAG_REMOTE_HOST=0.0.0.0 MATH_RAG_REMOTE_PORT=8000 MATH_RAG_REMOTE_TRANSPORT=http MATH_RAG_REMOTE_PATH=/mcp/ --min-replicas 0 --max-replicas 1 --cpu 0.5 --memory 1.0Gi
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp update --name math-rag-mcp-test --resource-group rg-math-rag-mcp-test --image ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot3-amd64
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp update --name math-rag-mcp-test --resource-group rg-math-rag-mcp-test --set-env-vars MATH_RAG_REMOTE_PUBLIC_BASE_URL=https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io
curl -i https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp/
python FastMCP client probe with Authorization: Bearer <api-key>
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --resource-group rg-math-rag-mcp-test --query "[].{name:name,type:type,location:location}" --output table
```

## Test Results

- Harmless index prep:
  - `2` sources
  - `4` chunks
  - source paths limited to:
    - `deploy/azure/test_corpus/sample_note.md`
    - `deploy/azure/test_corpus/sample_paper.tex`
- Azure HTTPS unauthenticated test:
  - `GET /mcp/` returned `401 Unauthorized`
  - `WWW-Authenticate: Bearer` present
- Authenticated FastMCP client test:
  - tools: `fetch,search`
  - `search_results=3`
  - `fetch` succeeded for returned chunk id
  - returned URLs used the Azure FQDN
  - no `/Users/...` local path leakage in search or fetch payloads
- Operational issues encountered and worked around:
  - `az containerapp up --source` hit an Azure CLI bug
  - `az acr build` was not permitted on this subscription
  - initial local image push used `linux/arm64`, which Container Apps rejected
  - final successful app revision used a `linux/amd64` image built via `docker-buildx`

## Eval Results

Not run / Reason: This task did not change retrieval ranking, chunking, downloader logic, or eval behavior. It deployed the existing remote read-only server with the harmless test index only.

## Current Status After Task

- Implemented:
  - first Azure pilot resource group
  - Container Apps environment
  - Azure Container Registry
  - public Container App endpoint
  - Container Apps secret for `MATH_RAG_API_KEY`
  - remote MCP pilot using only the harmless test index
- Tested:
  - unauthenticated HTTP access rejection
  - authenticated remote `search`
  - authenticated remote `fetch`
  - remote tool surface restricted to `search` and `fetch`
  - returned URL base updated to the Azure FQDN
  - no local path leaks
- Working:
  - public endpoint: `https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp/`
  - latest ready revision: `math-rag-mcp-test--0000001`
  - app image: `ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot3-amd64`
  - only the harmless test index is exposed
- Not implemented:
  - Azure API Management in front of the app
  - Entra ID / gateway OAuth layer
  - deployment of the real research index
- Blocked:
  - none for the tiny pilot itself
- Risk / caveat:
  - Azure resources are now live and may incur small charges
  - current auth is the app-layer bearer token only; Azure-fronted auth is still the next security step

## Known Limitations / Open Issues

- The pilot uses a public Container App endpoint with bearer-token app auth, but it is not yet behind API Management or Entra ID.
- The deployment path required multiple Azure workarounds:
  - provider registrations
  - bypassing the `containerapp up --source` CLI bug
  - bypassing blocked ACR Tasks
  - forcing a linux/amd64 build with `docker-buildx`
- Local machine state changed outside the repo:
  - Azure CLI providers registered
  - Docker ACR auth cached in `~/.docker/config.json`
  - `docker-buildx` installed

## Recommended Next Step

- Put Azure API Management with Entra-backed auth in front of this pilot endpoint before considering any non-harmless index content.

## Evidence Boundary

This log is engineering memory only. It is not mathematical theorem evidence.
