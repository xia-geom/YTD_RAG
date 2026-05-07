# Azure Remote Read-Only MCP Preparation

This directory contains preparation artifacts for running `math_rag` as a remote read-only MCP server that ChatGPT can connect to as a custom MCP connector.

This is documentation and configuration only. This task did not create Azure resources, run `az`, upload a corpus, upload `.math_rag_index`, or add secrets.

References:

- OpenAI MCP docs: https://developers.openai.com/api/docs/mcp
- OpenAI connector help: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt

## Architecture

```text
ChatGPT / MCP client
      |
      |  OAuth / Bearer token
      v
Azure API Management
      |
      |  validate-jwt or validate-azure-ad-token
      v
Azure Container App running math_rag.remote_mcp_server
      |
      v
Mounted read-only .math_rag_index
```

The remote server is a read-only wrapper over an already-built local index. Ingestion remains local.

## Tool Surface

The remote entrypoint is:

```bash
python -m math_rag.remote_mcp_server
```

It exposes only ChatGPT-compatible data tools:

- `search(query: str)`: returns JSON text with `results`.
- `fetch(id: str)`: returns JSON text for one indexed chunk.

It does not expose `rag_ingest`, downloader/discovery tools, shell tools, arbitrary file reads, or write tools.

## Required Runtime Environment

Use placeholders only in committed files. Configure real values in Azure environment settings or a secret store.

```bash
MATH_RAG_INDEX_DIR=/data/.math_rag_index
MATH_RAG_REMOTE_MCP_READ_ONLY=true
MATH_RAG_REMOTE_PUBLIC_BASE_URL=https://your-mcp-host.example.com
MATH_RAG_REMOTE_HOST=0.0.0.0
MATH_RAG_REMOTE_PORT=8000
MATH_RAG_REMOTE_TRANSPORT=http
MATH_RAG_REMOTE_PATH=/mcp/
```

`MATH_RAG_REMOTE_PUBLIC_BASE_URL` is required so `search` and `fetch` return stable citation URLs. Use HTTPS in production.

The server refuses startup if `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true` or `MATH_RAG_REMOTE_MCP_READ_ONLY=false`.

## Container Image

Build from the workspace root so the Dockerfile can copy the package:

```bash
# Documentation only. Do not run as part of this prep task.
docker build -f deploy/azure/Dockerfile -t math-rag-remote-mcp:local .
```

The root `.dockerignore` excludes `corpus/`, `.math_rag_index/`, virtual environments, PDFs, and secrets from the Docker build context.

The Dockerfile installs only the package and remote MCP dependencies. It does not copy `corpus/` or `.math_rag_index/`.

## Index Mount

Provide an already-built `.math_rag_index` at runtime, mounted read-only if possible:

```text
/data/.math_rag_index/index.json
```

Do not bake private corpus data or the private index into a public image. For Azure Container Apps, use a private storage account, private registry, and a locked-down mount strategy appropriate for your institution.

## Authentication

Treat indexed content as private research data. ChatGPT can read whatever the remote server exposes from the mounted index.

Do not connect ChatGPT to this server until HTTPS and authentication are configured. OpenAI recommends OAuth for protecting private MCP data integrations.

Preferred architecture: put Azure API Management in front of Azure Container Apps and use Microsoft Entra ID as the OAuth/JWT issuer. API Management should validate incoming bearer tokens with `validate-jwt` or `validate-azure-ad-token`, enforce the expected issuer, audience, scopes/claims, and forward only authenticated traffic to the Container App.

Container Apps built-in authentication is a fallback, not the default. It may be useful for a small private pilot, but API Management gives clearer bearer-token validation, gateway policy, logging, and rate-limit controls for a remote MCP endpoint.

This V1 prep does not implement OAuth inside `math_rag`; it documents the requirement and keeps the server read-only.

Avoid custom OAuth inside `math_rag` unless Azure-fronted authentication proves impossible. Keeping OAuth at the Azure boundary keeps the Python RAG server small, read-only, and easier to audit.

Pre-deployment checklist:

- confirm the ChatGPT connector/app auth mode available to the workspace;
- confirm the connector can use Entra OAuth endpoints and send `Authorization: Bearer ...` to the MCP endpoint;
- choose the MCP transport path, usually Streamable HTTP at `/mcp/`, and test API Management compatibility before production;
- design a private Entra app registration with explicit tenant, redirect URIs, scopes/audience, and restricted users/groups;
- define the API Management token validation policy with issuer, audience, required scopes/claims, expiration, and signed-token checks;
- prevent direct Container App ingress from bypassing API Management;
- mount `.math_rag_index` read-only from private storage;
- keep `corpus/`, `.math_rag_index/`, PDFs, `.env`, and secrets out of the image;
- keep `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false` and `MATH_RAG_REMOTE_MCP_READ_ONLY=true`;
- set `MATH_RAG_REMOTE_PUBLIC_BASE_URL` to the authenticated API Management URL;
- define logging policy so query text and returned snippets are not retained more broadly than intended;
- use a private test index first, not unpublished research content.

## Azure Container Apps Notes

Recommended target: Azure Container Apps, because it fits a containerized HTTP MCP server with managed environment variables and mounted storage.

Operational requirements:

- run the container as non-root;
- expose only the MCP HTTP endpoint, normally `/mcp/`;
- configure HTTPS;
- configure authentication before attaching ChatGPT;
- mount `/data/.math_rag_index` from private storage;
- keep `MATH_RAG_REMOTE_MCP_READ_ONLY=true`;
- never set `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true` in remote deployments.

The sample Bicep file is a skeleton for review only. It contains no secrets and should not be deployed without security review.

## ChatGPT Connector Setup

After deployment and authentication are configured, the connector URL should point to the remote MCP endpoint, for example:

```text
https://your-mcp-host.example.com/mcp/
```

Allow only these tools:

```json
["search", "fetch"]
```

Do not allow local stdio tools such as `rag_ingest`, `rag_ask`, `rag_get_chunk`, or downloader/discovery commands through the remote connector.
