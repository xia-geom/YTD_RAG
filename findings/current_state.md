# Current State

Date: 2026-05-15
Branch: `release/remote-mcp-extended-verification`
HEAD at inspection: `e76d995`

## Scope

This is the fixture/public-safe connector lane only. No corpus, eval,
retrieval, ranking, chunking, ingestion, downloader, private index, or local
stdio MCP behavior was changed.

## Repository State

The working tree is dirty from earlier connector, deployment, docs, and
retrieval/ranking work. The unrelated retrieval/ranking files remain outside
this finalization scope:

- `math_rag/src/math_rag/hybrid_search.py`
- `math_rag/src/math_rag/keyword_search.py`
- `math_rag/src/math_rag/vector_search.py`
- `math_rag/tests/test_hybrid_search.py`

The relevant connector entrypoints are:

- `math_rag/src/math_rag/mcp_http_server.py`: current Streamable HTTP remote
  MCP server.
- `math_rag/src/math_rag/mcp_server.py`: existing local stdio MCP server.
- `math_rag/src/math_rag/remote_mcp_server.py`: legacy remote adapter, not the
  current APIM fixture endpoint.

## Tool Surface

Current remote HTTP server modes:

- `MATH_RAG_TOOL_MODE=chatgpt`: `search`, `fetch`
- `MATH_RAG_TOOL_MODE=internal`: read-only `rag_*` tools
- `MATH_RAG_TOOL_MODE=all`: `search`, `fetch`, plus safe read-only `rag_*`

The live APIM fixture preflight observed exactly:

```text
search
fetch
```

## Auth State

The current low-cost fixture lane uses:

```text
ChatGPT Developer Mode app
  -> APIM /mcp with No Authentication
  -> APIM injects backend auth header
  -> Container App with app-layer bearer auth
  -> harmless fixture index
```

Python OAuth/JWT validation is not implemented in the app. OpenAI Apps SDK docs
say authenticated MCP servers are expected to use OAuth 2.1, and the resource
server must verify access tokens. That is a private-lane requirement, not a
fixture-lane blocker.

## Verification Result

The deterministic fixture verifier passed:

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

The only remaining fixture-lane proof gap is manual ChatGPT Developer Mode UI
evidence.

## LMFDB MCP Comparison

The `AndrewVSutherland/lmfdb-mcp` reference is much simpler because it exposes a
public read-only PostgreSQL mirror with public default credentials. Its README
documents unauthenticated Cloud Run deployment and a broad SQL-style tool
surface (`overview`, `list_tables`, `describe_table`, `run_sql`,
`export_query`, etc.).

That is useful as an ergonomics reference, but not as a private-index security
template. The math RAG connector has to sanitize local index metadata, preserve
the `search`/`fetch` public surface, avoid path/secret leaks, and keep private
index rollout blocked until backend bypass is solved.

## Handoff

Status: fixture APIM preflight is good; ChatGPT UI transcript is still missing;
private real index remains blocked.
