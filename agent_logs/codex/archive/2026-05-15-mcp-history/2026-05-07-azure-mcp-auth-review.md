# Agent Log: Azure remote MCP authentication review

Date: 2026-05-07
Agent: Codex
Branch: master
Commit: c816f34 at review start
Related files:
- `math_rag/src/math_rag/remote_mcp_server.py`
- `math_rag/tests/test_remote_mcp_server.py`
- `deploy/azure/README.md`
- `deploy/azure/azure-container-apps.sample.bicep`

## Goal

Review how to protect the private `.math_rag_index` before any Azure deployment or ChatGPT connection.

This review is documentation and threat-model work only. No Azure resources were created. No `az` commands were run. No corpus, index, or secrets were uploaded.

## Sources Reviewed

- OpenAI MCP docs: https://developers.openai.com/api/docs/mcp
- OpenAI ChatGPT apps/connectors help: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt
- Azure Container Apps authentication docs: https://learn.microsoft.com/en-us/azure/container-apps/authentication
- Azure API Management `validate-jwt` policy docs: https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy
- Azure Container Apps storage mounts docs: https://learn.microsoft.com/en-us/azure/container-apps/storage-mounts

## Current Remote MCP Status

The committed remote MCP implementation is structurally correct for a read-only ChatGPT data connector:

- remote entrypoint is separate from local stdio MCP;
- exposed remote tools are only `search` and `fetch`;
- `search` returns one text content item containing JSON with `results`;
- `fetch` returns one text content item containing JSON with `id`, `title`, `text`, `url`, and `metadata`;
- remote startup refuses `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true`;
- remote startup refuses `MATH_RAG_REMOTE_MCP_READ_ONLY=false`;
- remote response metadata sanitizes local path leaks;
- no ingestion, downloader, discovery, shell, arbitrary filesystem read, or write tool is exposed remotely.

OpenAI recommends OAuth for protecting custom remote MCP servers that expose private data. ChatGPT apps/connectors may require an OAuth flow when connecting an app.

## Options Compared

### Option A: Azure API Management in front of Container Apps

Use Microsoft Entra ID as the OAuth issuer and put Azure API Management in front of the remote MCP Container App. API Management validates incoming bearer tokens with `validate-jwt` or `validate-azure-ad-token`, enforces audience/issuer/scope claims, and forwards only authenticated traffic to the container.

Pros:

- best fit for non-browser MCP clients sending `Authorization: Bearer ...`;
- token validation is explicit and centralized;
- can add rate limits, request logging controls, IP restrictions, and claim-based access policies;
- keeps `math_rag` free of custom OAuth code.

Cons:

- more Azure configuration and likely more cost;
- must verify Streamable HTTP/SSE behavior through API Management before production;
- still requires correct Entra app registration and ChatGPT OAuth configuration.

### Option B: Azure Container Apps built-in authentication

Use Container Apps authentication, also known as Easy Auth, with Microsoft Entra ID or another OpenID Connect provider.

Pros:

- minimal code;
- built into Container Apps;
- can require authentication and inject user claims as headers.

Cons:

- browser/session-oriented behavior may be less predictable for MCP clients than direct bearer-token validation;
- client-directed flow may require `/.auth/login/<provider>` and `X-ZUMO-AUTH`;
- fewer API gateway controls than API Management.

### Option C: Custom OAuth inside `math_rag`

Implement OAuth authorization endpoints, token validation, and potentially dynamic client registration inside the Python remote MCP server.

Pros:

- maximum protocol control;
- could be tailored tightly to OpenAI MCP/app expectations.

Cons:

- highest security burden;
- easy to implement incorrectly;
- expands the trusted codebase and maintenance surface;
- conflicts with the goal that `math_rag` remain a small read-only RAG adapter.

## Recommended Architecture

Use **Azure API Management in front of Azure Container Apps**, with Microsoft Entra ID as the OAuth issuer.

Recommended shape:

```text
ChatGPT custom MCP connector
      |
      | OAuth / Bearer token
      v
Azure API Management
      |
      | validate-jwt or validate-azure-ad-token
      v
Azure Container App running math_rag.remote_mcp_server
      |
      v
Read-only mounted /data/.math_rag_index
```

Keep the Container App private or otherwise restrict direct bypass of API Management. The Python app should remain read-only and should not implement OAuth itself in V1.

Use Container Apps built-in authentication only as a fallback if API Management proves incompatible with the MCP HTTP transport or too heavy for the first private pilot.

Do not choose custom OAuth inside `math_rag` unless OpenAI/ChatGPT connector requirements make Azure-fronted auth impossible.

## Pre-Deployment Checklist

Before creating resources:

- Confirm the exact ChatGPT connector/app auth mode available to the workspace.
- Confirm whether the connector can use Entra OAuth endpoints and send `Authorization: Bearer` to the MCP endpoint.
- Decide whether the remote endpoint will use Streamable HTTP `/mcp/` or SSE `/sse/`, then verify that API Management supports the chosen transport in a smoke test.
- Create a private Entra app registration design with least privilege: explicit tenant, explicit redirect URIs, explicit scopes/audience, and restricted allowed users/groups.
- Define API Management token policy: issuer, audience, required scopes/claims, expiration required, signed tokens required.
- Ensure Container App ingress cannot be reached directly except through API Management.
- Mount `.math_rag_index` read-only, ideally from private Azure Files or equivalent private storage.
- Keep the image free of `corpus/`, `.math_rag_index/`, PDFs, `.env`, and secrets.
- Ensure `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false` and `MATH_RAG_REMOTE_MCP_READ_ONLY=true`.
- Set `MATH_RAG_REMOTE_PUBLIC_BASE_URL` to the authenticated public API Management URL.
- Define logging policy so query text and returned corpus snippets are not stored more broadly than intended.
- Prepare a private test index first; do not expose unpublished research content during initial smoke testing.

## Known Risks

- Remote MCP exposes indexed private content to any authenticated client allowed by the auth layer.
- Prompt injection remains possible because indexed documents may contain adversarial or irrelevant instructions; the server must stay data-only and read-only.
- API Management compatibility with MCP streaming transport must be tested before production.
- Misconfigured Container App ingress could bypass API Management.
- Misconfigured Entra audience/scope claims could allow unintended clients.
- Azure Files/storage credentials and mounts must be kept private and read-only where possible.
- Response metadata sanitization reduces path leaks but does not replace authentication.

## Commands Run

```bash
git status --short
math_rag/.venv/bin/python -m pytest math_rag/tests/test_remote_mcp_server.py
```

## Test Results

Focused remote MCP tests:

```text
10 passed
```

## Final Recommendation

Next implementation task should be documentation-only refinement of `deploy/azure/README.md` to record API Management + Entra ID as the preferred auth architecture and mark Container Apps Easy Auth as a fallback, or proceed directly to a no-secrets deployment dry-run checklist if the user wants operational prep.

Actual Azure deployment should wait until the auth design above is accepted.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
