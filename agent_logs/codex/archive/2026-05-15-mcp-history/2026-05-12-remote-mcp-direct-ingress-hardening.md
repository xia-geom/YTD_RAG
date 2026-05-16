# Agent Log: Remote MCP Direct Ingress Hardening

Date: 2026-05-12
Agent: Codex
Branch: `codex/remote-mcp-block-direct-ingress`
Commit: none; working tree HEAD was `e76d995`

## Related Files / Resources

- Documentation updated:
  - `docs/azure_remote_mcp_readiness.md`
  - `deploy/azure/README.md`
- Azure resources inspected:
  - Resource group: `rg-math-rag-mcp-test`
  - Container App: `math-rag-mcp-test`
  - Container Apps environment: `env-math-rag-mcp-test`
  - API Management: `apim-math-rag-mcp-5d67a258`
  - APIM gateway: `https://apim-math-rag-mcp-5d67a258.azure-api.net`
  - Direct Container App FQDN: `https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io`

## Status Before

The APIM / Entra fixture pilot already passed APIM `/healthz`, `/readyz`,
authenticated MCP initialize, `tools/list`, `search`, `fetch`, and path/secret
scanning. ChatGPT mode exposed exactly `search` and `fetch`.

The remaining blocker was public direct Container App ingress. Direct
unauthenticated `/mcp` was rejected by app-layer bearer auth, but direct network
access to the Container App FQDN remained possible.

## Goal

Resolve, or precisely characterize with evidence, whether direct public
Container App ingress can be blocked while preserving APIM access to the
harmless fixture-index MCP server.

## Scope Guard

No retrieval, ranking, chunking, ingestion, downloader, corpus, eval,
`.math_rag_index/index.json`, or local stdio MCP behavior was changed. The real
research index was not deployed, mounted, uploaded, copied, smoke-tested, or
exposed. No write tools were enabled.

## Changes Made

No Azure network changes were applied.

Documentation was updated to record the current direct-ingress blocker, the
reviewed mitigation options, rollback guidance, and the production direction
needed before a real-index rollout.

## Azure Resources Created / Updated

None.

## Auth / Network Architecture

Current fixture path:

```text
Entra JWT
  -> APIM /mcp
  -> APIM validates issuer/audience/scope/user claim
  -> APIM injects backend bearer token from a secret named value
  -> public Container App FQDN
  -> app-layer bearer auth
  -> harmless fixture index
```

APIM MCP policy still validates a Microsoft Entra token and sets the backend
`Authorization` header using `Bearer {{math-rag-backend-token}}`. The named
value secret was not printed or retrieved.

The Container App keeps:

- `MATH_RAG_INDEX_DIR=/data/.math_rag_index`
- `MATH_RAG_AUTH_MODE=bearer`
- `MATH_RAG_API_TOKEN` from secret reference `mathragapitoken`
- `MATH_RAG_TOOL_MODE=chatgpt`
- `MATH_RAG_REMOTE_MCP_READ_ONLY=true`
- `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false`
- `MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=false`

## Direct Ingress Status

Direct ingress is not blocked at the network layer.

Container App inspection:

```json
{
  "external": true,
  "fqdn": "math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io",
  "ipSecurityRestrictions": null,
  "runningStatus": "Running",
  "targetPort": 8000,
  "transport": "Http"
}
```

APIM inspection:

```json
{
  "gatewayUrl": "https://apim-math-rag-mcp-5d67a258.azure-api.net",
  "privateIPAddresses": null,
  "publicIPAddresses": null,
  "publicNetworkAccess": "Enabled",
  "sku": "Consumption",
  "virtualNetworkType": "None"
}
```

Container Apps environment inspection:

```json
{
  "defaultDomain": "bravehill-bd729733.canadacentral.azurecontainerapps.io",
  "internalLoadBalancerEnabled": null,
  "staticIp": "20.116.187.16",
  "vnetConfiguration": null
}
```

Direct public checks:

- Direct `GET /healthz`: `200 OK`
- Direct `GET /readyz`: `200 OK`
- Direct unauthenticated `GET /mcp`: `401 Unauthorized`
- Direct wrong-bearer `POST /mcp initialize`: `401 Unauthorized`

The direct FQDN is reachable. App-layer bearer auth blocks missing or wrong
tokens, but a caller with the backend bearer token could bypass APIM. This is
acceptable only for the harmless fixture pilot.

## Mitigation Review

### A. Private / Internal Backend Path

Not implemented.

Evidence:

- Current APIM SKU is `Consumption`.
- Current APIM has no VNet integration, no private IPs, and no dedicated public
  IPs.
- Current Container Apps environment has no VNet configuration or internal load
  balancer.
- APIM currently forwards to the public Container App service URL.

Microsoft documentation reviewed:

- Azure Container Apps external ingress can receive public internet traffic,
  while internal ingress is reachable only within the same Container Apps
  environment:
  `https://learn.microsoft.com/en-us/azure/container-apps/ingress-overview`
- APIM networking options depend on tier; VNet injection/integration is
  available only on selected Developer/Premium/Standard v2/Premium v2 designs,
  not the current Consumption instance:
  `https://learn.microsoft.com/en-us/azure/api-management/virtual-network-concepts`
  and `https://learn.microsoft.com/en-us/azure/api-management/api-management-features`

Production direction: create a network-capable APIM / Container Apps design
before real-index rollout. This likely requires a new or upgraded APIM design
and private networking resources, so it was not done without explicit approval.

### B. IP Ingress Restriction

Not implemented.

Evidence:

- Container Apps supports IP allow/deny rules, and no rules are currently set.
- APIM Consumption runs on shared infrastructure without a deterministic
  dedicated IP address; Microsoft documents that Consumption outbound allowlists
  require broad Azure datacenter ranges rather than a narrow instance IP.

Because the current APIM instance exposes no stable dedicated outbound IP, an
allowlist would either be too broad to block meaningful public bypass or risk
breaking APIM. It is not treated as a production-grade mitigation.

### C. Disable Direct Ingress

Not implemented.

Evidence:

- APIM API service URLs point to the public Container App FQDN.
- APIM has no private backend path to the Container Apps environment.

Disabling Container App ingress in this architecture would break APIM backend
forwarding.

### D. Leave Unchanged and Document Blocker

Chosen outcome.

The fixture pilot remains valid for harmless fixture content only. Real-index
rollout remains blocked until direct public backend bypass is blocked at the
network/ingress layer or an equivalent reviewed control is implemented.

## Commands Run

Repository:

```bash
git branch --show-current
git rev-parse --short HEAD
git status --short
git switch -c codex/remote-mcp-block-direct-ingress
```

Azure inspection:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az account show --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp show --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --query "{name:name, provisioningState:properties.provisioningState, runningStatus:properties.runningStatus, fqdn:properties.configuration.ingress.fqdn, external:properties.configuration.ingress.external, targetPort:properties.configuration.ingress.targetPort, transport:properties.configuration.ingress.transport, ipSecurityRestrictions:properties.configuration.ingress.ipSecurityRestrictions, latestRevisionName:properties.latestRevisionName, image:properties.template.containers[0].image}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim show --resource-group rg-math-rag-mcp-test --name apim-math-rag-mcp-5d67a258 --query "{name:name, sku:sku.name, provisioningState:provisioningState, publicIPAddresses:publicIPAddresses, privateIPAddresses:privateIPAddresses, gatewayUrl:gatewayUrl, publicNetworkAccess:publicNetworkAccess, virtualNetworkType:virtualNetworkType}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp env show --resource-group rg-math-rag-mcp-test --name env-math-rag-mcp-test --query "{name:name,provisioningState:properties.provisioningState,internalLoadBalancerEnabled:properties.vnetConfiguration.internal, infrastructureResourceGroup:properties.infrastructureResourceGroup, defaultDomain:properties.defaultDomain, staticIp:properties.staticIp, vnetConfiguration:properties.vnetConfiguration}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp ingress access-restriction list --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim api list --resource-group rg-math-rag-mcp-test --service-name apim-math-rag-mcp-5d67a258 --query "[].{name:name,path:path,protocols:protocols,serviceUrl:serviceUrl}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az rest --method get --url "https://management.azure.com/subscriptions/5d67a258-2450-4ffd-9266-9bdf8fa99bd0/resourceGroups/rg-math-rag-mcp-test/providers/Microsoft.ApiManagement/service/apim-math-rag-mcp-5d67a258/apis/math-rag-mcp/policies/policy?api-version=2022-08-01" --query properties.value --output tsv
```

Remote smoke:

```bash
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/readyz
curl -i -sS -H 'Accept: application/json, text/event-stream' https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
curl -i -sS https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/healthz
curl -i -sS https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/readyz
curl -i -sS -H 'Accept: application/json, text/event-stream' https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp
curl -i -sS -H 'Accept: application/json, text/event-stream' -H 'Authorization: Bearer definitely-not-the-backend-token' -H 'Content-Type: application/json' --data '<initialize JSON-RPC>' https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp
```

Authenticated APIM MCP smoke used `az account get-access-token` with the
approved CLI config and did not print the access token.

## Test Results

Local package tests were not run. This was a deployment/auth characterization
pass with documentation-only repository edits and no Python code changes.

## Remote Smoke Results

APIM:

- `GET /healthz`: `200 OK`, `tool_mode=chatgpt`, `tool_count=2`,
  `index_present=true`, `chunk_count=4`, `source_count=2`
- `GET /readyz`: `200 OK`, `status=ready`, `index_present=true`
- unauthenticated `/mcp`: `401 Unauthorized`
- authenticated initialize: `200`
- `notifications/initialized`: `202`
- `tools/list`: `search,fetch`
- `search` for `Remote MCP Test Note`: `200`, four fixture results
- `fetch` for the first returned id: `200`, title `sample note`

Direct Container App:

- `GET /healthz`: `200 OK`
- `GET /readyz`: `200 OK`
- unauthenticated `/mcp`: `401 Unauthorized`
- wrong-bearer initialize: `401 Unauthorized`

## Path / Secret Leak Scan

Captured APIM `tools/list`, `search`, and `fetch` payloads under
`/private/tmp/math-rag-apim-direct-hardening-smoke/` and scanned for:

```text
/Users/
/home/
/mnt/data/
file://
corpus/arxiv
corpus/my_notes
OPENAI_API_KEY
MATH_RAG_API_TOKEN
MATH_RAG_API_KEY
AZURE_
private/tmp
.math_rag_index
```

Result: passed. No forbidden strings were found in the captured APIM payloads.

## Real-Index Status

Not deployed. Not mounted. Not uploaded. Not copied. Not smoke-tested.

Real-index rollout remains blocked.

## Cleanup / Cost Notes

No Azure resources were created, deleted, upgraded, or network-reconfigured in
this pass.

The existing APIM Consumption and fixture storage resources may continue to
incur pilot costs. A production-grade private backend path will likely require a
new network-capable APIM / Container Apps architecture or SKU change; that was
not implemented because it is cost-affecting and requires explicit approval.

## Go / No-Go Decision

- `SAFE_FOR_HARMLESS_REMOTE_FIXTURE`: yes
- `SAFE_FOR_APIM_ENTRA_FIXTURE_PILOT`: yes, for fixture content only
- `SAFE_FOR_PRIVATE_REAL_INDEX`: no
- `NOT_SAFE_FOR_REAL_INDEX`: yes
- `NOT_PRODUCTION_READY`: yes

## Recommended Next Step

Design and cost a private-backend architecture using a network-capable APIM tier
and private/internal Container Apps backend, then get explicit approval before
creating or upgrading paid networking resources.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
