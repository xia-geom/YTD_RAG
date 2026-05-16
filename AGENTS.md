# Agent Notes

This file is the short operating guide for coding agents working in this repository. Keep detailed user-facing documentation in `README.md`, `math_rag/README.md`, and `agent_logs/README.md`.

## Project Roots

- `YTD_RAG/` is the workspace and Git root. It contains `corpus/`, `.math_rag_index/`, `eval/`, `metadata/`, `agent_logs/`, and project-level docs.
- `YTD_RAG/math_rag/` is the Python package root. It contains `pyproject.toml`, `src/math_rag/`, and `tests/`.
- Run normal project commands from the workspace root unless a task explicitly says otherwise.

## Remote MCP Connector

- Current safe lane is fixture/public-safe only: ChatGPT Developer Mode connects to `https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp` with `No Authentication`.
- Expected ChatGPT-facing tools are exactly `search` and `fetch`; internal `rag_*` tools must not be exposed to ChatGPT mode.
- Current live data is the harmless fixture index only unless a later task explicitly approves a reviewed public-safe index.
- Verify the APIM fixture connector with:
  ```bash
  math_rag/.venv/bin/python deploy/azure/fixture_connector_verification/verify_fixture_connector.py \
    --input deploy/azure/fixture_connector_verification/input/verification_input.json \
    --output-dir .tmp-fixture-verify
  ```
- Manual ChatGPT gate: create a draft app with the APIM `/mcp` URL, confirm exactly `search` and `fetch`, save a sanitized transcript, then rerun the verifier with `--manual-transcript`.
- Do not mount, deploy, upload, or expose the private real `.math_rag_index`; direct Container App ingress remains a blocker for private data.
- Private rollout requires network isolation plus OAuth/JWT validation; do not treat the current APIM Consumption fixture path as private-index ready.
- A personal risk-accepted private-index pilot is allowed only when explicitly requested: require APIM OAuth/JWT validation, backend bearer auth, `MATH_RAG_PROTECT_HEALTH=true`, read-only index mount, and a log that states the public-backend residual risk.
- Source-of-truth references: `findings/summary.md`, `findings/chatgpt_runbook.md`, `findings/private_lane.md`, and `agent_logs/codex/2026-05-15-mcp-connector-finalization.md`.

## Multi-Agent Use

- Multi-agent work is encouraged whenever the acting agent judges it useful for quality, speed, review, or independent inspection.


## Agent Logs

- For non-trivial implementation, audit, review, eval, retrieval, deployment-prep, or design-decision work, save a Markdown report under `agent_logs/codex/` or `agent_logs/claude/`.
- Use `agent_logs/templates/agent_log_template.md`.
- Filename format: `agent_logs/codex/YYYY-MM-DD-short-task-slug.md`.
- Example for the current MCP connector status work: `agent_logs/codex/2026-05-15-mcp-connector-finalization.md`.

## Agent Log Behavior

- Important completed tasks should produce a status-first log.
- Do not write long speculative plans in `agent_logs/`.
- Keep `Recommended Next Step` short.
- Record actual commands and test or eval results.
- Say `Not run` honestly when tests or evals were not run.
- Do not claim deployment or security guarantees unless they were actually verified.

## What To Log

- Goal and scope.
- Status before the task when relevant.
- Files created and files modified.
- Files removed or renamed when relevant.
- Commands run.
- Test results and eval results.
- Current status after the task.
- Known limitations.
- Recommended next step.

## What Not To Log

- Secrets, API keys, tokens, private credentials, or `.env` contents.
- Raw noisy chat transcripts unless intentionally curated.
- Corpus papers, PDFs, arXiv downloads, or generated indexes.
- Mathematical claims presented as proof evidence.

## Evidence Boundary

- Agent logs are engineering memory only.
- Do not cite agent logs as evidence that a theorem is true, a proof is complete, a paper proves a claim, or a mathematical result is novel.
- Mathematical evidence belongs in `corpus/` sources and reviewed research notes, not in `agent_logs/`.

## Safety Rules

- Do not commit generated or private data: `corpus/arxiv/`, `.math_rag_index/`, `.math_rag_agent_logs_index/`, virtualenvs, PDFs, `.env`, caches, build outputs, or secrets.
- Do not commit automatically. Make commits only when the user explicitly asks for a commit.
- Do not change retrieval ranking, chunking, downloader behavior, MCP behavior, or deployment behavior unless the task asks for it.
- Do not delete or rewrite user data without explicit approval.

## Validation Defaults

- For package changes, run:
  `math_rag/.venv/bin/python -m pytest math_rag/tests`
- For retrieval, index, or ranking work, also run:
  `math_rag/.venv/bin/python -m math_rag.cli stats`
  `math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml`
- For documentation-only edits, pytest is optional; at minimum inspect the changed docs and check `git status --short`.

## Final Response Checklist

- Report files created and modified.
- Report tests, stats, and eval commands run, or say why they were not run.
- Report known limitations.
- Confirm generated/private files were avoided when relevant.
- Recommend exactly one next task when useful.
