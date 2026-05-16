# Agent Log: Low-Cost Public MCP

Date: 2026-05-12
Agent: Codex with subagent handoffs
Branch: `codex/low-cost-public-mcp`
Commit: none; working tree HEAD was `e76d995`

## Status Before

The remote Streamable HTTP MCP server already existed as
`math_rag.mcp_http_server`. ChatGPT mode exposed `search` and `fetch` only. The
Azure fixture pilot was live behind APIM/Entra for harmless fixture data, but
direct Container App ingress remained public.

The previous private-index conclusion was: acceptable for harmless fixture data,
not safe for a private real-index rollout.

## Goal

Change strategy from private enterprise-style APIM/Entra hardening to a
low-cost public/semi-public read-only MCP connector suitable for Azure for
Students and ChatGPT Developer Mode.

## Strategy Change

Old private invariant:

```text
Every request must factor through APIM/Entra, and direct backend bypass blocks
real-index rollout.
```

New low-sensitivity invariant:

```text
Every request must be read-only, bounded, secret-safe, path-safe, and
cost-controlled. Public reachability is acceptable for semi-public corpus data.
```

Core tool surface remains:

```text
search
fetch
```

## Scope Guard

No retrieval, ranking, chunking, ingestion, downloader, eval logic, corpus files,
or `.math_rag_index/index.json` were changed. No real private index was mounted,
uploaded, copied, or smoke-tested. No secrets were printed. No write tools or
internal `rag_*` tools were exposed to ChatGPT mode.

## Chosen Architecture

Architecture B was chosen:

```text
ChatGPT Developer Mode app
  -> APIM Consumption /mcp with No Authentication
  -> APIM injects backend bearer token
  -> Container App with MATH_RAG_AUTH_MODE=bearer
  -> read-only fixture or public-safe index
```

The direct Container App endpoint remains bearer-protected for `/mcp` and should
not be used as the ChatGPT connector URL.

## Auth Decision

Official OpenAI docs reviewed:

- ChatGPT Developer Mode supports remote MCP over SSE and streaming HTTP.
- ChatGPT Developer Mode app authentication options are OAuth, No
  Authentication, and Mixed Authentication.
- The Apps SDK authentication docs describe OAuth 2.1 for authenticated MCP apps
  and say ChatGPT attaches the OAuth access token after the OAuth flow.
- The Responses API MCP tool can pass an `authorization` field, but that is API
  usage, not the ChatGPT Developer Mode connector setup.

Decision: ChatGPT Developer Mode does not currently provide a simple static
bearer/API-token field for a created app. Use APIM No Authentication for the
ChatGPT-facing façade, and keep the Container App protected by backend bearer.

## Cost Findings

Azure account inspection confirmed:

```text
Subscription: Azure for Students
State: Enabled
Tenant: UQAM
```

Live resources inspected in `rg-math-rag-mcp-test`:

| Resource | Purpose | SKU / setting | Keep / remove | Reason |
| --- | --- | --- | --- | --- |
| `math-rag-mcp-test` Container App | MCP backend | `0.5` CPU, `1Gi`, min replicas `0`, max replicas `1` | Keep for pilot | Already scale-to-zero and capped to one replica. |
| `env-math-rag-mcp-test` Container Apps environment | ACA host/logging | Log Analytics destination | Keep while testing | Required for Container App. |
| `ca3ae23477c8acr` ACR | Container image | `Basic` | Keep while testing; remove when idle | Basic registry unit is a fixed daily cost surface. |
| `stmathragmcp5d67a258` Storage | Fixture Azure Files index | `Standard_LRS` | Optional | Tiny fixture storage is low cost; baking a public-safe index into the image could remove this surface later. |
| `workspace-rgmathragmcptest3QJx` Log Analytics | Container logs | `PerGB2018`, 30-day retention | Keep minimal | Avoid body/snippet logging; ingestion can cost after any free grant. |
| `apim-math-rag-mcp-5d67a258` APIM | ChatGPT-compatible façade | `Consumption` | Keep for pilot | No fixed hourly APIM unit cost observed for Consumption calls; call volume can still cost after free tier. |

Retail price checks observed:

- APIM Consumption calls: first observed tier at `$0` per 10K calls, then
  `$0.035` per 10K calls.
- Container Apps Standard: active vCPU, memory, requests, and idle usage meters;
  scale-to-zero remains the key cost control.
- ACR Basic registry unit: `$0.1666` per day, plus data stored.
- Azure Files Standard LRS: `$0.066` per GB-month plus operations.
- Log Analytics: first observed ingestion tier at `$0`, then `$2.76` per GB;
  retention observed at `$0.12` per GB-month.

Do not claim the deployment is free. Expected posture is near-free for light
usage under Azure Student/Consumption limits, but storage, registry, logging,
bandwidth, APIM calls, and unexpected traffic may cost money.

## Azure Resources Kept / Created / Updated

Created: none.

Updated:

- APIM API policy for `math-rag-mcp` at `/mcp`.

Previous policy required an Entra JWT. New low-sensitivity policy removes
`validate-jwt`, injects the backend bearer token from the existing secret named
value, and rewrites to `/mcp`.

Attempted but rejected:

- APIM `rate-limit-by-key`; Azure rejected it with
  `Policy is not allowed in 'Consumption' sku`.

Rollback file:

```text
/private/tmp/math-rag-apim-mcp-policy-rollback.xml
```

Rollback command shape:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az rest \
  --method put \
  --url "https://management.azure.com/subscriptions/<subscription>/resourceGroups/rg-math-rag-mcp-test/providers/Microsoft.ApiManagement/service/apim-math-rag-mcp-5d67a258/apis/math-rag-mcp/policies/policy?api-version=2022-08-01" \
  --headers "Content-Type=application/json" \
  --body @<policy-json>
```

## Environment Variables

Backend Container App keeps:

```text
MATH_RAG_INDEX_DIR=/data/.math_rag_index
MATH_RAG_AUTH_MODE=bearer
MATH_RAG_API_TOKEN=<Azure secret reference>
MATH_RAG_TOOL_MODE=chatgpt
MATH_RAG_REMOTE_MCP_READ_ONLY=true
MATH_RAG_HOST=0.0.0.0
PORT=8000
MATH_RAG_REMOTE_TRANSPORT=streamable-http
MATH_RAG_REMOTE_PATH=/mcp
MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false
MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=false
```

## Data Packaging Decision

For the current pilot, keep the existing read-only Azure Files fixture index.
This avoids packaging or exposing any real corpus/index during the strategy
change.

For a cheap public demo with a public-safe index, preferred next packaging is to
bake only a reviewed public-safe `.math_rag_index/index.json` into the image if
the index size is reasonable. Do not bake raw `corpus/`, PDFs, `.env`, secrets,
private notes, or unpublished material.

## Commands Run

Repository:

```bash
pwd
git branch --show-current
git rev-parse --short HEAD
git status --short
git switch -c codex/low-cost-public-mcp
```

OpenAI documentation:

- `https://developers.openai.com/api/docs/guides/developer-mode`
- `https://developers.openai.com/apps-sdk/build/auth`
- `https://developers.openai.com/apps-sdk/deploy/connect-chatgpt`
- `https://developers.openai.com/api/docs/guides/tools-connectors-mcp`
- `https://developers.openai.com/api/docs/mcp`

Azure inspection:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az account show --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --resource-group rg-math-rag-mcp-test --query "[].{name:name,type:type,location:location,sku:sku.name}" --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp show --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --query "{name:name, provisioningState:properties.provisioningState, runningStatus:properties.runningStatus, fqdn:properties.configuration.ingress.fqdn, external:properties.configuration.ingress.external, targetPort:properties.configuration.ingress.targetPort, minReplicas:properties.template.scale.minReplicas, maxReplicas:properties.template.scale.maxReplicas, cpu:properties.template.containers[0].resources.cpu, memory:properties.template.containers[0].resources.memory, image:properties.template.containers[0].image}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim show --resource-group rg-math-rag-mcp-test --name apim-math-rag-mcp-5d67a258 --query "{name:name, sku:sku.name, provisioningState:provisioningState, gatewayUrl:gatewayUrl}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az acr show --resource-group rg-math-rag-mcp-test --name ca3ae23477c8acr --query "{name:name,sku:sku.name,loginServer:loginServer,provisioningState:provisioningState,publicNetworkAccess:publicNetworkAccess}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az storage account show --resource-group rg-math-rag-mcp-test --name stmathragmcp5d67a258 --query "{name:name,sku:sku.name,kind:kind,primaryLocation:primaryLocation,provisioningState:provisioningState,allowBlobPublicAccess:allowBlobPublicAccess,minimumTlsVersion:minimumTlsVersion}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az monitor log-analytics workspace show --resource-group rg-math-rag-mcp-test --workspace-name workspace-rgmathragmcptest3QJx --query "{name:name,sku:sku.name,retentionInDays:retentionInDays,provisioningState:provisioningState}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az rest --method get --url "<APIM policy ARM URL>" --query properties.value --output tsv
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az rest --method put --url "<APIM policy ARM URL>" --headers "Content-Type=application/json" --body @/private/tmp/math-rag-apim-public-mcp-policy.json --output none
```

Smoke:

```bash
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i -sS -H 'Accept: application/json, text/event-stream' https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp
```

## Tests Run

No local Python tests were run because no Python code was changed in this pass.
The stdio MCP server was not modified.

## Smoke Results

Before the policy change, APIM `/healthz` returned `200 OK` with:

```json
{"tool_mode":"chatgpt","tool_count":2,"index_present":true,"chunk_count":4,"source_count":2}
```

After the APIM no-auth façade policy update:

- APIM policy verification through Azure ARM succeeded; `validate-jwt` is gone
  and backend bearer injection remains.
- APIM `/healthz` returned `200 OK` once after the update with the same fixture
  counts.
- Full APIM MCP initialize/tools/search/fetch smoke could not be completed
  afterward because this local environment intermittently failed DNS resolution
  for `apim-math-rag-mcp-5d67a258.azure-api.net`.
- Direct Container App unauthenticated `/mcp` returned `401 Unauthorized`,
  confirming backend bearer protection remains active.

Latest verified tool list from the pre-change APIM smoke was exactly:

```text
search,fetch
```

Because the APIM policy does not alter backend tools and the backend
environment was not changed, the expected ChatGPT-visible tools remain
`search` and `fetch`. This still needs one post-change ChatGPT/remote MCP smoke
when DNS is stable.

## Path / Secret Leak Scan

The attempted post-change APIM MCP smoke did not produce `tools/list`,
`search`, or `fetch` payloads due DNS failures, so there was no new payload to
scan.

The latest successful APIM payload scan from the fixture pilot passed for:

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
.env
connectionString
AccountKey
SharedAccessSignature
.math_rag_index
```

No secrets were printed in this pass.

## Cost / Cleanup Notes

Cleanup command, not run:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az group delete \
  --name rg-math-rag-mcp-test \
  --yes \
  --no-wait
```

Selective cleanup commands, not run:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp delete --name math-rag-mcp-test --resource-group rg-math-rag-mcp-test --yes
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim delete --name apim-math-rag-mcp-5d67a258 --resource-group rg-math-rag-mcp-test --yes
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az acr delete --name ca3ae23477c8acr --resource-group rg-math-rag-mcp-test --yes
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az storage account delete --name stmathragmcp5d67a258 --resource-group rg-math-rag-mcp-test --yes
```

## Go / No-Go

- `SAFE_FOR_LOW_SENSITIVITY_PUBLIC_READ`: yes, with fixture data and bounded
  read-only tools
- `SAFE_FOR_CHATGPT_DEVELOPER_TEST`: partial; architecture and APIM policy are
  configured, but a post-change ChatGPT/manual MCP smoke is still needed
- `SAFE_FOR_PRIVATE_REAL_INDEX`: no
- `PRODUCTION_READY_PRIVATE_ARCHIVE`: no
- `COST_BOUNDED_FOR_STUDENT_PILOT`: yes, with caveat that unexpected traffic and
  storage/registry/logging can cost money
- `NEEDS_USER_APPROVAL_BEFORE_PUBLIC_NO_AUTH`: yes

## Recommended Next Step

When DNS is stable, create a ChatGPT Developer Mode connector with No
Authentication at `https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp`, verify
`tools/list` shows exactly `search` and `fetch`, then run one fixture
`search`/`fetch` and path/secret scan.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
