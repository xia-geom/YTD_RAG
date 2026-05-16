# Agent Log: Azure tiny pilot final status

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: 6b773d1
Related files/resources:
- Azure resource group `rg-math-rag-mcp-test`
- Azure Container App `math-rag-mcp-test`
- Azure Container Apps environment `env-math-rag-mcp-test`
- Azure Container Registry `ca3ae23477c8acr`
- Azure Log Analytics workspace `workspace-rgmathragmcptest3QJx`
- ACR image `ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot3-amd64`
- Endpoint `https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp/`

## Status Before

The main local and Azure prep work had already been done. The harmless test index existed, the remote server required bearer-token auth, and the Azure pilot resources were partially created. The remaining work was to confirm the live Azure state, ensure the app was actually running the `linux/amd64` image, and verify that the deployed endpoint exposed only harmless content.

## Goal of This Task

Finish the harmless Azure remote MCP pilot and produce a final status report for the live endpoint, without deploying any real corpus or private notes.

## Changes Made

### Files Created

- `agent_logs/codex/2026-05-07-azure-tiny-pilot-final-status.md`

### Files Modified

- None in the repository beyond this log.

### Azure Resources Created or Updated

- Confirmed existing resource group: `rg-math-rag-mcp-test`
- Confirmed existing Container Apps environment: `env-math-rag-mcp-test`
- Confirmed existing Azure Container Registry: `ca3ae23477c8acr`
- Confirmed existing Container App: `math-rag-mcp-test`
- Confirmed current running image: `ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot3-amd64`

## Commands Run

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az account show --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --resource-group rg-math-rag-mcp-test --query "[].{name:name,type:type,location:location}" --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp show --name math-rag-mcp-test --resource-group rg-math-rag-mcp-test --query "{name:name, provisioningState:properties.provisioningState, runningStatus:properties.runningStatus, fqdn:properties.configuration.ingress.fqdn, latestRevisionName:properties.latestRevisionName, image:properties.template.containers[0].image}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az acr repository list --name ca3ae23477c8acr --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az acr repository show-tags --name ca3ae23477c8acr --repository math-rag-mcp-test --output table
curl -i https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp/
python FastMCP authenticated probe against https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp/
python tighter authenticated payload inspection for forbidden strings and harmless source-path membership
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --resource-group rg-math-rag-mcp-test --query "[].{name:name,type:type,location:location}" --output table
```

## Test Results

- Azure account state:
  - subscription: `Azure for Students`
  - state: `Enabled`
- Azure resources present:
  - `workspace-rgmathragmcptest3QJx`
  - `env-math-rag-mcp-test`
  - `ca3ae23477c8acr`
  - `math-rag-mcp-test`
- Container App state:
  - provisioning state: `Succeeded`
  - running status: `Running`
  - latest revision: `math-rag-mcp-test--0000001`
  - FQDN: `math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io`
  - image: `ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:pilot3-amd64`
- ACR state:
  - repository: `math-rag-mcp-test`
  - tags: `pilot1`, `pilot3-amd64`
- Unauthenticated endpoint test:
  - `GET /mcp/` returned `401 Unauthorized`
  - `WWW-Authenticate: Bearer` present
- Authenticated endpoint test:
  - tools: `fetch,search`
  - `search_results=3`
  - `fetch` succeeded for returned chunk id
  - returned URLs used the Azure FQDN
  - no `/Users/...` path leakage
- Harmless-content verification:
  - search source paths:
    - `deploy/azure/test_corpus/sample_note.md`
    - `deploy/azure/test_corpus/sample_paper.tex`
  - fetch source path:
    - `deploy/azure/test_corpus/sample_note.md`
  - forbidden strings absent:
    - `/Users/`
    - `corpus/arxiv`
    - `corpus/my_notes`
    - `.math_rag_index`

## Current Status After Task

- Implemented:
  - Azure tiny pilot is live and reachable over HTTPS
  - Container App is running the `linux/amd64` harmless pilot image
  - app-layer bearer auth is enforced remotely
  - only harmless test-corpus content is exposed
- Tested:
  - Azure resource existence
  - Container App revision/running state
  - ACR repository/tag presence
  - unauthenticated access rejection
  - authenticated `search`
  - authenticated `fetch`
  - content exposure and path-leak checks
- Working:
  - endpoint: `https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp/`
  - tools exposed: `fetch,search`
  - content exposed: only `deploy/azure/test_corpus/` fixture content
- Not implemented:
  - Azure API Management in front of the app
  - Entra-backed gateway auth
  - deployment of any real research index
- Blocked:
  - None for the harmless pilot itself
- Risk / caveat:
  - the pilot is public on the internet and protected by the app-layer bearer token, but not yet by Azure-fronted auth
  - the Azure resources remain live and may incur small charges

## Known Limitations / Open Issues

- The current pilot is suitable for harmless connector testing, not for real private research data.
- Azure API Management / Entra protection is still the next security step before any non-harmless content.
- Local machine state changed during the pilot path:
  - `docker-buildx` installed
  - Docker ACR auth cached in `~/.docker/config.json`

## Recommended Next Step

- Put Azure API Management with Entra-backed auth in front of this endpoint before testing any non-harmless index content.
- Keep the pilot on harmless data only until that front-door auth layer exists.

## Cleanup Command Proposal

Do not run cleanup unless explicitly approved.

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az group delete --name rg-math-rag-mcp-test --yes
```

## Evidence Boundary

This log is engineering memory only. It is not mathematical theorem evidence.
