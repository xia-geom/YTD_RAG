# Agent Log: MCP Connector Finalization

Date: 2026-05-15
Agent: Codex
Branch: `release/remote-mcp-extended-verification`
Commit: pending; HEAD before commit was `e76d995`

## Status Before

The fixture APIM connector was already implemented and had a deterministic
verification harness. The remaining gap was manual ChatGPT Developer Mode UI
proof. Private real-index rollout was blocked by public direct Container App
ingress and lack of OAuth/JWT validation.

## Goal

Produce final `findings/` artifacts, rerun fixture verification, inspect Azure
APIM/Container App state, compare against `lmfdb-mcp`, and leave a commit if the
new finalization artifacts are cleanly scoped.

## Scope Guard

No retrieval, ranking, chunking, ingestion, downloader, corpus, eval, private
index, `.math_rag_index/index.json`, or local stdio MCP behavior was changed.

## Files Created

- `findings/current_state.md`
- `findings/apim_policy.md`
- `findings/chatgpt_runbook.md`
- `findings/security_scan.md`
- `findings/private_lane.md`
- `findings/summary.md`
- `findings/final_prompt.txt`
- `agent_logs/codex/2026-05-15-mcp-connector-finalization.md`

## Commands Run

Repository:

```bash
git rev-parse --show-toplevel
git status --short
rg -n "mcp_http_server|remote_mcp_server|FastMCP|search\(|fetch\(|rag_(ask|get_chunk|list_sources|search|stats)|MATH_RAG_AUTH_MODE|MATH_RAG_API_TOKEN|MATH_RAG_API_KEY|MATH_RAG_TOOL_MODE|ALLOW_UNAUTHENTICATED" .
rg -n "(OPENAI_API_KEY|MATH_RAG_API_TOKEN|MATH_RAG_API_KEY|AZURE_|sk-[A-Za-z0-9]|Bearer[[:space:]]+[A-Za-z0-9._-]+|connectionString|AccountKey|SharedAccessSignature)" .
```

Reference implementation:

```bash
curl -L -sS https://raw.githubusercontent.com/AndrewVSutherland/lmfdb-mcp/main/README.md
curl -L -sS https://raw.githubusercontent.com/AndrewVSutherland/lmfdb-mcp/main/server.py
curl -L -sS https://raw.githubusercontent.com/AndrewVSutherland/lmfdb-mcp/main/Dockerfile
```

Fixture verifier:

```bash
math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
  --input deploy/azure/fixture_connector_verification/input/verification_input.json \
  --output-dir .tmp-fixture-verify
```

Azure inspection:

```bash
AZURE_CONFIG_DIR=<azure-cli-config> az containerapp show --resource-group rg-math-rag-mcp-test --name math-rag-mcp-test --query "{external:properties.configuration.ingress.external,fqdn:properties.configuration.ingress.fqdn,ipSecurityRestrictions:properties.configuration.ingress.ipSecurityRestrictions,targetPort:properties.configuration.ingress.targetPort}" --output json
AZURE_CONFIG_DIR=<azure-cli-config> az apim show --resource-group rg-math-rag-mcp-test --name apim-math-rag-mcp-5d67a258 --query "{gatewayUrl:gatewayUrl,sku:sku.name,publicNetworkAccess:publicNetworkAccess,virtualNetworkType:virtualNetworkType}" --output json
AZURE_CONFIG_DIR=<azure-cli-config> az apim api list --resource-group rg-math-rag-mcp-test --service-name apim-math-rag-mcp-5d67a258 --query "[].{name:name,path:path,serviceUrl:serviceUrl}" --output table
AZURE_CONFIG_DIR=<azure-cli-config> az rest --method get --url "<APIM policy ARM URL>" --query properties.value --output tsv
```

Endpoint checks:

```bash
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/readyz
```

Payload scan:

```bash
rg -n '(/Users/|/home/|/mnt/data/|/private/tmp/|file://|corpus/arxiv|corpus/my_notes|\.math_rag_index|OPENAI_API_KEY|MATH_RAG_API_TOKEN|MATH_RAG_API_KEY|AZURE_|mathragapitoken|math-rag-backend-token|Bearer |sk-|\.env)' .tmp-fixture-verify
```

## Test Results

Fixture verifier:

```json
{
  "decision": "blocked_pending_operator",
  "preflight_overall": "pass",
  "manual_chatgpt_status": "blocked",
  "tool_names_observed": ["search", "fetch"],
  "search_result_count": 4,
  "fetch_text_length": 287,
  "fetch_max_chars": 12000,
  "secret_scan_status": "pass",
  "secret_scan_hits": [],
  "private_real_index_status": "blocked_not_tested"
}
```

Payload scan:

```text
no matches
```

APIM health:

```text
200 OK, read_only=true, tool_mode=chatgpt, tool_count=2, chunk_count=4, source_count=2
```

APIM readiness:

```text
200 OK, read_only=true, tool_mode=chatgpt, index_present=true
```

Full package tests were not rerun in this pass because no package code was
changed.

## Azure Status

Container App remains externally reachable:

```json
{
  "external": true,
  "ipSecurityRestrictions": null,
  "targetPort": 8000
}
```

APIM remains public Consumption without VNet integration:

```json
{
  "sku": "Consumption",
  "publicNetworkAccess": "Enabled",
  "virtualNetworkType": "None"
}
```

The live `/mcp` policy is No Auth at APIM, injects a backend auth header from a
named value, and rewrites to `/mcp`. The named-value secret was not printed.

## Current Decision

`SAFE_FOR_APIM_FIXTURE`: yes

`SAFE_FOR_CHATGPT_DEVELOPER_TEST`: blocked pending manual ChatGPT UI transcript

`SAFE_FOR_PRIVATE_REAL_INDEX`: no

`NOT_PRODUCTION_READY`: yes

## Recommended Next Step

Create the ChatGPT Developer Mode app with the APIM `/mcp` URL, choose No
Authentication, confirm exactly `search` and `fetch`, save a sanitized
transcript, and rerun the verifier with `--manual-transcript`.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
