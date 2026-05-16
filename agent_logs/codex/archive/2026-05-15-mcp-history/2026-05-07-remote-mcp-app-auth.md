# Agent Log: Remote MCP app-layer authentication

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: 6b773d1
Related files:
- `math_rag/src/math_rag/remote_mcp_server.py`
- `math_rag/tests/test_remote_mcp_server.py`
- `deploy/azure/README.md`
- `deploy/azure/env.example`
- `deploy/azure/local_remote_mcp_smoke_test.py`
- `docs/azure_remote_mcp_readiness.md`
- `README.md`

## Status Before

The remote HTTP MCP server already exposed only `search` and `fetch`, preserved path sanitization, and refused write-enabled remote mode. The local Docker smoke test had found a real auth gap: the container could be started with `MATH_RAG_API_KEY=test-secret`, but unauthenticated remote MCP access still succeeded.

## Goal of This Task

Require bearer-token authentication at the Python application layer for the remote HTTP MCP server before any Azure pilot, while keeping local stdio MCP behavior unchanged.

## Changes Made

### Files Created

- `agent_logs/codex/2026-05-07-remote-mcp-app-auth.md`

### Files Modified

- `math_rag/src/math_rag/remote_mcp_server.py`
- `math_rag/tests/test_remote_mcp_server.py`
- `deploy/azure/README.md`
- `deploy/azure/env.example`
- `deploy/azure/local_remote_mcp_smoke_test.py`
- `docs/azure_remote_mcp_readiness.md`
- `README.md`

### Files Removed / Renamed

- None.

## Commands Run

```bash
math_rag/.venv/bin/python -m pytest math_rag/tests/test_remote_mcp_server.py
math_rag/.venv/bin/python -m pytest math_rag/tests
math_rag/.venv/bin/python -m math_rag.cli ingest deploy/azure/test_corpus --index-dir /private/tmp/math-rag-azure-test-index-auth
cp -R /private/tmp/math-rag-azure-test-index-auth .tmp-docker-test-index-auth
/opt/homebrew/opt/colima/bin/colima start -f
docker build -f deploy/azure/Dockerfile -t math-rag-remote-mcp:local .
docker run --rm -d --name math-rag-remote-mcp-auth-test -p 8000:8000 -e MATH_RAG_API_KEY=test-secret -e MATH_RAG_REMOTE_PUBLIC_BASE_URL=http://localhost:8000 -e MATH_RAG_REMOTE_MCP_READ_ONLY=true -e MATH_RAG_INDEX_DIR=/app/.math_rag_index -e MATH_RAG_REMOTE_HOST=0.0.0.0 -e MATH_RAG_REMOTE_PORT=8000 -e MATH_RAG_REMOTE_TRANSPORT=http -e MATH_RAG_REMOTE_PATH=/mcp/ -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false -v /Users/xiaxiao/Desktop/Projects/YTD_RAG/.tmp-docker-test-index-auth:/app/.math_rag_index:ro math-rag-remote-mcp:local
curl -i http://127.0.0.1:8000/mcp/
math_rag/.venv/bin/python - <<'PY'
import asyncio, json
import httpx
from fastmcp import Client

class StaticBearerAuth(httpx.Auth):
    def __init__(self, token: str) -> None:
        self._token = token
    def auth_flow(self, request):
        request.headers['Authorization'] = f'Bearer {self._token}'
        yield request

async def unauthenticated_probe():
    try:
        async with Client('http://127.0.0.1:8000/mcp/') as client:
            await client.list_tools()
    except Exception as exc:
        print(f'unauthenticated={type(exc).__name__}:{exc}')

async def authenticated_probe():
    async with Client('http://127.0.0.1:8000/mcp/', auth=StaticBearerAuth('test-secret')) as client:
        tools = await client.list_tools()
        print('tools=' + ','.join(sorted(tool.name for tool in tools)))
        search_result = await client.call_tool('search', {'query': 'Remote MCP Test Note'})
        search_payload = json.loads(search_result.content[0].text)
        first_id = search_payload['results'][0]['id']
        fetch_result = await client.call_tool('fetch', {'id': first_id})
        fetch_payload = json.loads(fetch_result.content[0].text)
        print('fetch_url=' + fetch_payload['url'])
        print('local_path_leak=' + str('/Users/' in json.dumps(fetch_payload)))

asyncio.run(unauthenticated_probe())
asyncio.run(authenticated_probe())
PY
math_rag/.venv/bin/python -m math_rag.cli ingest corpus --enrich-metadata
math_rag/.venv/bin/python -m math_rag.cli stats
docker stop math-rag-remote-mcp-auth-test
/opt/homebrew/opt/colima/bin/colima stop
```

## Test Results

- `math_rag/.venv/bin/python -m pytest math_rag/tests/test_remote_mcp_server.py`: `20 passed`
- `math_rag/.venv/bin/python -m pytest math_rag/tests`: `161 passed`
- Local Docker smoke test:
  - image build succeeded
  - container startup succeeded
  - unauthenticated `curl` to `/mcp/` returned `401 Unauthorized`
  - unauthenticated external FastMCP client failed with `401 Unauthorized`
  - authenticated external FastMCP client listed only `fetch,search`
  - authenticated external FastMCP client successfully called `search` and `fetch`
  - fetch payload did not leak `/Users/...` paths
- The first Python-to-container client attempt failed inside the sandbox with `Operation not permitted`; rerunning that specific probe with escalated execution confirmed the real auth behavior outside the sandbox restriction.

## Eval Results

Not run / Reason: No retrieval ranking, chunking, downloader, or eval logic changed.

## Current Status After Task

- Implemented:
  - `remote_mcp_server.py` now requires `MATH_RAG_API_KEY` by default.
  - `MATH_RAG_REMOTE_ALLOW_NO_AUTH=true` allows no-auth mode only as an explicit local-development override.
  - Remote HTTP requests now require `Authorization: Bearer <token>`.
  - Token comparison uses `secrets.compare_digest`.
  - Remote startup still refuses write-enabled configuration.
- Tested:
  - startup failure when API key is missing
  - explicit no-auth override
  - missing, malformed, and wrong bearer token rejection
  - authenticated list-tools, search, and fetch
  - remote tool surface restricted to `search` and `fetch`
  - path sanitization preserved
  - local Docker container behavior with the harmless test index
- Working:
  - remote app-layer auth is enforced at the Python layer
  - external authenticated FastMCP client access works
  - unauthenticated remote MCP access is rejected before Azure deployment
  - main workspace index was restored to `80` sources and `13870` chunks after the harmless-index smoke test
- Not implemented:
  - Azure resource creation
  - API Management configuration
  - Entra ID token validation at the Azure edge
- Blocked:
  - None at the repo/application layer
- Risk / caveat:
  - the temporary harmless test index directories remain on disk for reuse:
    - `/private/tmp/math-rag-azure-test-index-auth`
    - `.tmp-docker-test-index-auth/`

## Known Limitations / Open Issues

- The remote server now has application-layer bearer auth, but Azure-fronted auth is still required for a real deployment boundary.
- `MATH_RAG_REMOTE_ALLOW_NO_AUTH=true` is intentionally dangerous outside local development and must stay unset on Azure.
- The Docker smoke test still depends on the Colima bind-mount caveat already documented elsewhere: mount a workspace-shared copy, not `/private/tmp/...` directly.

## Recommended Next Step

- Prepare the tiny Azure pilot deployment inputs for API Management + Entra ID, using only the harmless test index and keeping `MATH_RAG_REMOTE_ALLOW_NO_AUTH` unset.

## Evidence Boundary

This log is engineering memory only. It is not mathematical theorem evidence.
