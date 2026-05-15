# Safe Fixture ChatGPT Connector Verification

This pack verifies the harmless fixture MCP connector through the APIM endpoint
only. It is deliberately fixture-only and does not approve private-index rollout.

## Scope

Target endpoint:

```text
https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
```

Expected ChatGPT-facing tool surface:

```text
search
fetch
```

The verification does not use the direct Container App backend URL. The current
backend can still be directly reached at the network layer, so the private real
index remains blocked.

## Run

From the workspace root:

```bash
math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
  --input deploy/azure/fixture_connector_verification/input/verification_input.json \
  --output-dir <artifact-dir>
```

The script writes:

- `preflight_report.json`
- `verification_summary.json`

It performs:

- `GET /healthz`
- `GET /readyz`
- MCP `initialize`
- MCP `notifications/initialized`
- MCP `tools/list`
- MCP `tools/call search`
- MCP `tools/call fetch`
- forbidden string scan over APIM response bodies

## Manual ChatGPT Gate

The deterministic preflight cannot prove the ChatGPT Developer Mode UI can see
the tools. Create a draft app manually using:

```text
URL: https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
Authentication: No Authentication
```

Expected visible tools:

```text
search
fetch
```

Save a sanitized transcript outside the repo or in an ignored temporary
directory. A minimal transcript shape is:

```json
{
  "created_app": true,
  "auth_mode": "No Authentication",
  "tool_list_observed": ["search", "fetch"],
  "query": "Remote MCP Test Note",
  "selected_result_id": "copied-from-search-result",
  "transcript_sanitized": "No secrets, bearer material, local paths, or private corpus text.",
  "notes": "No rag_* tools visible"
}
```

Then rerun:

```bash
math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
  --input deploy/azure/fixture_connector_verification/input/verification_input.json \
  --manual-transcript /path/to/manual_chatgpt_transcript.json \
  --output-dir <artifact-dir>
```

## Decision Rules

- `go_fixture_only`: APIM preflight passes and sanitized manual ChatGPT evidence
  is present.
- `blocked_pending_operator`: APIM preflight passes but manual ChatGPT evidence
  is missing.
- `no_go`: tool surface mismatch, APIM/MCP failure, fixture search/fetch failure,
  or forbidden strings are detected.

No result from this pack approves private real-index deployment.

## Evidence Boundary

This pack is engineering verification only. Do not use it as mathematical
theorem evidence.
