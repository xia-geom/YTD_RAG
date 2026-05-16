# Agent Log: Remote MCP Extended Verification

Date: 2026-05-13
Agent: Codex
Branch: `release/remote-mcp-extended-verification`
Commit: none; working tree HEAD was `e76d995`

## Status Before

The remote MCP server existed as `math_rag.mcp_http_server`. ChatGPT mode exposed
only `search` and `fetch`. A prior APIM/Entra fixture pilot had passed
`/healthz`, `/readyz`, authenticated MCP initialize, `tools/list`, `search`,
`fetch`, and path/secret scans. Direct Container App ingress remained public.

A later low-cost strategy had selected a public/semi-public APIM façade:

```text
ChatGPT Developer Mode app
  -> APIM Consumption /mcp with No Authentication
  -> APIM injects backend bearer token
  -> Container App with MATH_RAG_AUTH_MODE=bearer
  -> read-only fixture or public-safe index
```

## Goal

Run extended verification without changing retrieval, ranking, chunking,
ingestion, downloader, corpus, eval, `.math_rag_index/index.json`, or local
stdio MCP behavior.

## Chosen Path

`PUBLIC-SAFE`

No non-fixture public-safe index was prepared or approved in this sprint. The
live remote endpoint still serves the harmless fixture index only.

## Changes Made

Repository changes in this sprint:

- Created `agent_logs/codex/2026-05-13-extended-verification-scope.md`.
- Created this final extended verification log.

No Azure resources were created, deleted, upgraded, or network-reconfigured in
this sprint.

## Files Intentionally Not Changed

- retrieval/ranking files
- chunking/ingestion/downloader files
- corpus files
- `.math_rag_index/index.json`
- `eval/`
- local stdio MCP behavior
- mathematical candidate/gold evaluation files

## Azure Resources Inspected

Resource group: `rg-math-rag-mcp-test`

Observed resources:

```text
workspace-rgmathragmcptest3QJx  Log Analytics workspace
env-math-rag-mcp-test           Container Apps environment
ca3ae23477c8acr                 ACR Basic
math-rag-mcp-test               Container App
stmathragmcp5d67a258            StorageV2 Standard_LRS
apim-math-rag-mcp-5d67a258      APIM Consumption
```

Container App:

```json
{
  "cpu": 0.5,
  "external": true,
  "fqdn": "math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io",
  "image": "ca3ae23477c8acr.azurecr.io/math-rag-mcp-test:mcp-http-20260512-amd64",
  "ipSecurityRestrictions": null,
  "latestRevisionName": "math-rag-mcp-test--0000002",
  "maxReplicas": 1,
  "memory": "1Gi",
  "minReplicas": 0,
  "runningStatus": "Running",
  "targetPort": 8000
}
```

APIM:

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

Container Apps environment:

```json
{
  "defaultDomain": "bravehill-bd729733.canadacentral.azurecontainerapps.io",
  "internalLoadBalancerEnabled": null,
  "staticIp": "20.116.187.16",
  "vnetConfiguration": null,
  "appLogsConfiguration": {
    "destination": "log-analytics",
    "logAnalyticsConfiguration": {
      "sharedKey": null
    }
  }
}
```

Log Analytics:

```json
{
  "name": "workspace-rgmathragmcptest3QJx",
  "retentionInDays": 30,
  "sku": "PerGB2018"
}
```

ACR tags for `math-rag-mcp-test`:

```text
mcp-http-20260512
mcp-http-20260512-amd64
pilot1
pilot3-amd64
```

## APIM Mode

`NO_AUTH_FACADE_MODE`

Current `/mcp` policy:

```xml
<policies>
  <inbound>
    <base />
    <set-header name="Authorization" exists-action="override">
      <value>Bearer {{math-rag-backend-token}}</value>
    </set-header>
    <rewrite-uri template="/mcp" copy-unmatched-params="true" />
  </inbound>
  <backend>
    <base />
  </backend>
  <outbound>
    <base />
  </outbound>
  <on-error>
    <base />
  </on-error>
</policies>
```

`validate-jwt` is not present. The backend bearer named value is referenced but
its secret value was not printed or retrieved.

APIM APIs:

```text
math-rag-healthz -> /healthz -> direct Container App FQDN
math-rag-readyz  -> /readyz  -> direct Container App FQDN
math-rag-mcp     -> /mcp     -> direct Container App FQDN
```

## Direct Ingress Status

`DIRECT_INGRESS_STILL_PUBLIC_PUBLIC_SAFE_ONLY`

Direct backend checks:

- direct `/healthz`: `200 OK`, fixture counts only
- direct `/readyz`: `200 OK`
- direct unauthenticated `/mcp`: `401 Unauthorized`
- direct wrong-bearer `/mcp initialize`: `401 Unauthorized`

The direct Container App FQDN remains public. App-layer bearer protects `/mcp`,
but a caller with the backend bearer token could bypass APIM. This blocks the
private real index.

## Threat Model

Fixture risk:

- Acceptable for harmless fixture data.
- Public `/healthz` and `/readyz` expose status and counts only.
- Direct `/mcp` requires backend bearer.

Public-safe corpus risk:

- Public reachability can be acceptable only if the index is deliberately
  reviewed as public-safe or semi-public.
- `search` must not return raw text.
- `fetch` must return bounded evidence only.
- No private notes, unpublished material, secrets, personal/admin files, raw
  local paths, PDFs, or raw corpus files should be packaged.

Private real-index risk:

- Not acceptable while direct backend ingress is public.
- Private path requires direct backend bypass to be blocked or an equivalent
  reviewed control.

Security invariants:

```text
search = locate evidence only
fetch = return bounded evidence only
retrieved text = untrusted evidence
LLM synthesis = outside the tool
```

## Data Classification

Allowed in current deployment:

- `HARMLESS_FIXTURE`: `sample_note.md`, `sample_paper.tex`

Not approved in this sprint:

- `PUBLIC_ARXIV_ONLY`
- `PUBLIC_BIBLIOGRAPHIC_ONLY`
- `PUBLIC_SAFE_NOTES`

Denied:

- `PRIVATE_NOTES`
- `UNPUBLISHED_RESEARCH`
- `PERSONAL_OR_ADMIN_DATA`
- `SECRETS`
- raw PDFs
- raw `corpus/`
- `.env`
- full private `.math_rag_index`

Public-safe index status: not prepared and not approved. Stay on fixture index.

## Commands Run

Repository and scope:

```bash
pwd
git branch --show-current
git rev-parse --short HEAD
git status --short
git diff --stat
git diff --name-only
git switch -c release/remote-mcp-extended-verification
git diff --name-only --staged
git diff --name-only -- math_rag/src/math_rag/hybrid_search.py math_rag/src/math_rag/keyword_search.py math_rag/src/math_rag/vector_search.py
git diff --name-only -- corpus/ .math_rag_index eval/
```

Azure inspection:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az account show --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az resource list --resource-group rg-math-rag-mcp-test --query "[].{name:name,type:type,location:location,sku:sku.name}" --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp show --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --query "{...}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp env show --resource-group rg-math-rag-mcp-test --name env-math-rag-mcp-test --query "{...}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim show --resource-group rg-math-rag-mcp-test --name apim-math-rag-mcp-5d67a258 --query "{...}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az containerapp ingress access-restriction list --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az apim api list --resource-group rg-math-rag-mcp-test --service-name apim-math-rag-mcp-5d67a258 --query "[].{name:name,path:path,protocols:protocols,serviceUrl:serviceUrl}" --output json
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az rest --method get --url "<APIM policy ARM URL>" --query properties.value --output tsv
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az acr repository show-tags --name ca3ae23477c8acr --repository math-rag-mcp-test --output table
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az monitor log-analytics workspace show --resource-group rg-math-rag-mcp-test --workspace-name workspace-rgmathragmcptest3QJx --query "{...}" --output json
```

Local and Docker:

```bash
math_rag/.venv/bin/python -m compileall math_rag/src/math_rag/mcp_http_server.py
math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py -q
math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py math_rag/tests/test_remote_mcp_server.py math_rag/tests/test_mcp_server.py -q
math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py
math_rag/.venv/bin/python -m pytest math_rag/tests
docker build -f deploy/azure/Dockerfile -t math-rag-mcp-http:extended-verification .
docker run --rm --entrypoint /bin/sh math-rag-mcp-http:extended-verification -lc 'find /app -maxdepth 5 -type f | sort | head -300'
docker run -d --rm --name math-rag-mcp-extended-smoke ...
curl http://127.0.0.1:8003/healthz
curl -H 'Authorization: Bearer test-secret' ... http://127.0.0.1:8003/mcp
docker stop math-rag-mcp-extended-smoke
```

Remote smoke:

```bash
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/readyz
curl -i -sS https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/healthz
curl -i -sS https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/readyz
curl -i -sS -H 'Accept: application/json, text/event-stream' https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp
curl -i -sS -H 'Authorization: Bearer definitely-not-the-backend-token' ... https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io/mcp
```

## Test Results

Local:

- `compileall mcp_http_server.py`: passed
- `pytest math_rag/tests/test_mcp_http_server.py -q`: `14 passed`
- `pytest test_mcp_http_server.py test_remote_mcp_server.py test_mcp_server.py -q`: `64 passed`
- `deploy/azure/local_remote_mcp_smoke_test.py`: passed
  - fixture sources: `sample_note.md`, `sample_paper.tex`
  - ChatGPT tools: `fetch`, `search`
  - internal tools only in internal mode: `rag_ask`, `rag_get_chunk`,
    `rag_list_sources`, `rag_search`, `rag_stats`
  - search results: `4`
- full `pytest math_rag/tests`: `194 passed in 4.69s`

Docker:

- Docker build: passed
- Image file-list inspection: no `corpus/`, `.math_rag_index`, PDFs, `.env`, or
  secrets observed in `/app`; application package files only
- Docker `/healthz`: passed once with fixture counts
- Docker initialize: passed once and returned `Mcp-Session-Id`
- Docker follow-up protocol calls were unreliable through local Colima
  localhost port forwarding and were not completed
- Container was stopped

APIM:

- `/healthz`: passed when DNS resolved, `200 OK`, fixture counts only
- `/readyz`: previously passed in this run, `200 OK`
- APIM policy verification: passed, current mode is no-auth façade
- APIM extended initialize/tools/list/search/fetch: not completed because this
  environment intermittently failed DNS resolution for
  `apim-math-rag-mcp-5d67a258.azure-api.net`

Direct backend:

- `/healthz`: `200 OK`
- `/readyz`: `200 OK`
- unauthenticated `/mcp`: `401 Unauthorized`
- wrong-bearer `/mcp initialize`: `401 Unauthorized`

## Path / Secret Leak Scan

Successful latest fixture scans from prior APIM smoke and current local/Docker
fixture smoke did not expose forbidden strings in `search`/`fetch` payloads.

Forbidden strings checked included:

```text
/Users/
/home/
/mnt/data/
/private/tmp/
file://
corpus/arxiv
corpus/my_notes
.math_rag_index
OPENAI_API_KEY
MATH_RAG_API_TOKEN
MATH_RAG_API_KEY
AZURE_
mathragapitoken
math-rag-backend-token
Bearer
sk-
.env
```

New post-change APIM `tools/list`/`search`/`fetch` payload scan could not be
completed because APIM MCP protocol smoke was blocked by intermittent DNS.

No secrets were printed.

## Cost / Quota Findings

Current cost surfaces:

- Container Apps active/idle CPU, memory, and request meters
- ACR Basic daily registry cost and stored image layers
- Standard LRS storage / Azure Files operations
- Log Analytics ingestion and 30-day retention
- APIM Consumption calls
- bandwidth/egress
- unexpected public traffic to APIM no-auth façade

Cost controls currently verified:

- Container App min replicas `0`
- max replicas `1`
- APIM SKU `Consumption`
- no private endpoint, VNet, premium SKU, or always-on resource added
- backend `fetch` and `search` caps remain in server config

Cleanup command, not run:

```bash
AZURE_CONFIG_DIR=/private/tmp/azure-cli-config az group delete --name rg-math-rag-mcp-test --yes --no-wait
```

## ChatGPT Draft App Result

Not run in this Codex session. The expected ChatGPT Developer Mode configuration
for the public-safe fixture pilot is:

```text
URL: https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
Authentication: No Authentication
Expected tools: search, fetch
Test query: Remote MCP Test Note
```

## Current Status After Task

- `SAFE_FOR_LOCAL_DEV`: yes
- `SAFE_FOR_DOCKER_FIXTURE`: partial
- `SAFE_FOR_APIM_FIXTURE`: partial, because APIM health and policy are verified
  but post-change APIM MCP protocol smoke is blocked by DNS instability
- `SAFE_FOR_LOW_COST_PUBLIC_SAFE_INDEX`: no, because no non-fixture public-safe
  index was classified or approved
- `SAFE_FOR_PRIVATE_REAL_INDEX`: no
- `NOT_SAFE_FOR_PRIVATE_REAL_INDEX`: yes
- `NOT_PRODUCTION_READY`: yes
- `CLEANUP_RECOMMENDED`: yes when not actively testing

## Known Limitations

- APIM public DNS resolution was intermittent from this local environment.
- Post-change APIM MCP initialize/tools/search/fetch was not completed.
- Docker full protocol smoke was partial due intermittent localhost port
  connectivity through Colima.
- No ChatGPT draft app was created or tested.
- No public-safe non-fixture index was prepared.
- Direct Container App ingress remains public.

## Recommended Next Step

From a stable network, create a ChatGPT Developer Mode connector using the APIM
URL with No Authentication, verify `tools/list` shows exactly `search` and
`fetch`, then run one fixture `search`/`fetch` and path/secret scan.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
