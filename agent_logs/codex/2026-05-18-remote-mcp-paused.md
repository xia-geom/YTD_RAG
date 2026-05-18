# Remote MCP Paused

Date: 2026-05-18

## Goal And Scope

Pause the live Azure remote MCP connector while preserving local RAG usage and
keeping the Azure deployment recoverable. This task did not delete the resource
group, storage account, Azure Files shares, APIM service, ACR, or Container App.

## Status Before

- Branch: `codex/private-index-risk-accepted-pilot`
- HEAD: `59a7da3`
- The working tree already had unrelated dirty files before this task.
- Container App `math-rag-mcp-test` had external ingress enabled.
- Container App scale was min replicas `0`, max replicas `1`.
- APIM APIs `mcp`, `healthz`, and `readyz` pointed to the Container App public
  FQDN.
- The Container App mounted Azure Files storage `math-rag-public-safe-index` at
  `/data/.math_rag_index`.

## Azure Resources Inspected

Resource group `rg-math-rag-mcp-test` contained:

- Container Apps environment `env-math-rag-mcp-test`
- Container App `math-rag-mcp-test`
- APIM Consumption service `apim-math-rag-mcp-5d67a258`
- ACR Basic registry `ca3ae23477c8acr`
- StorageV2 account `stmathragmcp5d67a258`
- Log Analytics workspace `workspace-rgmathragmcptest3QJx`

Azure Files shares inspected:

- `math-rag-fixture-index`
- `math-rag-public-safe-index`

## Changes Made

- Disabled ingress for Container App `math-rag-mcp-test`.
- Updated `AGENTS.md` to mark remote MCP as paused and point future agents to
  this log.

No local RAG source, retrieval, ranking, corpus, eval, or index files were
modified by this pause task.

## Commands Run

```bash
git status --short
git branch --show-current
git rev-parse --short HEAD
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az login
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --resource-group rg-math-rag-mcp-test --query "[].{name:name,type:type,location:location,sku:sku.name}" --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp show --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --query "{name:name,provisioningState:properties.provisioningState,runningStatus:properties.runningStatus,latestRevisionName:properties.latestRevisionName,latestReadyRevisionName:properties.latestReadyRevisionName,fqdn:properties.configuration.ingress.fqdn,external:properties.configuration.ingress.external,targetPort:properties.configuration.ingress.targetPort,transport:properties.configuration.ingress.transport,minReplicas:properties.template.scale.minReplicas,maxReplicas:properties.template.scale.maxReplicas,volumes:properties.template.volumes,volumeMounts:properties.template.containers[0].volumeMounts}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim api list --resource-group rg-math-rag-mcp-test --service-name apim-math-rag-mcp-5d67a258 --query "[].{name:name,path:path,protocols:protocols,serviceUrl:serviceUrl}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az storage share-rm list --resource-group rg-math-rag-mcp-test --storage-account stmathragmcp5d67a258 --query "[].{name:name,quota:shareQuota,enabledProtocols:enabledProtocols,accessTier:accessTier}" --output json
curl -i -sS --max-time 20 https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i -sS --max-time 20 https://apim-math-rag-mcp-5d67a258.azure-api.net/readyz
curl -i -sS --max-time 20 -H "Accept: application/json, text/event-stream" https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp ingress disable --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp show --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --query "{name:name,provisioningState:properties.provisioningState,runningStatus:properties.runningStatus,latestRevisionName:properties.latestRevisionName,latestReadyRevisionName:properties.latestReadyRevisionName,ingress:properties.configuration.ingress,minReplicas:properties.template.scale.minReplicas,maxReplicas:properties.template.scale.maxReplicas,volumes:properties.template.volumes,volumeMounts:properties.template.containers[0].volumeMounts}" --output json
curl -i -sS --max-time 20 https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i -sS --max-time 20 https://apim-math-rag-mcp-5d67a258.azure-api.net/readyz
curl -i -sS --max-time 20 -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" --data '{"jsonrpc":"2.0","id":"pause-check","method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"pause-check","version":"1"}}}' https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
curl -i -sS --max-time 20 -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" --data '{"jsonrpc":"2.0","id":"pause-check","method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"pause-check","version":"1"}}}' https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp
```

## Test Results

- Post-pause `az containerapp show` reports `ingress: null`.
- APIM `/healthz` returns `404 Not Found` with Azure Container App unavailable
  HTML.
- APIM `/readyz` returns `404 Not Found` with Azure Container App unavailable
  HTML.
- APIM `/mcp` initialize returns `404 Not Found` with Azure Container App
  unavailable HTML.
- Direct Container App `/mcp` initialize returns `404 Not Found` with Azure
  Container App unavailable HTML.

Before the pause, APIM and direct probes timed out at 20 seconds, likely due to
scale-to-zero cold start or network latency. The post-pause 404 responses are
the expected result of disabled ingress.

## Current Status After Task

Remote MCP serving is paused. The APIM gateway still exists, but its configured
backend FQDN is unavailable because Container App ingress is disabled. The local
RAG workflow is unchanged.

## Remaining Costs

Because the resource group was preserved, some costs may remain:

- Azure Files storage and operations for fixture/public-safe shares
- ACR Basic registry storage
- Log Analytics retention/ingestion
- APIM Consumption metadata/calls
- Any other Azure platform minimums or unexpected traffic

## Resume Command

Re-enable ingress before using APIM or ChatGPT again:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp ingress enable \
  --resource-group rg-math-rag-mcp-test \
  --name math-rag-mcp-test \
  --type external \
  --target-port 8000 \
  --transport http
```

Then verify APIM `/healthz`, `/readyz`, MCP `initialize`, `tools/list`,
`search`, and `fetch`.

## Full Cleanup Command

Only run this if deleting the remote MCP test deployment is intended:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az group delete \
  --name rg-math-rag-mcp-test \
  --yes \
  --no-wait
```

## Recommended Next Step

Use local RAG only. Revisit remote MCP only if there is a concrete ChatGPT or
public-safe sharing need.
