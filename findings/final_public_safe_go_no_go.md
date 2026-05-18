# Final Public-Safe MCP Go / No-Go

Date: 2026-05-16

Pause update: on 2026-05-18 the remote MCP service was paused by disabling
Container App ingress for `math-rag-mcp-test`. The APIM endpoint is preserved
but is not currently a usable live connector. See
`agent_logs/codex/2026-05-18-remote-mcp-paused.md`.

## Decision

GO_PUBLIC_SAFE_CHATGPT_CONNECTOR=false

GO_PUBLIC_SAFE_APIM_MCP_ENDPOINT=true

SAFE_FOR_PUBLIC_SAFE_ARXIV_RESEARCH=true

SAFE_FOR_PRIVATE_SECRET_INDEX=false

## Summary

The public-safe research index was deployed behind the existing APIM MCP
endpoint during the 2026-05-16 verification. APIM health reported 18,544 chunks
and 104 sources. MCP protocol tests passed, the ChatGPT-visible tool surface
remained exactly `search` and `fetch`, all five required math queries returned
results, and APIM payload scans passed.

The final ChatGPT web UI Draft app gate is still pending, so the stricter
`GO_PUBLIC_SAFE_CHATGPT_CONNECTOR` value remains false until a manual ChatGPT
transcript or screenshots are captured.

## What Changed

- Created Azure Files share `math-rag-public-safe-index`.
- Uploaded only `.math_rag_index/index.json`.
- Registered the share as read-only Container Apps environment storage.
- Updated Container App `math-rag-mcp-test` to mount that storage at
  `/data/.math_rag_index`.

## What Index Is Deployed

The deployed index is the audited public-safe `.math_rag_index/index.json`.
It contains 18,544 chunks and 104 source paths. The user explicitly
reclassified relative `corpus/my_notes` provenance as public-safe.

## Tool Surface Observed

Exactly:

- `search`
- `fetch`

No `rag_*` tools and no write tools were observed through APIM.

## Example Successful Math Query

Query:

`Apostolov Auvray Sektnan Poincare type toric metrics`

Top result:

- `Extremal Kähler Poincaré type metrics on toric varieties`
- `https://arxiv.org/abs/1711.08424`

Fetch returned bounded evidence text and sanitized metadata.

## Payload Scan Result

GO_PAYLOAD_SAFE=true

No hard forbidden markers were found in `.tmp-public-safe-verify/`.

## ChatGPT Operator Result

Pending. Use Developer Mode with:

`https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp`

Auth mode:

`No Authentication`

## Remaining Risks

- The direct Container App backend remains publicly reachable.
- Direct `/mcp` still requires backend bearer auth, but this architecture is not
  suitable for private secret indexes.
- Search latency through APIM is about 30-32 seconds per query on the larger
  JSON index.
- The ChatGPT UI gate is not complete.

## Cost / Cleanup Note

This adds one Azure Files share containing a roughly 55 MB `index.json`. The
Container App remains Consumption with min replicas 0 / max replicas 1, but
ingress is now disabled. Costs should remain low for light use, but storage,
logs, registry storage, APIM metadata/calls, bandwidth, and unexpected traffic
may cost money.

## Rollback Plan

Restore the fixture deployment by changing the Container App template volume
storage from `math-rag-public-safe-index` back to `math-rag-fixture-index`, then
verify APIM `/healthz`, `/readyz`, initialize, `tools/list`, `search`, and
`fetch`.
