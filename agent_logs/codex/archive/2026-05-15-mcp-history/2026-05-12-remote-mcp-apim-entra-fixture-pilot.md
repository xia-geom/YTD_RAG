# Agent Log: Remote MCP APIM Entra Fixture Pilot

Date: 2026-05-12
Agent: Codex
Branch: release/remote-mcp-apim-pilot
Commit: none; working tree HEAD was e76d995

## Goal

Create a safe Azure API Management / Microsoft Entra front door for the `math_rag.mcp_http_server` ChatGPT-compatible remote MCP server, using only the harmless fixture index. Do not expose the real research index.

## Scope Guard

No retrieval, ranking, chunking, ingestion, downloader, corpus, eval, `.math_rag_index/index.json`, or local stdio MCP behavior was changed in this sprint. The real research index was not deployed.

## APIM Tier / Cost Note

Before creating APIM, Azure Retail Prices were queried for API Management in `canadacentral`.

Recorded pilot choice:

- Tier: API Management `Consumption`
- Region: Canada Central
- Retail pricing record: `Consumption Calls`
- Price observed: USD `$0` for the initial tier of 100 units of 10K calls, then USD `$0.035` per 10K calls after that tier
- Fixed hourly APIM unit cost observed for Consumption: none in the retail price response

This was chosen as the smallest suitable pilot tier. Storage account costs for the fixture Azure Files share still apply.

## Azure Resources Created / Updated

Created:

- API Management: `apim-math-rag-mcp-5d67a258`
  - Gateway: `https://apim-math-rag-mcp-5d67a258.azure-api.net`
  - SKU: `Consumption`
  - Status: `Succeeded`
- Storage account: `stmathragmcp5d67a258`
- Azure Files share: `math-rag-fixture-index`
  - Contains fixture `index.json` only
- Container Apps environment storage: `math-rag-fixture-index`
  - Access mode: `ReadOnly`
- APIM APIs:
  - `math-rag-mcp` at `/mcp`
  - `math-rag-healthz` at `/healthz`
  - `math-rag-readyz` at `/readyz`
- APIM named value:
  - `math-rag-backend-token`
  - Secret value not printed

Updated:

- ACR image pushed: `ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:mcp-http-20260512-amd64`
- Container App: `math-rag-mcp-test`
  - Current image: `ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:mcp-http-20260512-amd64`
  - Revision: `math-rag-mcp-test--0000002`
  - Traffic: 100%
  - Health: Healthy
  - Mounted fixture storage at `/data/.math_rag_index`
  - `MATH_RAG_TOOL_MODE=chatgpt`
  - `MATH_RAG_AUTH_MODE=bearer`
  - `MATH_RAG_REMOTE_MCP_READ_ONLY=true`
  - `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false`
  - `MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=false`

## Auth Architecture

Implemented for fixture pilot:

```text
Entra JWT -> APIM /mcp -> APIM injects backend bearer -> Container App -> fixture index
```

APIM `/mcp` policy:

- Validates `Authorization: Bearer ...` JWT.
- OpenID config: `https://login.microsoftonline.com/12cb4e1a-42da-491c-90e1-7a7a9753506f/.well-known/openid-configuration`
- Issuer: `https://sts.windows.net/12cb4e1a-42da-491c-90e1-7a7a9753506f/`
- Audience used for this CLI-verifiable pilot: `https://management.azure.com/`
- Required scope claim: `scp=user_impersonation`
- Required user claim: `upn=kj091980@ens.uqam.ca`
- APIM overrides backend `Authorization` with `Bearer {{math-rag-backend-token}}`.

Caveat: this validates Entra JWTs and restricts the pilot to the signed-in user, but it is not yet a ChatGPT OAuth app registration. A production ChatGPT connector should use a dedicated Entra app audience/scope such as `api://<client-id>/mcp.read`.

## Direct Ingress Status

Container App direct ingress remains public:

- FQDN: `https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io`
- `external=true`
- Direct unauthenticated `/mcp` is rejected by app-layer bearer auth.
- Direct `/healthz` and `/readyz` are public status endpoints from the app.

Because direct ingress is still reachable, a caller with the backend bearer token could bypass APIM. This is acceptable for the harmless fixture pilot only. It blocks real-index rollout.

## Commands Run

Cost/pricing:

```bash
curl -sS "https://prices.azure.com/api/retail/prices?currencyCode=USD&%24filter=serviceName%20eq%20%27API%20Management%27%20and%20armRegionName%20eq%20%27canadacentral%27"
```

Local/Docker preparation:

```bash
docker buildx build --platform linux/amd64 -f deploy/azure/Dockerfile -t ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:mcp-http-20260512-amd64 --push .
```

Azure setup and inspection:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az provider register -n Microsoft.Storage --wait --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az storage account create --resource-group rg-math-rag-mcp-test --name stmathragmcp5d67a258 --location canadacentral --sku Standard_LRS --kind StorageV2 --allow-blob-public-access false --https-only true --min-tls-version TLS1_2
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp env storage set --resource-group rg-math-rag-mcp-test --name env-math-rag-mcp-test --storage-name math-rag-fixture-index --access-mode ReadOnly
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim create --name apim-math-rag-mcp-5d67a258 --resource-group rg-math-rag-mcp-test --location canadacentral --sku-name Consumption --publisher-email kj091980@ens.uqam.ca --publisher-name math-rag-fixture-pilot
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp update --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --yaml /tmp/math-rag-aca-update.yaml
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim api create ...
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim api operation create ...
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim nv create ...
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az rest --method put .../apis/math-rag-mcp/policies/policy...
```

Remote smoke:

```bash
curl -i https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i https://apim-math-rag-mcp-5d67a258.azure-api.net/readyz
curl -i -H 'Accept: application/json, text/event-stream' https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
TOKEN=$(AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az account get-access-token --resource https://management.azure.com/ --query accessToken -o tsv)
curl -i -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' --data '<initialize JSON-RPC>' https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
curl -H "Authorization: Bearer $TOKEN" -H 'Mcp-Session-Id: <session-id>' --data '<tools/list JSON-RPC>' https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
curl -H "Authorization: Bearer $TOKEN" -H 'Mcp-Session-Id: <session-id>' --data '<search JSON-RPC>' https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
curl -H "Authorization: Bearer $TOKEN" -H 'Mcp-Session-Id: <session-id>' --data '<fetch JSON-RPC>' https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
```

## Local / Docker Test Results

From the prior release-cut run on this branch:

- Full package tests: `194 passed`
- Docker fixture smoke: passed
- ChatGPT mode exposed exactly `search` and `fetch`
- Local/Docker bearer auth worked
- Fixture output was sanitized to `sample_note.md`, `sample_paper.tex`, and `<fixture-index>`

This sprint did not change retrieval or HTTP MCP server code.

## Remote Test Results

APIM endpoint:

- `GET /healthz`: `200 OK`
  - `tool_mode=chatgpt`
  - `tool_count=2`
  - `index_present=true`
  - `chunk_count=4`
  - `source_count=2`
- `GET /readyz`: `200 OK`
  - `status=ready`
  - `index_present=true`
- unauthenticated `/mcp`: `401 Unauthorized`
- authenticated initialize through APIM: passed
- `notifications/initialized`: `202`
- `tools/list`: exactly `search`, `fetch`
- `search` for `Remote MCP Test Note`: returned four fixture results, no raw text in search
- `fetch` for `chunk-1337d032580f72f6`: returned harmless fixture note text and metadata with `source_id=sample_note.md`

## Path / Secret Leak Scan

Remote APIM payload scan checked:

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

Result: passed. The captured APIM payload file was 4,739 bytes and contained no forbidden strings.

## ChatGPT Draft App Result

Not run. The APIM endpoint works, but this Codex session does not have a configured ChatGPT developer-mode app creation workflow. The endpoint should be tested manually as a draft app using:

```text
https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
```

Expected visible tools:

```text
search
fetch
```

Do not connect a real-index backend for this draft app yet.

## Real-Index Status

Not deployed. Real-index rollout remains blocked.

Required before real index:

- Dedicated ChatGPT-compatible Entra app registration and `mcp.read` scope.
- ChatGPT draft app verification through APIM.
- Direct Container App bypass blocked by network policy or equivalent.
- Remote path/secret scan passes with the real index.
- Logs and retention policy are reviewed for private research content.

## Cleanup / Cost Notes

Resources now incurring possible cost:

- APIM Consumption service `apim-math-rag-mcp-5d67a258`
- Storage account `stmathragmcp5d67a258`
- Existing Container App and ACR resources

Local temporary files/directories remain unstaged:

- `.tmp-azure-test-index/`
- `.tmp-azure-deploy/`
- `.tmp-docker-test-index-auth/`
- `/tmp/math-rag-aca-update.yaml`
- `/tmp/math-rag-apim-payloads.txt`

## Go / No-Go Decision

- `SAFE_FOR_LOCAL_DEV`: yes
- `SAFE_FOR_HARMLESS_REMOTE_FIXTURE`: yes
- `SAFE_FOR_APIM_ENTRA_FIXTURE_PILOT`: yes, for the signed-in UQAM user and fixture data only
- `SAFE_FOR_PRIVATE_REAL_INDEX`: no
- `NOT_SAFE_FOR_REAL_INDEX`: yes
- `NOT_PRODUCTION_READY`: yes

## Recommended Next Step

Create a dedicated Entra app registration and ChatGPT draft app using `api://<client-id>/mcp.read`, then rerun the same APIM smoke through that OAuth flow before any direct-ingress or real-index changes.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
