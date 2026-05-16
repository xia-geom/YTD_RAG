# Public-Safe ChatGPT MCP Final Sprint

## Date

2026-05-16

## Agent

Codex

## Branch

`codex/private-index-risk-accepted-pilot`

## Commit

`395fc9c`

## Status Before

- Live APIM endpoint was verified for fixture-only MCP mechanics.
- Current live data was the harmless fixture index.
- User requested replacing fixture data with a public-safe research index.
- User explicitly reclassified relative `corpus/my_notes` provenance as public
  knowledge for this sprint.

## Goal

Deploy an audited public-safe index behind the existing APIM Consumption MCP
endpoint while preserving ChatGPT `search`/`fetch` mode and backend bearer auth.

## Scope Guard

- No raw `corpus/`, PDFs, `.env`, or secrets deployed.
- No retrieval, ranking, chunking, ingestion, downloader, eval, or local stdio
  MCP behavior changes.
- No Azure secrets printed.
- APIM remains the ChatGPT-facing endpoint.

## Commands Run

- `pwd`
- `git branch --show-current`
- `git rev-parse --short HEAD`
- `git status --short`
- Protected-path `git diff --name-only`
- Python JSON load and index shape checks
- `rg` forbidden-marker scans against `.math_rag_index`
- Local `search_payload` / `fetch_payload` checks for five math queries
- Azure account and Container App inspection
- Azure Files share create: `math-rag-public-safe-index`
- Azure Files upload of only `index.json`
- Container Apps environment storage registration with `ReadOnly` access mode
- Container App update to mount `math-rag-public-safe-index`
- Container App revision readiness checks
- APIM `/healthz` and `/readyz`
- APIM MCP initialize, initialized notification, `tools/list`, search/fetch
  matrix
- Direct backend unauthenticated and wrong-bearer negative controls
- Payload forbidden-marker scan over `.tmp-public-safe-verify/`

## Index Audit

GO_INDEX_PUBLIC_SAFE=true

- `index.json`: 57,457,360 bytes
- chunks: 18,544
- distinct source paths: 104
- `corpus/arxiv`: 18,274 chunks
- `corpus/my_notes`: 270 chunks, accepted by user as public-safe
- no absolute local paths or secret markers after reclassification

Review notes:

- `unpublished` appears in public citation/prose contexts.
- `sk-` appears inside TeX/math tokens, not API keys.

## Azure Deployment

GO_AZURE_PUBLIC_SAFE_DEPLOYED=true

- New share: `math-rag-public-safe-index`
- Uploaded file: `index.json` only
- Active revision: `math-rag-mcp-test--0000003`
- Mounted storage: `math-rag-public-safe-index`
- Mount path: `/data/.math_rag_index`
- APIM health: 18,544 chunks / 104 sources

## MCP Protocol Test

GO_MCP_PUBLIC_SAFE=true

- Tool surface: exactly `search`, `fetch`
- Five of five math queries returned results
- Fetch succeeded for top result of each query
- Search/fetch schemas passed
- SSE/JSON fallback equivalence passed

## Payload / Secret Scan

GO_PAYLOAD_SAFE=true

No hard forbidden markers were found in APIM response artifacts under
`.tmp-public-safe-verify/`.

## ChatGPT Operator Result

Pending. The ChatGPT web UI Draft app check was not run in this environment.

## Direct Backend Status

- `/healthz`: public, 200
- `/readyz`: public, 200
- `/mcp` without bearer: 401
- `/mcp` with wrong bearer: 401

This remains public-safe only, not private-secret-index ready.

## Go / No-Go

GO_PUBLIC_SAFE_APIM_MCP_ENDPOINT=true

GO_PUBLIC_SAFE_CHATGPT_CONNECTOR=false until the manual ChatGPT Developer Mode
check is captured.

SAFE_FOR_PUBLIC_SAFE_ARXIV_RESEARCH=true

SAFE_FOR_PRIVATE_SECRET_INDEX=false

## Known Limitations

- Search latency through APIM is about 30-32 seconds per query on the larger
  JSON index.
- Direct Container App health/readiness are publicly reachable.
- The current architecture uses APIM No Authentication for ChatGPT and is not a
  private archive design.

## Rollback

Change the Container App template volume `storageName` from
`math-rag-public-safe-index` back to `math-rag-fixture-index`, then rerun APIM
health/readiness and MCP smoke tests.

## Recommended Next Step

Run the manual ChatGPT Developer Mode connector check and save a sanitized
transcript.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
