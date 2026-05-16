# Azure Remote Read-Only MCP Preparation

This directory contains preparation artifacts for running `math_rag` as a remote read-only MCP server that ChatGPT can connect to as a custom MCP connector.

This is documentation and configuration only. This task did not create Azure resources, run `az`, upload a corpus, upload `.math_rag_index`, or add secrets.

Before creating Azure resources, complete the no-secrets readiness checklist in `docs/azure_remote_mcp_readiness.md`. The first Azure deployment should use the harmless fixture corpus in `deploy/azure/test_corpus/`, not the real research index.

For a repeatable local preflight, run:

```bash
math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py
```

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
Azure Container App running math_rag.mcp_http_server
      |
      v
Mounted read-only .math_rag_index
```

The remote server is a read-only wrapper over an already-built local index. Ingestion remains local.

## Tool Surface

The remote entrypoint is:

```bash
python -m math_rag.mcp_http_server
```

Default `MATH_RAG_TOOL_MODE=chatgpt` exposes only:

- `search(query)`
- `fetch(id)`

Internal mode is available for trusted MCP clients:

```bash
MATH_RAG_TOOL_MODE=internal
```

It exposes `rag_search`, `rag_get_chunk`, `rag_list_sources`, `rag_stats`, and
conservative `rag_ask`.

It does not expose `rag_ingest`, downloader/discovery tools, shell tools, arbitrary file reads, or write tools.

## Required Runtime Environment

Use placeholders only in committed files. Configure real values in Azure environment settings or a secret store.

```bash
MATH_RAG_INDEX_DIR=/data/.math_rag_index
MATH_RAG_AUTH_MODE=bearer
MATH_RAG_API_TOKEN=<secret-store-value>
MATH_RAG_TOOL_MODE=chatgpt
MATH_RAG_REMOTE_MCP_READ_ONLY=true
MATH_RAG_HOST=0.0.0.0
PORT=8000
MATH_RAG_REMOTE_TRANSPORT=streamable-http
MATH_RAG_REMOTE_PATH=/mcp
MATH_RAG_SEARCH_TOP_K=8
MATH_RAG_MAX_TOP_K=20
MATH_RAG_FETCH_MAX_CHARS=12000
MATH_RAG_PROTECT_HEALTH=false
```

Generate a token with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

With `MATH_RAG_AUTH_MODE=bearer`, every remote MCP HTTP request must send:

```text
Authorization: Bearer <MATH_RAG_API_TOKEN>
```

Local-development-only no-auth mode is available on localhost with:

```bash
MATH_RAG_AUTH_MODE=none
```

Do not use `MATH_RAG_AUTH_MODE=none` on Azure. The server refuses
`MATH_RAG_HOST=0.0.0.0` with no auth unless
`MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=true` is explicitly set.

The server refuses startup if bearer mode lacks `MATH_RAG_API_TOKEN`,
`MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true`, or `MATH_RAG_REMOTE_MCP_READ_ONLY=false`.

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

The app-layer bearer token check is a second line of defense. It does not replace Azure-fronted authentication.

For any private-index pilot, set `MATH_RAG_PROTECT_HEALTH=true` before mounting
the real index. With bearer auth enabled, this protects `/mcp`, `/healthz`, and
`/readyz` with the same backend bearer token so the direct Container App FQDN
does not publicly reveal private-index readiness or counts. APIM health and
readiness policies must inject the backend bearer token when this flag is on.

## Low-Cost Public / Semi-Public Pilot

For low-sensitivity corpus data, use a locked vending-machine model: public
read access is acceptable, but the only buttons are `search` and `fetch`.

OpenAI's current ChatGPT Developer Mode app flow supports remote MCP over SSE
and streaming HTTP, with OAuth, No Authentication, or Mixed Authentication. It
does not provide a simple static bearer-token field for a ChatGPT-created
connector. Static bearer tokens are useful for backend protection and API
clients, but not as the primary ChatGPT Developer Mode app auth mechanism.

Preferred low-cost architecture for ChatGPT testing:

```text
ChatGPT Developer Mode app
      |
      | No Authentication
      v
APIM Consumption /mcp
      |
      | injects backend Authorization: Bearer <secret>
      v
Container App public FQDN
      |
      | MATH_RAG_AUTH_MODE=bearer
      v
read-only fixture or public-safe index
```

This is not a private-archive architecture. Direct Container App ingress may
remain public, but direct `/mcp` still requires the backend bearer token. Use it
only for low-sensitivity, bounded read-only data. Do not claim production or
private-index readiness.

Current low-cost pilot settings:

- Subscription: Azure for Students
- APIM: `apim-math-rag-mcp-5d67a258`, SKU `Consumption`
- Container App: `math-rag-mcp-test`, `0.5` CPU, `1Gi`, min replicas `0`, max replicas `1`
- ACR: `ca3ae23477c8acr`, SKU `Basic`
- Storage: `stmathragmcp5d67a258`, `Standard_LRS`
- Log Analytics: `workspace-rgmathragmcptest3QJx`, `PerGB2018`, 30-day retention

The APIM Consumption policy for this public/semi-public pilot should not
validate Entra on `/mcp`; it should only inject the backend bearer token and
rewrite to `/mcp`. APIM Consumption rejected `rate-limit-by-key` in this
tenant/SKU, so cost bounds currently rely on Container Apps min/max replicas,
server-side `search`/`fetch` caps, and manual cleanup.

ChatGPT setup for this pilot:

```text
Connector URL: https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
Authentication: No Authentication
Expected tools: search, fetch
Test query: Remote MCP Test Note
```

Do not use the direct Container App FQDN in ChatGPT. It is useful only for
backend diagnostics because it requires the private backend bearer token.

Cost caveat: this should be near-free for light fixture usage under
Consumption-style limits, but it is not guaranteed free. Storage, registry,
logging, bandwidth, APIM calls after any free tier, and unexpected traffic can
cost money.

For the APIM-fronted pilot, choose one backend-auth pattern explicitly:

- Preferred: APIM validates the user's Entra JWT, then replaces the inbound `Authorization` header with `Authorization: Bearer <MATH_RAG_API_TOKEN>` when forwarding to the Container App. Store that backend token as an APIM named value or secret-backed setting.
- Controlled-test fallback: the client supplies both the Entra/OAuth token required by APIM and the app-layer bearer token required by the container. Use this only for a private fixture-index test.
- Low-sensitivity public fallback: ChatGPT uses No Authentication to APIM, and
  APIM injects the backend bearer token. Use this only for public/semi-public,
  bounded read-only data.
- Do not set `MATH_RAG_AUTH_MODE=none` on an internet-reachable Container App. Only consider disabling app-layer bearer auth if the Container App is private and APIM is the only network path to it.

Minimal APIM/Entra policy shape for production review:

```xml
<validate-jwt header-name="Authorization" failed-validation-httpcode="401">
  <openid-config url="https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration" />
  <audiences>
    <audience>api://<entra-app-client-id></audience>
  </audiences>
  <required-claims>
    <claim name="scp" match="any">
      <value>mcp.read</value>
    </claim>
  </required-claims>
</validate-jwt>
```

After validation, APIM must preserve or set the MCP headers needed by the
backend. At minimum, allow `Accept`, `Content-Type`, `Mcp-Session-Id`, and the
backend `Authorization` header. Do not buffer or transform the Streamable HTTP
response body unless tested against the MCP initialize/list/call flow.

The non-secret template `deploy/azure/apim-private-mcp-policy.template.xml`
captures the risk-accepted private pilot policy shape. Replace placeholders
outside Git before applying it, and do not commit raw tokens or client secrets.

Also add gateway rate limits, avoid logging request/response bodies containing
queries or snippets, and prevent direct Container App ingress from bypassing
APIM.

### Direct Container App Ingress

For the 2026-05-12 fixture pilot, direct Container App ingress is still public:

```text
https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io
```

The app-layer bearer check rejects unauthenticated or wrong-token `/mcp`
requests, but this is not enough for private research data. A caller with the
backend bearer token could bypass APIM and reach the Container App directly.

Do not mount or expose the real `.math_rag_index` while this remains true.

The current APIM SKU is `Consumption`, and the current Container Apps
environment has no VNet/internal backend path. Do not apply a Container Apps IP
allowlist unless the APIM outbound source addresses are known and stable for the
chosen tier. For the current Consumption pilot, Azure reports no deterministic
dedicated APIM outbound IP, so IP allowlisting is not treated as a production
fix.

The production-grade direction is to use a network-capable APIM tier/design that
can reach a private/internal Container Apps backend, then keep the Container App
bearer token enabled as defense in depth. Disabling ingress without that private
path will break APIM because APIM currently forwards to the public Container App
service URL.

APIM / Entra pilot runbook:

1. Confirm the ChatGPT developer-mode app auth mode available to the workspace.
2. Create an Entra app registration with explicit tenant, audience, redirect URI, `mcp.read` scope, and restricted users/groups.
3. Create an APIM API for the MCP endpoint and attach the JWT validation policy to `/mcp`.
4. Configure APIM to inject the private backend bearer token or document the controlled-test fallback.
5. Keep `MATH_RAG_AUTH_MODE=bearer`, `MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=false`, `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false`, and `MATH_RAG_REMOTE_MCP_READ_ONLY=true`.
6. Mount only the fixture index from `deploy/azure/test_corpus/`, not the real research index.
7. Verify direct Container App ingress is blocked. If it is still publicly reachable, mark real-index rollout as blocked.
8. Run APIM endpoint checks: `/healthz`, `/readyz`, unauthenticated `/mcp`, authenticated initialize, `notifications/initialized`, `tools/list`, `search`, `fetch`, and path-leak scan.
9. Create a ChatGPT draft app only after APIM auth works, and confirm ChatGPT sees only `search` and `fetch`.
10. Switch to the real research index only after every fixture-index gateway, direct-ingress, ChatGPT, and leak-scan check passes.

## Azure Container Apps Notes

Recommended target: Azure Container Apps, because it fits a containerized HTTP MCP server with managed environment variables and mounted storage.

Operational requirements:

- run the container as non-root;
- expose only the MCP HTTP endpoint, normally `/mcp`;
- configure HTTPS;
- configure authentication before attaching ChatGPT;
- mount `/data/.math_rag_index` from private storage;
- keep `MATH_RAG_REMOTE_MCP_READ_ONLY=true`;
- never set `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true` in remote deployments.

The sample Bicep file is a skeleton for review only. It contains no secrets and should not be deployed without security review.

## ChatGPT Connector Setup

After deployment and authentication are configured, the connector URL should point to the remote MCP endpoint, for example:

```text
https://your-mcp-host.example.com/mcp
```

Allow only these tools:

```json
["search", "fetch"]
```

Do not allow internal `rag_*` tools, local stdio write tools such as
`rag_ingest`, downloader/discovery commands, shell tools, or arbitrary
filesystem tools through the ChatGPT connector.
