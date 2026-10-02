# Remote MCP deployment gates

**Recorded status: paused since 2026-05-18.** Container App ingress was disabled,
so the existing APIM backend path cannot serve MCP. This document is a checklist
for a deliberate future resume, not evidence of a current live deployment.
See the [pause report](../agent_logs/codex/2026-05-18-remote-mcp-paused.md).

## Fixture/public-safe lane

The last deployed data was a reviewed public-safe index. The recorded route was:

```text
ChatGPT → APIM (No Authentication) → backend bearer check → read-only public-safe index
```

This lane is only for harmless fixtures or explicitly reviewed public data.
Before resuming:

1. Run the package tests and [local fixture smoke test](../deploy/azure/README.md#local-verification).
2. Build/check the Docker image with only fixture data mounted read-only.
   Exclude corpus, private indexes, PDFs, `.env`, and secrets from the image.
3. Inspect actual cloud state and deliberately restore the intended ingress
   path. Keep backend bearer authentication enabled and write tools disabled.
4. Run the [APIM verifier](../deploy/azure/fixture_connector_verification/README.md)
   for health/readiness, initialize, tool list, search, fetch, and leak scanning.
5. Verify the ChatGPT draft app sees exactly `search` and `fetch`; save a
   sanitized transcript and rerun the verifier with `--manual-transcript`.

A passing local smoke test does not establish remote availability. A passing
APIM verifier without manual UI evidence does not establish ChatGPT readiness.

## Private-index lane

Private rollout requires all of the following:

- OAuth/JWT validation at the gateway, including signature, expiry, issuer,
  audience, required scope, and allowed users/groups.
- A private/internal backend route or reviewed equivalent that prevents direct
  public ingress from bypassing the gateway, even with a backend bearer token.
- Backend bearer authentication, `MATH_RAG_PROTECT_HEALTH=true`, a read-only
  index mount, and remote write tools disabled.
- Fixture verification of authentication, direct-ingress isolation, ChatGPT
  tool visibility, result caps, and path/secret leakage before private data.
- An explicit decision to expose the intended private data.

The recorded APIM Consumption/public-backend setup does not establish these
requirements. OAuth is a gateway responsibility; the Python server implements
backend bearer checks, not OAuth/JWT validation. The
[policy template](../deploy/azure/apim-private-mcp-policy.template.xml) contains
placeholders, not a completed configuration.

An explicitly requested, risk-accepted personal pilot may retain a public
backend only with OAuth/JWT validation, backend bearer auth, protected health,
a read-only mount, and a record of that residual risk. It is not strict
private-index readiness. See [private lane history](../findings/private_lane.md).

## Operational constraints

Keep the existing small pilot resource/replica limits unless a new deployment
requires otherwise. Retained registry, storage, logging, and gateway resources
may still incur costs while serving is paused. Verify actual resources and
pricing before resuming; no cost or security guarantee is implied here.

Keep tokens in a secret store and avoid logging queries, snippets, or response
bodies. Preserve Streamable HTTP headers through APIM. Do not infer isolation
from the presence of a gateway or from one successful bearer-auth request.

For server settings see [remote_mcp_server.md](remote_mcp_server.md); for retained
assets and local commands see [deploy/azure/README.md](../deploy/azure/README.md).
