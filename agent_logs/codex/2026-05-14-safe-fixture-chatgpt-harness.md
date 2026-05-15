# Agent Log: Safe Fixture ChatGPT Connector Harness

Date: 2026-05-14
Agent: Codex with read-only review subagents
Branch: `release/remote-mcp-extended-verification`
Commit: none; working tree HEAD was `e76d995`

## Status Before

The remote Streamable HTTP MCP server already existed as
`math_rag.mcp_http_server`. ChatGPT mode was expected to expose exactly
`search` and `fetch`. The live low-cost APIM path was fixture-only:

```text
ChatGPT Developer Mode app
  -> APIM Consumption /mcp with No Authentication
  -> APIM injects backend auth
  -> Container App with app-layer bearer auth
  -> harmless fixture index
```

Direct Container App ingress was still public from earlier verification, so the
private real index remained blocked.

## Goal

Create a reusable APIM-only verification pack for the final safe fixture
ChatGPT connector check, run deterministic MCP preflight, and record whether the
remaining manual ChatGPT Developer Mode gate is complete.

## Scope Guard

No retrieval, ranking, chunking, ingestion, downloader, corpus, eval, real
`.math_rag_index/index.json`, or local stdio MCP behavior was changed.

No private index was uploaded, mounted, copied, or smoke-tested.

## Changes Made

Created:

- `deploy/azure/fixture_connector_verification/README.md`
- `deploy/azure/fixture_connector_verification/verify_fixture_connector.py`
- `deploy/azure/fixture_connector_verification/input/verification_input.json`
- `deploy/azure/fixture_connector_verification/prompts/master.txt`
- `deploy/azure/fixture_connector_verification/prompts/researcher.txt`
- `deploy/azure/fixture_connector_verification/prompts/prompt_writer.txt`
- `deploy/azure/fixture_connector_verification/prompts/security_auditor.txt`
- `deploy/azure/fixture_connector_verification/prompts/test_runner.txt`
- `deploy/azure/fixture_connector_verification/prompts/synthesizer.txt`
- `deploy/azure/fixture_connector_verification/schemas/verification_input.schema.json`
- `deploy/azure/fixture_connector_verification/schemas/agent_envelope.schema.json`
- `deploy/azure/fixture_connector_verification/schemas/verification_bundle.schema.json`
- `agent_logs/codex/2026-05-14-safe-fixture-chatgpt-harness.md`

Modified:

- none outside the new verification pack and this log

## Verification Pack

The harness uses the APIM endpoint only:

```text
https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp
```

It verifies:

- `/healthz`
- `/readyz`
- MCP `initialize`
- MCP `notifications/initialized`
- MCP `tools/list`
- MCP `tools/call search`
- MCP `tools/call fetch`
- structured content and JSON fallback match for `search` and `fetch`
- no raw text in `search`
- forbidden string scan over APIM response bodies

It does not use the direct Container App URL.

## Commands Run

Repository inspection:

```bash
pwd
git branch --show-current
git rev-parse --short HEAD
git status --short
rg --files deploy/azure docs agent_logs/codex math_rag/src/math_rag math_rag/tests
```

Syntax check:

```bash
math_rag/.venv/bin/python -m py_compile deploy/azure/fixture_connector_verification/verify_fixture_connector.py
```

APIM preflight, first sandboxed attempt:

```bash
math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
  --input deploy/azure/fixture_connector_verification/input/verification_input.json \
  --output-dir <artifact-dir>
```

Result: failed with DNS resolution errors from Python networking inside the
sandbox. No forbidden strings were detected.

Control health checks with `curl`:

```bash
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/healthz
curl -i -sS https://apim-math-rag-mcp-5d67a258.azure-api.net/readyz
```

Result: both returned `200 OK`.

APIM preflight with approved network access for the Python harness:

```bash
math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
  --input deploy/azure/fixture_connector_verification/input/verification_input.json \
  --output-dir <artifact-dir>
```

Focused regression:

```bash
math_rag/.venv/bin/python -m pytest math_rag/tests/test_mcp_http_server.py -q
```

Pack scan:

```bash
rg -n "<secret/path marker regex>" deploy/azure/fixture_connector_verification
```

The hits were the intentional forbidden-string blocklist entries in
`verification_input.json`.

Post-review hardening:

```bash
math_rag/.venv/bin/python -m py_compile deploy/azure/fixture_connector_verification/verify_fixture_connector.py
math_rag/.venv/bin/python -m json.tool deploy/azure/fixture_connector_verification/input/verification_input.json
math_rag/.venv/bin/python -m json.tool deploy/azure/fixture_connector_verification/schemas/verification_input.schema.json
rg -n "<local path marker regex>" deploy/azure/fixture_connector_verification agent_logs/codex/2026-05-14-safe-fixture-chatgpt-harness.md
math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
  --input deploy/azure/fixture_connector_verification/input/verification_input.json \
  --output-dir <artifact-dir>
```

Changes from security review:

- removed absolute artifact paths from committed docs/log text
- added configured APIM host validation before any network probes
- added `fetch_max_chars=12000` verification
- sanitized manual transcript path storage in the report

## Test Results

Focused pytest:

```text
14 passed in 0.87s
```

Full `math_rag/tests` was not run because this sprint only added an external
verification harness and did not change package behavior.

## APIM Preflight Results

Artifact directory:

```text
<artifact-dir>
```

Summary:

```json
{
  "decision": "blocked_pending_operator",
  "preflight_overall": "pass",
  "manual_chatgpt_status": "blocked",
  "tool_names_observed": ["search", "fetch"],
  "search_result_count": 4,
  "fetch_text_length": 287,
  "fetch_max_chars": 12000,
  "secret_scan_status": "pass",
  "secret_scan_hits": [],
  "private_real_index_status": "blocked_not_tested"
}
```

Detailed checks:

- configured URL host policy: pass, all configured URLs use the APIM host
- `/healthz`: `200 OK`, fixture counts only: 4 chunks, 2 sources
- `/readyz`: `200 OK`
- MCP `initialize`: `200 OK`
- MCP session header: present
- `notifications/initialized`: `202`
- `tools/list`: exactly `search`, `fetch`
- `search("Remote MCP Test Note")`: 4 fixture results
- `fetch(first_result_id)`: fixture result fetched, 287 text characters under
  the 12000-character verification cap
- forbidden string scan: pass

## ChatGPT Draft App Result

Not run in this task. The final end-to-end decision is therefore
`blocked_pending_operator`, not `go_fixture_only`.

Manual next input needed:

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

## Current Status After Task

`SAFE_FOR_APIM_FIXTURE`: yes, based on deterministic APIM preflight.

`SAFE_FOR_CHATGPT_DEVELOPER_TEST`: blocked pending manual ChatGPT Developer Mode
evidence.

`SAFE_FOR_PRIVATE_REAL_INDEX`: no.

`NOT_PRODUCTION_READY`: yes.

## Review Handoffs

Read-only review agents checked:

- APIM preflight evidence: confirmed health, readiness, initialize,
  initialized notification, `tools/list`, `search`, `fetch`, and forbidden scan
  all passed for the fixture endpoint.
- Docs and decision language: confirmed fixture-only scope, APIM-only URL, No
  Authentication for ChatGPT Developer Mode, expected `search`/`fetch` tools,
  manual transcript requirement, and private real-index block.
- Security hardening: initial review found local artifact path references and no
  configured-host proof; follow-up review confirmed those blockers were resolved
  by APIM host validation, relative default artifact path, sanitized transcript
  path output, and explicit fetch cap enforcement.

## Known Limitations

- The direct Container App backend remains public from prior verification.
- The harness intentionally does not test or use the direct backend URL.
- The harness does not prove ChatGPT UI behavior without a sanitized manual
  transcript.
- This task did not run full package tests.
- This task did not create, update, or delete Azure resources.

## Recommended Next Step

Create a ChatGPT Developer Mode draft app using the APIM `/mcp` URL with No
Authentication, capture a sanitized transcript showing exactly `search` and
`fetch`, then rerun the harness with `--manual-transcript`.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
