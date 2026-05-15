# ChatGPT Developer Mode Runbook

Date: 2026-05-15

## Purpose

Finish the manual UI proof for the harmless fixture connector.

## Endpoint

Use only:

```text
https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
```

Do not use the direct Container App FQDN as the ChatGPT app URL.

## ChatGPT App Setup

1. Open ChatGPT web.
2. Go to Settings -> Apps -> Advanced settings.
3. Enable Developer Mode.
4. Create a new app.
5. MCP server URL:

```text
https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
```

6. Authentication:

```text
No Authentication
```

7. Refresh the app tools.

Expected visible tools:

```text
search
fetch
```

No `rag_*`, shell, file, ingest, delete, update, or write tools should appear.

## Manual Test

Run:

```text
Search for Remote MCP Test Note using the math RAG app.
```

Then fetch the first returned result.

Expected:

- search returns fixture results only
- fetch returns harmless fixture text only
- no local paths
- no secrets
- no private corpus/index markers

## Sanitized Transcript Shape

Save the transcript outside committed private data, then rerun the verifier with
`--manual-transcript`.

```json
{
  "created_app": true,
  "auth_mode": "No Authentication",
  "tool_list_observed": ["search", "fetch"],
  "query": "Remote MCP Test Note",
  "selected_result_id": "copied-from-search-result",
  "transcript_sanitized": "No secrets, auth material, local paths, or private corpus text.",
  "notes": "No rag_* tools visible"
}
```

Command:

```bash
math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
  --input deploy/azure/fixture_connector_verification/input/verification_input.json \
  --manual-transcript <manual_chatgpt_transcript.json> \
  --output-dir .tmp-fixture-verify
```

## Current Status

The deterministic APIM preflight passes. Manual ChatGPT UI proof is still
missing, so the current verifier decision is `blocked_pending_operator`.
