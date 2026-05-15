# APIM Policy Findings

Date: 2026-05-15

## Azure Inspection

Container App:

```json
{
  "external": true,
  "fqdn": "math-rag-mcp-test.bravehill-bd729733.canadacentral.azurecontainerapps.io",
  "ipSecurityRestrictions": null,
  "targetPort": 8000
}
```

APIM:

```json
{
  "gatewayUrl": "https://apim-math-rag-mcp-5d67a258.azure-api.net",
  "publicNetworkAccess": "Enabled",
  "sku": "Consumption",
  "virtualNetworkType": "None"
}
```

APIM API mappings:

```text
math-rag-healthz -> /healthz -> Container App public FQDN
math-rag-mcp     -> /mcp     -> Container App public FQDN
math-rag-readyz  -> /readyz  -> Container App public FQDN
```

## Current /mcp Policy

The live policy is a No Authentication facade. It rewrites public `/mcp` to
backend `/mcp` and injects a backend auth header from an APIM named value. The
named value itself was not read or printed.

Sanitized current shape:

```xml
<policies>
  <inbound>
    <base />
    <set-header name="Authorization" exists-action="override">
      <value>Bearer {{<backend-token-named-value>}}</value>
    </set-header>
    <rewrite-uri template="/mcp" copy-unmatched-params="true" />
  </inbound>
  <backend>
    <base />
  </backend>
  <outbound>
    <base />
  </outbound>
  <on-error>
    <base />
  </on-error>
</policies>
```

`validate-jwt` is not present in the live No Auth fixture policy.

## Current Lane Requirement

For harmless fixture or explicitly reviewed public-safe data, this APIM shape is
sufficient:

- `set-header` to inject backend auth.
- `rewrite-uri` to `/mcp`.
- backend service URL configured on the APIM API.
- no ChatGPT-side authentication.

`set-backend-service` is optional if the APIM API `serviceUrl` is already set.
It would be useful only if the policy itself must override or route to a
different backend.

## Private Lane Requirement

For the private real index, the current policy is not sufficient. Required
additions:

- gateway auth such as `validate-jwt` or `validate-azure-ad-token`
- issuer, audience/resource, expiry, and scope checks
- preferably a private/internal backend path instead of a public Container App
  FQDN
- backend app-layer bearer retained as defense in depth or replaced with a
  private backend credential path

## Handoff

Status: current APIM policy is correct for fixture/public-safe testing; private
real index remains blocked because the backend is public and no JWT validation
is active.
