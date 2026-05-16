# Agent Log: Docker remote MCP container smoke test

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: 6b773d1
Related files:
- `docs/azure_remote_mcp_readiness.md`

## Status Before

The remote MCP code, the harmless test corpus, and the local in-process smoke-test helper were already working. The remaining local pre-Azure gap was container validation: build the image, mount a harmless index, and verify the `/mcp/` HTTP endpoint from outside the container.

## Goal of This Task

Run the Docker/Colima smoke test locally and record any operational caveats that affect the first Azure-style container run.

## Changes Made

### Files Created

- `agent_logs/codex/2026-05-07-docker-remote-mcp-container-smoke-test.md`

### Files Modified

- `docs/azure_remote_mcp_readiness.md`

### Files Removed / Renamed

- None.

## Commands Run

```bash
brew install colima docker
/opt/homebrew/opt/colima/bin/colima start -f
docker version --format '{{.Client.Version}}|{{.Server.Version}}'
docker build -f deploy/azure/Dockerfile -t math-rag-remote-mcp:local .
docker run --rm -d --name math-rag-remote-mcp-test -p 8000:8000 -e MATH_RAG_INDEX_DIR=/data/.math_rag_index -e MATH_RAG_REMOTE_MCP_READ_ONLY=true -e MATH_RAG_REMOTE_PUBLIC_BASE_URL=http://127.0.0.1:8000 -e MATH_RAG_REMOTE_HOST=0.0.0.0 -e MATH_RAG_REMOTE_PORT=8000 -e MATH_RAG_REMOTE_TRANSPORT=http -e MATH_RAG_REMOTE_PATH=/mcp/ -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false -v /private/tmp/math-rag-azure-test-index:/data/.math_rag_index:ro math-rag-remote-mcp:local
docker exec math-rag-remote-mcp-test /bin/sh -lc 'ls -lah /data/.math_rag_index && test -f /data/.math_rag_index/index.json && echo has_index || echo missing_index'
cp -R /private/tmp/math-rag-azure-test-index .tmp-docker-test-index
docker stop math-rag-remote-mcp-test
docker run --rm -d --name math-rag-remote-mcp-test -p 8000:8000 -e MATH_RAG_INDEX_DIR=/data/.math_rag_index -e MATH_RAG_REMOTE_MCP_READ_ONLY=true -e MATH_RAG_REMOTE_PUBLIC_BASE_URL=http://127.0.0.1:8000 -e MATH_RAG_REMOTE_HOST=0.0.0.0 -e MATH_RAG_REMOTE_PORT=8000 -e MATH_RAG_REMOTE_TRANSPORT=http -e MATH_RAG_REMOTE_PATH=/mcp/ -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false -v /Users/xiaxiao/Desktop/Projects/YTD_RAG/.tmp-docker-test-index:/data/.math_rag_index:ro math-rag-remote-mcp:local
docker exec math-rag-remote-mcp-test /bin/sh -lc 'ls -lah /data/.math_rag_index && test -f /data/.math_rag_index/index.json && echo has_index || echo missing_index'
math_rag/.venv/bin/python - <<'PY'
import asyncio, json
from fastmcp import Client

async def main():
    async with Client('http://127.0.0.1:8000/mcp/') as client:
        tools = await client.list_tools()
        print('tools=' + ','.join(sorted(tool.name for tool in tools)))
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

- Docker CLI installed successfully with Homebrew.
- Colima VM started successfully.
- Docker image build succeeded for `math-rag-remote-mcp:local`.
- First container run failed functionally because a direct `/private/tmp/...` bind mount appeared empty inside Colima.
- Second container run passed after mounting a workspace-shared copy of the same index.
- FastMCP client against `http://127.0.0.1:8000/mcp/` reported:
  - tools: `fetch,search`
  - `search_results=3`
  - `local_path_leak=False`

## Eval Results

Not run / Reason: No retrieval logic, ranking logic, or eval assets changed.

## Current Status After Task

- Implemented: The local Docker/Colima remote MCP path was validated and the readiness doc now captures the Colima mount caveat.
- Tested: Image build, container startup, visible mounted `index.json`, external FastMCP client call to `/mcp/`, and successful `search` and `fetch`.
- Working: The containerized remote MCP server serves only `fetch` and `search` and can read the harmless test index when the bind mount uses a workspace-shared path.
- Not implemented: Azure resources, API Management, Entra auth, and any real index deployment remain undone.
- Blocked: None for local container testing.
- Risk / caveat: Colima users must not mount `/private/tmp/...` directly for this test; use a workspace-shared copy.

## Known Limitations / Open Issues

- The Docker/Colima install modified the local machine outside the repo.
- The readiness doc still assumes a manual container run; it does not yet have a helper that wraps the Docker/Colima steps.

## Recommended Next Step

- Create Azure resources for a tiny private pilot behind API Management plus Entra ID, using only the harmless test index.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
