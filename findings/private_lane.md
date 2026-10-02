# Private Real-Index Lane

> Historical snapshot. Remote MCP was last recorded as paused on 2026-05-18
> with Container App ingress disabled. Claims below describe their original
> inspection dates; live status has not been rechecked. See the
> [remote MCP guide](../docs/remote_mcp_server.md) before any future use.

Date: 2026-05-15

## Current Blockers

Private real-index rollout is blocked by architecture, not by missing retrieval
code.

Observed blockers:

- Container App ingress is external/public.
- No Container App ingress IP restrictions are configured.
- APIM is Consumption, public, and has no VNet integration.
- APIM forwards to the public Container App FQDN.
- APIM current `/mcp` policy does not validate JWTs.
- Python app does not implement OAuth/JWT resource-server validation.

## Minimum Safe Direction

For private data, build a separate private lane:

```text
ChatGPT
  -> OAuth 2.1 / Entra-compatible auth
  -> APIM or equivalent gateway with JWT validation
  -> private/internal backend path
  -> Container App still read-only
  -> private index mounted read-only
```

## Network Change

The current APIM Consumption + public Container App setup should not be treated
as network isolation. Options for private rollout:

- APIM tier/topology with VNet-capable private backend access.
- Container Apps internal ingress or private endpoint pattern.
- Direct public Container App FQDN disabled only after APIM has a verified
  private backend route.

Do not simply disable ingress in the current topology; APIM currently depends on
the public Container App service URL.

## Auth Change

OpenAI Apps SDK auth guidance expects OAuth 2.1 for authenticated MCP servers.
Token verification can live at the gateway first, but any app-side user-specific
authorization later needs Python resource-server checks too:

- signature
- issuer
- audience/resource
- expiry / not-before
- scope
- replay/policy considerations

## What Can Stay Unchanged

- Keep external ChatGPT tool surface to `search` and `fetch`.
- Keep internal `rag_*` tools out of ChatGPT mode.
- Keep retrieval/ranking/chunking/ingestion unchanged.
- Keep fetched text bounded and metadata/path sanitized.
- Keep retrieved text as untrusted evidence, not instructions.

## Handoff

Status: fixture/public-safe lane is near complete. Private real-index lane
requires network/auth architecture work before any index mount.
