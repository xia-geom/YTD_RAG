# Agent Log: Legacy Project Cleanup

Date: 2026-10-02
Agent: Codex
Branch: `codex/private-index-risk-accepted-pilot`
Commits: `9589640` (code/tests), `438aaa4` (obsolete files); architecture, guides, and this report are committed together separately at the user's request.
Related files: `ARCHITECTURE.md`, `README.md`, `math_rag/README.md`, package source/tests, remote guides.

## Current Status After Task

- Implemented: one argparse CLI, one dataclass model implementation, smaller dependency extras, clear architecture and command reference; removed 41 obsolete tracked files.
- Tested: 208 package tests pass; local fixture MCP smoke passes; core retrieval metrics are unchanged.
- Working: local research commands and both retained MCP interfaces; remote serving remains recorded as paused.
- Not implemented: removal of the legacy remote adapter, which contains pre-existing uncommitted work; no ranking/downloader/transport redesign.
- Blocked: nothing required for this cleanup.
- Risk / caveat: model annotations no longer apply optional Pydantic coercion/validation. Valid persisted records retain their schema and values. No cloud or container deployment was performed.

## Status Before

The workspace had 196 passing tests and substantial existing dirty retrieval,
remote-adapter, documentation, and report changes. The CLI duplicated twelve
commands across Typer and argparse. Models changed implementation depending on
whether Pydantic happened to be installed. Documentation repeated setup and
remote deployment narratives, including states superseded by the recorded
2026-05-18 pause.

## Goal of This Task

Simplify the legacy project and provide an architecture file. The user selected
retaining local research tools and paused remote MCP support while deleting
duplication, dead code, unnecessary reports, and runtime leftovers.

## Changes Made

### Files Created

- `ARCHITECTURE.md`: data flow, responsibilities, storage, dependencies, interface boundaries, and limitations.
- `math_rag/tests/test_cli.py`: public CLI workflow and argument/error coverage.
- `math_rag/tests/test_models.py`: persisted JSON compatibility and serialization/default isolation.
- This status report.

### Files Modified

- `README.md`, `math_rag/README.md`: concise setup and command reference; migration notes for removed scripts/extras and dataclass behavior. Preserved the intent of existing remote-auth/private-index safety additions.
- `math_rag/src/math_rag/cli.py`: removed Typer/Rich frontends; all commands use public `main(argv)` and argparse with unchanged options/defaults.
- `math_rag/src/math_rag/models.py`: dataclasses only; retained schema version 1, known fields/defaults, and ignoring unknown persisted fields as in the former Pydantic path.
- `math_rag/src/math_rag/config.py`: removed unused `local_only` flag.
- `math_rag/src/math_rag/discovery.py`, `paper_ranker.py`: removed unused import and unreferenced `config_to_dict` helper.
- `math_rag/src/math_rag/rag_service.py`: corrected return-type documentation only.
- `math_rag/src/math_rag/pdf_loader.py`, `math_rag/.env.example`: current install/config guidance.
- `math_rag/pyproject.toml`: supported extras now `pdf`, `remote-mcp`, `dev`; removed Typer, Rich, direct Pydantic, rank-bm25, and sentence-transformers declarations.
- Existing `test_arxiv_downloader.py`, `test_eval.py`, `test_evidence_eval.py`, `test_metadata_enrichment.py`: call public CLI entrypoint.
- `docs/remote_mcp_server.md`, `docs/azure_remote_mcp_readiness.md`, `deploy/azure/README.md`: separate server reference, deployment gates, and operational assets; mark recorded pause and distinguish fixture/private lanes.
- `deploy/azure/fixture_connector_verification/README.md`, `input/verification_input.json`: pause guidance and removal of eight unused config fields. All eleven consumed keys retain their values; verifier implementation unchanged.
- `findings/summary.md`, `findings/chatgpt_runbook.md`, `findings/private_lane.md`: historical/pause banners; original bodies preserved.
- `.gitignore`: ignore generated `.tmp-*/` directories.

### Files Removed / Renamed

41 tracked files removed; no renames:

- Three redundant launchers: `math_rag/scripts/ask.py`, `search.py`, `build_index.py`.
- Six unused verifier `prompts/*.txt` and three unused `schemas/*.schema.json`.
- `findings/final_prompt.txt`.
- Nineteen explicitly superseded files under `agent_logs/codex/archive/2026-05-15-mcp-history/` (eighteen dated reports and its README).
- Nine duplicate findings: `apim_policy.md`, `azure_deploy.md`, `chatgpt_operator.md`, `current_state.md`, `final_public_safe_go_no_go.md`, `index_audit.md`, `mcp_protocol_test.md`, `payload_security.md`, `security_scan.md`.

The retained May 15 finalization, May 16 public-safe deployment, and May 18 pause
reports contain the durable deployment facts. Historical inventories may still
name deleted files; they describe past work, not active instructions. Deleted
tracked reports remain recoverable from Git history.

Removed these twelve generated/cache items (1,253,233 bytes total):

- `.DS_Store`
- `.archive/2026-05-15-local-cleanup/.pytest_cache`
- `.archive/2026-05-15-local-cleanup/math_rag.build`
- `.archive/2026-05-15-local-cleanup/math_rag.pytest_cache`
- `.tmp-azure-test-index`
- `deploy/azure/__pycache__`
- `deploy/azure/fixture_connector_verification/__pycache__`
- `math_rag/.DS_Store`
- `math_rag/.pytest_cache`
- `math_rag/scripts/__pycache__`
- `math_rag/src/math_rag/__pycache__`
- `math_rag/tests/__pycache__`

Private corpus/index data, metadata, candidate approvals, eval inputs, research
profile, virtualenv, nested Git backup, and archived operational evidence were
preserved. No generated/private data was staged or committed.

## Commands Run

From the workspace root:

```bash
git status --short
git diff --stat
git diff --check
math_rag/.venv/bin/python -m pytest math_rag/tests
math_rag/.venv/bin/python -m math_rag.cli --help
math_rag/.venv/bin/python -m math_rag.cli stats
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
math_rag/.venv/bin/python deploy/azure/local_remote_mcp_smoke_test.py
```

Additional checks used Python scripts for protected-file SHA-256 comparison,
Markdown link resolution, TOML parsing and entrypoint imports, verifier config
consumer inspection, and deletion of the exact generated/cache paths above.
Scoped CLI/model tests were run during implementation before the final suite.

## Test Results

- Initial suite: 196 passed in 117.39 seconds.
- CLI/eval/enrichment/downloader focused suite: 67 passed.
- Model/loader/enrichment/discovery/MCP focused suite: 91 passed.
- Final working-tree suite (including preserved pre-existing changes): 208 passed in 5.40 seconds. Timing is recorded, not a performance claim.
- Local fixture smoke: 2 sources, 4 chunks; ChatGPT tools exactly `search`, `fetch`; internal read-only tools also passed.
- Protected-file hashes: 510 checked, zero changes, including all corpus/index/metadata files and pre-existing dirty runtime files/reports.
- Active Markdown links in seven guides resolve; no active references to deleted reports/assets found.
- TOML and all three console entrypoint targets verified; `git diff --check` passed.
- A setuptools metadata check was attempted but could not import setuptools from this virtualenv. TOML parsing/entrypoint checks passed instead; a wheel build or fresh dependency install was not run.

## Eval Results

Before and after cleanup, on the unchanged local index:

- Sources: 104; chunks: 18,544.
- Questions: 42 total; 39 positive; 3 negative.
- hits@1: 21/39 = 0.538.
- hits@3: 28/39 = 0.718.
- hits@5: 32/39 = 0.821.
- Missing expected sources: none.

These are retrieval regression metrics, not mathematical proof evidence.

## Known Limitations / Open Issues

Remote Azure state was not queried; the recorded pause is not a fresh cloud
verification. Docker build and live APIM/ChatGPT verification were not run.
The older remote adapter and original unrelated dirty work remain intentionally
untouched. Runtime model type coercion/validation is no longer supplied by
optional Pydantic. The CLI continues to use explicit `--index-dir`; this task
did not change environment/default resolution or retrieval behavior.

## Commit Validation

The user subsequently requested committing and syncing. Fetched `origin` and
confirmed the current branch had no upstream and no new remote commits to
integrate. Staged only cleanup-owned files; excluded the pre-existing retrieval,
remote-adapter, Docker-ignore, agent-log workflow, and older untracked changes.

Exported the staged index to `/tmp/ytd-rag-commit-check-h8rs4_km` with
`git checkout-index --all --prefix=...` and ran the project virtualenv's Python
with `PYTHONPATH` set to that snapshot's `math_rag/src`:

```bash
python -m pytest math_rag/tests -p no:cacheprovider
python deploy/azure/local_remote_mcp_smoke_test.py
```

- Isolated staged suite: 192 passed in 2.61 seconds. The 16 additional tests in
  the working-tree result belong to pre-existing uncommitted retrieval/MCP work.
- Isolated local MCP smoke: passed with two fixture sources/four chunks and
  exactly `search`/`fetch`. The first attempt lacked the helper's expected
  `.venv` path; linking the existing interpreter environment into the temporary
  snapshot resolved that setup issue. No project code changed for it.
- Reviewed `git diff --cached --name-only`, `--stat`, and `--check` before each
  scoped commit. No corpus, indexes, PDFs, credentials, or generated artifacts
  were included.
- Removed the architecture reference to the excluded local `query_expansion.py`
  experiment so the published guide matches a clean checkout.

## Recommended Next Step

Review the preserved legacy remote-adapter changes before deciding whether to retire that adapter.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
