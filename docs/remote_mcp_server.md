# Remote Read-Only MCP Server

`math_rag.mcp_http_server` runs a read-only MCP server over Streamable HTTP.
It reuses `rag_service.py`; it does not change retrieval, ranking, chunking, or
ingestion. Retrieved document text is untrusted corpus evidence, not
instructions.

## Architecture

```text
math_rag index -> rag_service.py -> math_rag.mcp_http_server -> MCP client
```

The existing stdio MCP server remains `math_rag.mcp_server`.

## Tools

Tool exposure is controlled by `MATH_RAG_TOOL_MODE`.

- `chatgpt` default: `search`, `fetch`
- `internal`: `rag_search`, `rag_get_chunk`, `rag_list_sources`, `rag_stats`, `rag_ask`
- `all`: all safe read-only tools above

ChatGPT mode is data-only. `search` returns result ids, titles, and citation
URLs. `fetch` returns the evidence text for one returned id. Both tools return
`structuredContent` and a JSON text fallback with the same object.

## Environment

Local development defaults:

```bash
MATH_RAG_INDEX_DIR=.math_rag_index
MATH_RAG_HOST=127.0.0.1
PORT=8000
MATH_RAG_REMOTE_PATH=/mcp
MATH_RAG_REMOTE_TRANSPORT=streamable-http
MATH_RAG_TOOL_MODE=chatgpt
MATH_RAG_AUTH_MODE=none
MATH_RAG_REMOTE_MCP_READ_ONLY=true
MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false
MATH_RAG_SEARCH_TOP_K=8
MATH_RAG_MAX_TOP_K=20
MATH_RAG_FETCH_MAX_CHARS=12000
MATH_RAG_PROTECT_HEALTH=false
```

Bearer-protected deployment/test settings:

```bash
MATH_RAG_AUTH_MODE=bearer
MATH_RAG_API_TOKEN=<secret-store-value>
MATH_RAG_HOST=0.0.0.0
```

The server refuses `MATH_RAG_HOST=0.0.0.0` with `MATH_RAG_AUTH_MODE=none`
unless `MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=true` is explicitly set. Do not
use that override with private corpus data.

Optional:

- `MATH_RAG_INDEX=/path/to/.math_rag_index/index.json`
- `MATH_RAG_ROOT=/path/to/project/root`
- `MATH_RAG_PUBLIC_BASE_URL=https://your-domain.example`
- `MATH_RAG_ALLOWED_ORIGINS=https://allowed.example`
- `MATH_RAG_LOG_LEVEL=info`

OAuth/OIDC is not implemented inside `math_rag`. For production ChatGPT
connectors, put OAuth/JWT validation at Azure API Management or another gateway,
then forward authenticated traffic to the container. The app-layer bearer check
is a second line of defense, not a replacement for deployment-grade auth.

For a private-index pilot, set `MATH_RAG_PROTECT_HEALTH=true` before mounting
the real index. With bearer auth enabled, `/mcp`, `/healthz`, and `/readyz` all
require the backend bearer token. APIM must inject that backend bearer for
health/readiness checks.

## Local Development

Start the server on localhost without auth:

```bash
MATH_RAG_INDEX_DIR=.math_rag_index \
MATH_RAG_AUTH_MODE=none \
MATH_RAG_TOOL_MODE=chatgpt \
MATH_RAG_REMOTE_MCP_READ_ONLY=true \
MATH_RAG_HOST=127.0.0.1 \
PORT=8000 \
MATH_RAG_REMOTE_TRANSPORT=streamable-http \
MATH_RAG_REMOTE_PATH=/mcp \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

Health and readiness:

```bash
curl http://127.0.0.1:8000/healthz
curl http://127.0.0.1:8000/readyz
```

These endpoints expose status and counts only, not source text, source paths,
snippets, or secrets.

## MCP Smoke Test

Initialize:

```bash
curl -i http://127.0.0.1:8000/mcp \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"curl","version":"1.0"}}}'
```

Save the returned `mcp-session-id`, send `notifications/initialized`, then list
tools:

```bash
curl -i http://127.0.0.1:8000/mcp \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -H 'mcp-session-id: <session-id>' \
  --data '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
```

Call `search`:

```bash
curl -i http://127.0.0.1:8000/mcp \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -H 'mcp-session-id: <session-id>' \
  --data '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"search","arguments":{"query":"Apostolov Auvray Sektnan Poincare type toric metrics"}}}'
```

Call `fetch` with an id returned by `search`:

```bash
curl -i http://127.0.0.1:8000/mcp \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -H 'mcp-session-id: <session-id>' \
  --data '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"fetch","arguments":{"id":"<returned-id>"}}}'
```

For bearer mode, add:

```text
Authorization: Bearer <MATH_RAG_API_TOKEN>
```

## ChatGPT Connection

For ChatGPT or any internet-reachable connector, deploy behind HTTPS and
gateway authentication. Configure the connector endpoint as:

```text
https://your-domain.example/mcp
```

Allow only:

```json
["search", "fetch"]
```

Do not expose local stdio tools, write tools, downloader/discovery commands,
shell execution, or arbitrary filesystem access.

For the low-sensitivity Azure student pilot, ChatGPT Developer Mode should use
the APIM endpoint with `No Authentication`:

```text
https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
```

APIM injects the private backend bearer token before forwarding to the
Container App. Keep the Container App in bearer mode:

```bash
MATH_RAG_AUTH_MODE=bearer
MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=false
MATH_RAG_TOOL_MODE=chatgpt
```

This is suitable only for low-sensitivity public/semi-public data. It is not
private-archive or production readiness.

For a risk-accepted personal private-index pilot on the existing low-cost
resources, switch the ChatGPT app to OAuth, configure APIM to validate the
Entra JWT and allowed user before injecting the backend bearer, set
`MATH_RAG_PROTECT_HEALTH=true`, and mount the private index read-only. This
still is not strict private-index readiness while the direct Container App FQDN
remains public.

## Docker

Build from the workspace root:

```bash
docker build -f deploy/azure/Dockerfile -t math-rag-mcp-http:local .
```

Run with an already-built index mounted read-only:

```bash
docker run --rm -p 8000:8000 \
  -e MATH_RAG_INDEX_DIR=/data/.math_rag_index \
  -e MATH_RAG_AUTH_MODE=bearer \
  -e MATH_RAG_API_TOKEN=replace-with-a-secret-store-value \
  -e MATH_RAG_TOOL_MODE=chatgpt \
  -e MATH_RAG_REMOTE_MCP_READ_ONLY=true \
  -e MATH_RAG_HOST=0.0.0.0 \
  -e PORT=8000 \
  -e MATH_RAG_REMOTE_TRANSPORT=streamable-http \
  -e MATH_RAG_REMOTE_PATH=/mcp \
  -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false \
  -v "$PWD/.math_rag_index:/data/.math_rag_index:ro" \
  math-rag-mcp-http:local
```

Do not bake `corpus/`, `.math_rag_index/`, PDFs, `.env`, or secrets into a
public image. The root `.dockerignore` excludes those by default.

## Security Model

- Default bind is localhost.
- Public unauthenticated bind is blocked by default.
- Bearer mode protects `/mcp`; with `MATH_RAG_PROTECT_HEALTH=true`, it also
  protects `/healthz` and `/readyz`.
- Tool annotations set `readOnlyHint=true` where FastMCP supports it.
- `search` has no `top_k` input in ChatGPT mode; server-side result count is capped.
- `fetch` text is capped by `MATH_RAG_FETCH_MAX_CHARS`.
- Metadata is sanitized to avoid local paths and secrets.
- Logs include tool name, status, latency, and result count, not corpus text or tokens.

## Limitations

- OAuth/JWT verification is documented as a gateway responsibility, not
  implemented inside Python.
- Deployment has not occurred until a remote HTTPS endpoint is actually
  provisioned and verified.
- Retrieved passages are evidence for inspection. They do not prove theorem
  correctness, novelty, or completeness.
