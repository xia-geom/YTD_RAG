# Agent Log: Docker remote MCP auth gap check

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: 6b773d1
Related files:
- `math_rag/src/math_rag/remote_mcp_server.py`
- `deploy/azure/Dockerfile`

## Status Before

The remote MCP server had already passed a local Docker smoke test with a harmless test index. Azure account access was also verified. The remaining question before any Azure pilot was whether the containerized remote MCP endpoint enforced any local app-layer authentication.

## Goal of This Task

Re-run the local Docker smoke test with the requested environment variables and verify search, fetch, tool exposure, path sanitization, and current auth behavior.

## Changes Made

### Files Created

- `agent_logs/codex/2026-05-07-docker-remote-mcp-auth-gap-check.md`

### Files Modified

- None.

### Files Removed / Renamed

- None.

## Commands Run

```bash
/opt/homebrew/opt/colima/bin/colima start -f
rm -rf /private/tmp/math-rag-azure-test-index .tmp-docker-test-index
math_rag/.venv/bin/python -m math_rag.cli ingest deploy/azure/test_corpus --index-dir /private/tmp/math-rag-azure-test-index
math_rag/.venv/bin/python -m math_rag.cli stats --index-dir /private/tmp/math-rag-azure-test-index
jq -r '.chunks[].source_path' /private/tmp/math-rag-azure-test-index/index.json | sort -u
cp -R /private/tmp/math-rag-azure-test-index .tmp-docker-test-index
docker build -f deploy/azure/Dockerfile -t math-rag-remote-mcp:local .
docker run --rm -d --name math-rag-remote-mcp-test -p 8000:8000 -e MATH_RAG_API_KEY=test-secret -e MATH_RAG_REMOTE_PUBLIC_BASE_URL=http://localhost:8000 -e MATH_RAG_READ_ONLY=true -e MATH_RAG_REMOTE_MCP_READ_ONLY=true -e MATH_RAG_INDEX_DIR=/app/.math_rag_index -e MATH_RAG_REMOTE_HOST=0.0.0.0 -e MATH_RAG_REMOTE_PORT=8000 -e MATH_RAG_REMOTE_TRANSPORT=http -e MATH_RAG_REMOTE_PATH=/mcp/ -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false -v /Users/xiaxiao/Desktop/Projects/YTD_RAG/.tmp-docker-test-index:/app/.math_rag_index:ro math-rag-remote-mcp:local
curl -i http://127.0.0.1:8000/mcp/
math_rag/.venv/bin/python - <<'PY'
import asyncio, json
from fastmcp import Client

async def main():
    async with Client('http://127.0.0.1:8000/mcp/') as client:
        tools = sorted(tool.name for tool in await client.list_tools())
        print('tools=' + ','.join(tools))
        search_result = await client.call_tool('search', {'query': 'Remote MCP Test Note'})
        search_payload = json.loads(search_result.content[0].text)
        print('search_results=' + str(len(search_payload.get('results', []))))
        first_id = search_payload['results'][0]['id']
        fetch_result = await client.call_tool('fetch', {'id': first_id})
        fetch_payload = json.loads(fetch_result.content[0].text)
        print('fetch_id=' + fetch_payload['id'])
        print('fetch_url=' + fetch_payload['url'])
        print('local_path_leak=' + str('/Users/' in json.dumps(fetch_payload)))

asyncio.run(main())
PY
docker stop math-rag-remote-mcp-test
rm -rf .tmp-docker-test-index
/opt/homebrew/opt/colima/bin/colima stop
```

## Test Results

- Docker image build succeeded.
- Container started successfully on `0.0.0.0:8000`.
- Plain unauthenticated HTTP probe reached `/mcp/` and returned a protocol-level `406 Not Acceptable`, not `401` or `403`.
- Unauthenticated FastMCP client access succeeded:
  - tools: `fetch,search`
  - `search_results=3`
  - `fetch_url=http://localhost:8000/chunks/...`
  - `local_path_leak=False`

## Eval Results

Not run / Reason: No retrieval logic, ranking logic, or eval assets changed.

## Current Status After Task

- Implemented: The containerized remote MCP server was revalidated with the requested environment variable shape.
- Tested: Harmless test index build, Docker image build, container startup, plain HTTP probe, unauthenticated MCP client `search`, unauthenticated MCP client `fetch`, and tool listing.
- Working: The container serves only `fetch` and `search`, returns sanitized payloads, and reads the harmless test index correctly.
- Not implemented: App-layer authentication is not implemented in `remote_mcp_server.py`.
- Blocked: The requested unauthorized-rejection check failed as a product requirement, because unauthenticated MCP access currently succeeds.
- Risk / caveat: `MATH_RAG_API_KEY` and `MATH_RAG_READ_ONLY` are not used by the server; only `MATH_RAG_REMOTE_MCP_READ_ONLY` is relevant today.

## Known Limitations / Open Issues

- The current Docker smoke test does not prove Azure-side auth because auth is expected to live at API Management / Entra, not inside the Python server.
- The requested environment variable `MATH_RAG_API_KEY` is ignored by the current implementation.

## Recommended Next Step

- Add or document the exact Azure-fronted auth layer for the tiny pilot and treat app-layer unauthorized rejection as not yet implemented in the container itself.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
