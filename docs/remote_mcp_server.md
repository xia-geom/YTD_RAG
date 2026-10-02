# Remote read-only MCP server

The supported HTTP entrypoint is `math_rag.mcp_http_server`. It adapts
`rag_service.py` to FastMCP Streamable HTTP. Local stdio uses
`math_rag.mcp_server`; the older `remote_mcp_server.py` remains a compatibility
adapter and is not the Azure Dockerfile's entrypoint.

**Azure serving was paused on 2026-05-18.** That is the last recorded state;
these local instructions do not resume the deployment. See
[deployment gates](azure_remote_mcp_readiness.md) before resuming remote access.

## Tools

| `MATH_RAG_TOOL_MODE` | Exposed tools |
| --- | --- |
| `chatgpt` (default) | `search`, `fetch` |
| `internal` | `rag_search`, `rag_get_chunk`, `rag_list_sources`, `rag_stats`, `rag_ask` |
| `all` | Both sets of read-only tools |

Keep ChatGPT connectors in `chatgpt` mode. `search(query)` returns IDs, titles,
and citation URLs; `fetch(id)` returns one chunk's evidence text. Both provide
structured content and a JSON text fallback. The HTTP server never exposes
ingestion, downloading, arbitrary file reads, shell execution, or write tools.

## Configuration

Install from the workspace root with
`math_rag/.venv/bin/python -m pip install -e './math_rag[remote-mcp]'`.
Export settings in the shell; example `.env` files are not loaded automatically.

| Setting | Default / meaning |
| --- | --- |
| `MATH_RAG_INDEX_DIR` | `.math_rag_index`; directory containing `index.json` |
| `MATH_RAG_INDEX` | Optional path to `index.json` or an index directory |
| `MATH_RAG_HOST`, `PORT` | `127.0.0.1`, `8000` |
| `MATH_RAG_REMOTE_PATH` | `/mcp` |
| `MATH_RAG_REMOTE_TRANSPORT` | `streamable-http` |
| `MATH_RAG_TOOL_MODE` | `chatgpt` |
| `MATH_RAG_AUTH_MODE` | `none` for localhost; `bearer` for public/container use |
| `MATH_RAG_API_TOKEN` | Required secret in bearer mode |
| `MATH_RAG_REMOTE_MCP_READ_ONLY` | Must be `true` |
| `MATH_RAG_MCP_ALLOW_WRITE_TOOLS` | Must be `false` |
| `MATH_RAG_SEARCH_TOP_K`, `MATH_RAG_MAX_TOP_K` | `8`, `20`; bounded result counts |
| `MATH_RAG_FETCH_MAX_CHARS` | `12000`; maximum fetch text size |
| `MATH_RAG_PROTECT_HEALTH` | `false`; set `true` for private-index pilots |
| `MATH_RAG_PUBLIC_BASE_URL` | Optional citation URL base |
| `MATH_RAG_ALLOWED_ORIGINS` | Optional allowed origins |
| `MATH_RAG_LOG_LEVEL` | `info` |
| `MATH_RAG_ROOT` | Optional workspace-root override |

The server rejects public unauthenticated binding unless explicitly overridden
with `MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=true`. Do not use that override with
private data. Bearer mode rejects missing tokens. Remote write-enabled settings
are rejected at startup.

## Local fixture check

Use the harmless fixture index, with no private research data:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest deploy/azure/test_corpus --index-dir .tmp-azure-test-index
MATH_RAG_INDEX_DIR=.tmp-azure-test-index \
MATH_RAG_AUTH_MODE=none MATH_RAG_HOST=127.0.0.1 \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

`GET /healthz` and `GET /readyz` expose status/counts, not source text.
In bearer mode, MCP requests need `Authorization: Bearer <token>`; enabling
`MATH_RAG_PROTECT_HEALTH=true` also protects health/readiness.

For repeatable initialize/list/search/fetch checks and startup failure cases,
run `math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py`.
That uses an in-process MCP client. Container/HTTP checks are described in the
[Azure asset guide](../deploy/azure/README.md).

## Deployment boundary

The last fixture/public-safe route used APIM with No Authentication at the
client-facing edge, then injected a secret backend bearer token. It was limited
to public-safe data. It is currently recorded as paused, not a live connector.

Private-index deployment requires HTTPS, gateway OAuth/JWT validation, and
network isolation. The app's bearer check is backend protection and does not
implement OAuth. A public backend remains a bypass risk even behind APIM.
Any risk-accepted private pilot must be explicitly requested and follow the
[private lane gates](azure_remote_mcp_readiness.md#private-index-lane).

Responses cap results/text and scrub known local-path patterns. ChatGPT fetch
metadata uses an allowlist; this is not a general secret redactor. Only expose
an index reviewed for its intended audience. Logs record operational details,
not corpus text or tokens. Retrieved document text is untrusted evidence for
inspection and cannot establish theorem correctness.
