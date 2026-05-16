# Azure Remote MCP Readiness

This checklist prepares the project for a first Azure test deployment of the remote read-only MCP server. It does not create Azure resources, run `az`, upload the private corpus, or expose the real `.math_rag_index`.

## Target Architecture

```text
ChatGPT / custom app
      |
      | OAuth / Bearer token
      v
Azure API Management
      |
      | validate-jwt or validate-azure-ad-token
      v
Azure Container App
      |
      v
Read-only mounted test .math_rag_index
```

Use API Management plus Microsoft Entra ID as the default authentication
boundary for private or risk-accepted private-index work. Container Apps
built-in auth is a fallback. Do not implement custom OAuth inside `math_rag`
for the first deployment. The current fixture/public-safe lane is different:
it uses APIM as a No Authentication facade that injects the backend bearer
token.

## Low-Cost Public Strategy

For the low-sensitivity public/semi-public strategy, the objective changes from
private archive protection to bounded read-only access:

```text
ChatGPT Developer Mode app
      |
      | No Authentication
      v
APIM Consumption /mcp
      |
      | injects backend bearer token
      v
Container App with MATH_RAG_AUTH_MODE=bearer
      |
      v
fixture or public-safe read-only index
```

This strategy is intentionally a locked vending machine, not a bank vault. It is
acceptable only when the indexed corpus is low-sensitivity or intentionally
public-readable. Keep the exposed tool surface to `search` and `fetch`, preserve
fetch/search caps, and keep metadata/path sanitization enabled.

OpenAI's ChatGPT Developer Mode app setup supports SSE and streaming HTTP with
OAuth, No Authentication, or Mixed Authentication. It does not provide a simple
static bearer-token field for a created ChatGPT connector, so direct
Container-App bearer mode is best kept as backend protection or for API clients.
For a cheap ChatGPT test, use APIM No Authentication in front of a
bearer-protected Container App.

Do not switch to public no-auth Container App mode unless explicitly approved:

```bash
MATH_RAG_AUTH_MODE=none
MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=true
```

That fallback removes the backend bearer check and is weaker than the APIM
façade.

Cost controls for the student pilot:

- Container App min replicas `0`, max replicas `1`
- no private endpoints, VNets, premium SKUs, or always-on replicas
- APIM SKU `Consumption` only
- ACR SKU `Basic`
- small Standard LRS storage only if using an Azure Files mount
- minimal logs; do not log full request/response bodies or large snippets
- cleanup the whole resource group when not testing

Known APIM Consumption limitation observed in the pilot: `rate-limit-by-key` was
rejected for this SKU, so do not depend on APIM rate limiting unless a supported
policy is verified.

## Runtime Environment

Use these values for the first test deployment, replacing placeholders in Azure configuration only:

```bash
MATH_RAG_INDEX_DIR=/data/.math_rag_index
MATH_RAG_AUTH_MODE=bearer
MATH_RAG_API_TOKEN=<random-secret>
MATH_RAG_TOOL_MODE=chatgpt
MATH_RAG_REMOTE_MCP_READ_ONLY=true
MATH_RAG_HOST=0.0.0.0
PORT=8000
MATH_RAG_REMOTE_TRANSPORT=streamable-http
MATH_RAG_REMOTE_PATH=/mcp
MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false
MATH_RAG_ALLOW_UNAUTHENTICATED_PUBLIC=false
MATH_RAG_PROTECT_HEALTH=false
```

Generate the API key with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Resource-name placeholders for the first pilot:

```text
resource group: rg-ytd-rag-mcp-test
container app: ca-ytd-rag-mcp-test
container app environment: cae-ytd-rag-mcp-test
container registry: acr<unique>ytdragtest
storage account: st<unique>ytdragtest
file share: math-rag-test-index
api management: apim-ytd-rag-mcp-test
Entra app registration: ytd-rag-mcp-test
scope/audience: api://<entra-app-client-id>/mcp.read
```

## Tiny Test Index Workflow

Use only harmless test fixtures for the first deployment. The fixture corpus is under `deploy/azure/test_corpus/`.

Build a test-only index locally:

```bash
math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py
```

This helper builds `.tmp-azure-test-index`, verifies safe remote-server failure modes, runs an in-process MCP client against ChatGPT `search`/`fetch`, checks internal `rag_*` mode separately, and prints a JSON summary with sanitized source identifiers.

If you want the manual steps instead:

```bash
rm -rf .tmp-azure-test-index
math_rag/.venv/bin/python -m math_rag.cli ingest deploy/azure/test_corpus --index-dir .tmp-azure-test-index
math_rag/.venv/bin/python -m math_rag.cli stats --index-dir .tmp-azure-test-index
```

Expected result: the stats output should show only the dummy test sources from `deploy/azure/test_corpus/`.

For a local remote-MCP smoke test:

```bash
MATH_RAG_INDEX_DIR=.tmp-azure-test-index \
MATH_RAG_AUTH_MODE=none \
MATH_RAG_TOOL_MODE=chatgpt \
MATH_RAG_REMOTE_MCP_READ_ONLY=true \
MATH_RAG_HOST=127.0.0.1 \
PORT=8000 \
MATH_RAG_REMOTE_TRANSPORT=streamable-http \
MATH_RAG_REMOTE_PATH=/mcp \
MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

Also verify local safety failures:

```bash
MATH_RAG_INDEX_DIR=.tmp-azure-test-index \
MATH_RAG_HOST=0.0.0.0 \
MATH_RAG_AUTH_MODE=none \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

Expected: startup fails because unauthenticated public bind is blocked.

```bash
MATH_RAG_INDEX_DIR=.tmp-azure-test-index \
MATH_RAG_AUTH_MODE=bearer \
MATH_RAG_API_TOKEN=test-secret \
MATH_RAG_REMOTE_MCP_READ_ONLY=false \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

Expected: startup fails because remote mode is read-only only.

```bash
MATH_RAG_INDEX_DIR=.tmp-azure-test-index \
MATH_RAG_AUTH_MODE=bearer \
MATH_RAG_API_TOKEN=test-secret \
MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true \
math_rag/.venv/bin/python -m math_rag.mcp_http_server
```

Expected: startup fails because remote mode refuses write-enabled configuration.

`MATH_RAG_AUTH_MODE=none` is local-development-only and must not be used on Azure.

For a private-index pilot, set `MATH_RAG_PROTECT_HEALTH=true` before mounting
the real index. That makes `/healthz` and `/readyz` require the same backend
bearer token as `/mcp`; APIM must inject the backend bearer for those endpoint
checks. This does not make a public Container App backend private, but it avoids
leaking index readiness/counts from direct unauthenticated health probes.

## Container Readiness

Build from the workspace root:

```bash
docker build -f deploy/azure/Dockerfile -t math-rag-remote-mcp:local .
```

Run locally with the test index mounted read-only:

```bash
cp -R .tmp-azure-test-index .tmp-docker-test-index
docker run --rm \
  -p 8000:8000 \
  -e MATH_RAG_INDEX_DIR=/data/.math_rag_index \
  -e MATH_RAG_AUTH_MODE=bearer \
  -e MATH_RAG_API_TOKEN=test-secret \
  -e MATH_RAG_TOOL_MODE=chatgpt \
  -e MATH_RAG_REMOTE_MCP_READ_ONLY=true \
  -e MATH_RAG_HOST=0.0.0.0 \
  -e PORT=8000 \
  -e MATH_RAG_REMOTE_TRANSPORT=streamable-http \
  -e MATH_RAG_REMOTE_PATH=/mcp \
  -e MATH_RAG_MCP_ALLOW_WRITE_TOOLS=false \
  -v "$PWD/.tmp-docker-test-index:/data/.math_rag_index:ro" \
  math-rag-remote-mcp:local
rm -rf .tmp-docker-test-index
```

Confirm the container runs as the non-root `mathrag` user and exposes only `search` and `fetch` in ChatGPT mode.
Confirm that a request without `Authorization: Bearer test-secret` is rejected and that authenticated `search` succeeds.

On Colima, use workspace-shared temporary directories such as `.tmp-docker-test-index`; host paths outside the shared workspace can produce empty mounts and `index_not_found` responses.

## Azure Auth Preflight

Before running any private or risk-accepted Azure command, write down:

- Entra tenant ID and app registration name.
- Redirect URI required by the ChatGPT custom app flow.
- Audience and scope, using `api://<client-id>/mcp.read` for the test pilot.
- Users or groups allowed to connect.
- API Management policy that requires `Authorization: Bearer ...`, validates issuer, audience, expiration, signature, and required scope.
- Container App ingress rule that prevents direct bypass of API Management.
- Storage mount strategy for `/data/.math_rag_index`, read-only if possible.
- Secret source for `MATH_RAG_API_TOKEN`.
- Logging policy that avoids retaining query text and returned snippets beyond intended diagnostics.

## APIM Modes and Runbooks

### Current Fixture/Public-Safe APIM Mode

Use this mode for the harmless fixture connector or for a separately reviewed
public-safe index only.

- ChatGPT Developer Mode connects to
  `https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp` with
  `No Authentication`.
- The current APIM fixture/public-safe policy does not validate an Entra JWT.
  It injects the private backend bearer token from an APIM named value and
  rewrites the request to backend `/mcp`.
- APIM unauthenticated MCP initialize may succeed in this mode because the
  caller-facing edge is intentionally no-auth for ChatGPT compatibility.
- The direct Container App `/mcp` endpoint must still require the backend
  bearer token. Direct `/healthz` and `/readyz` may be public unless
  `MATH_RAG_PROTECT_HEALTH=true` is enabled.
- This mode is not private-index ready. Keep it limited to fixture data or
  explicitly reviewed public-safe data.

### Private / Risk-Accepted OAuth Runbook

Use this as the operator checklist before mounting private index data. Replace
placeholders only in Azure or a private deployment notebook, never in committed
files.

1. Create or identify an Entra app registration for the MCP API.
   - Tenant: `<tenant-id>`
   - Application/client ID: `<api-client-id>`
   - Application ID URI or audience: `api://<api-client-id>`
   - Scope: `mcp.read`
   - Allowed users/groups: restricted test users only
   - Redirect URI: the value required by the ChatGPT draft app flow, if ChatGPT developer mode is used
2. Create or identify an APIM instance and API for the MCP endpoint.
   - Public path should route `/mcp`, `/healthz`, and `/readyz`.
   - Preserve Streamable HTTP headers: `Accept`, `Content-Type`, `Mcp-Session-Id`, and `Authorization`.
   - Do not log request or response bodies.
3. Add APIM JWT validation on `/mcp`.
   - Validate issuer from `https://login.microsoftonline.com/<tenant-id>/v2.0`.
   - Validate audience `api://<api-client-id>`.
   - Require signed, unexpired tokens.
   - Require the `mcp.read` scope or equivalent restricted claim.
   - Start from `deploy/azure/apim-private-mcp-policy.template.xml` if applying
     the policy manually; replace placeholders outside Git and never write raw
     bearer tokens or client secrets into a committed file.
4. Decide how APIM reaches the backend bearer check.
   - Preferred: APIM injects a private backend `Authorization: Bearer <MATH_RAG_API_TOKEN>` after validating the user JWT.
   - Alternative: client satisfies both gateway OAuth and app bearer auth, only for a controlled test.
   - Do not disable app bearer auth unless the Container App is private and APIM is the only reachable caller.
5. Block or mark direct Container App ingress as unsafe.
   - Preferred: private networking or ingress restrictions allow only APIM to reach the backend.
   - If direct public ingress remains reachable, strict private rollout is
     blocked. A personal risk-accepted private-index pilot may continue only
     after explicit approval and only with APIM OAuth/JWT validation, backend
     bearer auth, protected health endpoints, and a read-only index mount.
6. Mount the approved index only.
   - For fixture validation, source content must be limited to
     `deploy/azure/test_corpus/sample_note.md` and
     `deploy/azure/test_corpus/sample_paper.tex`.
   - For private-index work, do not mount or upload the private index until
     APIM OAuth/JWT validation succeeds.
   - The mount should be read-only where the Azure storage mode supports it.
7. Run remote checks through the APIM hostname, not the raw Container App hostname.
   - `/healthz`
   - `/readyz`
   - unauthenticated `/mcp`, expecting `401` or `403` only after the private
     OAuth/JWT policy is installed
   - authenticated initialize
   - `notifications/initialized`
   - `tools/list`, expecting exactly `search` and `fetch`
   - `search`
   - `fetch`
   - forbidden-string/path-leak scan

Do not use the real research index until every APIM, direct-ingress, ChatGPT
tool-list, search/fetch, and path-leak check above passes on the fixture index.

## Current Direct-Ingress Blocker

As of 2026-05-12, the fixture pilot uses:

- API Management: `apim-math-rag-mcp-5d67a258`, SKU `Consumption`
- APIM gateway: `https://apim-math-rag-mcp-5d67a258.azure-api.net`
- Container App: `math-rag-mcp-test`
- Direct Container App FQDN: `https://math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io`
- Mounted index: harmless fixture index only, mounted at `/data/.math_rag_index`

The current fixture/public-safe APIM policy is a No Authentication facade for
ChatGPT Developer Mode. It injects the private backend bearer token for the
Container App and rewrites requests to backend `/mcp`; it does not currently
validate an Entra JWT. The Container App still has public external ingress
enabled and no IP security restrictions. Direct unauthenticated `/mcp` is
rejected by app-layer bearer auth, but the direct Container App hostname remains
network-reachable.

Do not use the current fixture/public-safe deployment for the real private
research index. A caller with the backend bearer token could bypass APIM and
call the Container App directly. Strict private-index readiness requires a
private/internal backend path or equivalent reviewed control. A personal
risk-accepted private-index pilot still requires explicit approval, APIM
OAuth/JWT validation, backend bearer auth, protected health endpoints, and a
read-only mount before any private index is exposed.

The reviewed mitigation options are:

- Preferred private/internal path: requires a network-capable design, such as a
  VNet-integrated or VNet-injected APIM tier and a private/internal Container
  Apps backend. The current APIM Consumption instance and Container Apps
  environment are not configured for that.
- IP allowlisting: not accepted as a production-grade fix for the current
  Consumption APIM instance because it does not expose a deterministic dedicated
  outbound IP suitable for a narrow Container Apps allow rule.
- Disable Container App ingress: not viable in the current architecture because
  APIM forwards to the public Container App service URL and has no alternate
  private backend path.

Rollback for any future ingress/network change: restore the Container App
ingress to external HTTP target port `8000`, remove any Container Apps IP
security restrictions that broke APIM, verify `/healthz` and `/readyz`, then
rerun authenticated APIM initialize, `tools/list`, `search`, and `fetch`.

Required production direction before real-index rollout:

1. Create a dedicated ChatGPT-compatible Entra app registration and `mcp.read`
   scope.
2. Move to a network architecture where APIM reaches the backend through a
   private/internal path, or another reviewed equivalent that blocks the public
   Container App FQDN even for callers with the backend bearer token.
3. Keep app-layer bearer auth enabled as defense in depth.
4. Rerun the fixture APIM smoke, direct-ingress test, ChatGPT draft app test,
   and path/secret scan.
5. Only then request explicit approval to mount the real index read-only.

## Go / No-Go Before Azure

Proceed to Azure only when all are true:

- Status-first documentation changes are either intentionally uncommitted or committed by explicit user request.
- Unit tests for remote MCP pass.
- Full package tests pass.
- The tiny test index builds and stats show only test fixture sources.
- Local remote MCP works with the tiny test index.
- Docker image builds and runs locally with the tiny test index.
- No private `corpus/`, real `.math_rag_index`, PDFs, `.env`, secrets, or unpublished research are in the image or planned upload.

Do not expose the real research index until the tiny test-index deployment proves authentication, transport, logging, and tool behavior.
