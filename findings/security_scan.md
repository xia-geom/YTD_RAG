# Security Scan Findings

Date: 2026-05-15

## Deterministic Fixture Payload Scan

Command:

```bash
rg -n '(/Users/|/home/|/mnt/data/|/private/tmp/|file://|corpus/arxiv|corpus/my_notes|\.math_rag_index|OPENAI_API_KEY|MATH_RAG_API_TOKEN|MATH_RAG_API_KEY|AZURE_|mathragapitoken|math-rag-backend-token|Bearer |sk-|\.env)' .tmp-fixture-verify
```

Result:

```text
no matches
```

The fixture verifier also reported:

```json
{
  "secret_scan_status": "pass",
  "secret_scan_hits": []
}
```

## Repository Scan Notes

Repo-wide scans find many expected documentation and test references to env var
names, placeholder tokens, historical logs, and local smoke commands. Those are
not evidence of payload leakage, but they should not be confused with deployable
secrets.

The new fixture verification pack keeps the forbidden strings as intentional
blocklist entries in:

```text
deploy/azure/fixture_connector_verification/input/verification_input.json
```

## Tool Surface Safety

Live APIM preflight observed:

```text
search
fetch
```

No internal `rag_*` tools were observed through APIM.

## Remaining Risk

The direct Container App FQDN remains public. App-layer bearer protects `/mcp`,
but this is still not sufficient for private real-index rollout because a holder
of the backend credential could bypass APIM.

## Handoff

Status: payload/path/secret scan passes for fixture APIM artifacts. Private
real-index rollout remains blocked.
