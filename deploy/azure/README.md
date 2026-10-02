# Optional Azure MCP deployment

**Remote serving was paused on 2026-05-18 by disabling Container App ingress.**
The last recorded deployment used a reviewed public-safe index. No cloud state
is checked or changed by reading these instructions. See the
[pause report](../../agent_logs/codex/2026-05-18-remote-mcp-paused.md) for resource
history and the deliberate resume procedure.

The container runs `math_rag.mcp_http_server` over an already-built index.
Ingestion remains local. Complete the [deployment gates](../../docs/azure_remote_mcp_readiness.md)
before exposing any endpoint; the private research index is not fixture data.

## Retained assets

| File/directory | Purpose |
| --- | --- |
| `Dockerfile` | Non-root Python image; installs the `remote-mcp` extra |
| `env.example` | Runtime setting reference; no secrets |
| `azure-container-apps.sample.bicep` | Reviewable infrastructure skeleton |
| `apim-private-mcp-policy.template.xml` | Gateway JWT/backend-bearer policy template |
| `test_corpus/` | Harmless Markdown/LaTeX fixture sources |
| `local_remote_mcp_smoke_test.py` | In-process fixture MCP checks |
| `fixture_connector_verification/` | APIM verifier, input, and manual evidence instructions |

Templates are not ready-to-apply private deployment configurations. Replace
placeholders outside Git. Historical investigations remain in `findings/`.

## Local verification

From the workspace root:

```bash
math_rag/.venv/bin/python -m pip install -e './math_rag[remote-mcp,dev]'
math_rag/.venv/bin/python -m pytest math_rag/tests
math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py
```

The smoke helper builds `.tmp-azure-test-index` from `test_corpus/`, checks
read-only/auth startup rules, and exercises ChatGPT `search`/`fetch` and internal
read-only tools with an in-process client. It does not contact Azure or verify
HTTP networking. Its generated fixture index is disposable; the research index
is not used.

For manual fixture ingestion:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest deploy/azure/test_corpus --index-dir .tmp-azure-test-index
math_rag/.venv/bin/python -m math_rag.cli stats --index-dir .tmp-azure-test-index
```

## Container verification

Build from the workspace root. Set `MATH_RAG_API_TOKEN` in the shell from a
secret store before running the bearer-protected container:

```bash
docker build -f deploy/azure/Dockerfile -t math-rag-mcp-http:local .
docker run --rm -p 127.0.0.1:8000:8000 \
  -e MATH_RAG_API_TOKEN \
  -e MATH_RAG_AUTH_MODE=bearer \
  -e MATH_RAG_TOOL_MODE=chatgpt \
  -e MATH_RAG_PROTECT_HEALTH=true \
  -v "$PWD/.tmp-azure-test-index:/data/.math_rag_index:ro" \
  math-rag-mcp-http:local
```

Verify requests without a token fail and authenticated MCP calls succeed with
exactly `search` and `fetch`. `.dockerignore` excludes research data, indexes,
virtualenvs, PDFs, and secrets; the image copies package code only. Mount only
the fixture index for these checks.

For HTTP settings and tool behavior, use the
[server reference](../../docs/remote_mcp_server.md). For APIM checks after a
deliberate resume, use the [fixture verifier guide](fixture_connector_verification/README.md).
