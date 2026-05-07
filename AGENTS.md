# Agent Notes

This file is the short operating guide for coding agents working in this repository. Keep detailed user-facing documentation in `README.md`, `math_rag/README.md`, and `agent_logs/README.md`.

## Project Roots

- `YTD_RAG/` is the workspace and Git root. It contains `corpus/`, `.math_rag_index/`, `eval/`, `metadata/`, `agent_logs/`, and project-level docs.
- `YTD_RAG/math_rag/` is the Python package root. It contains `pyproject.toml`, `src/math_rag/`, and `tests/`.
- Run normal project commands from the workspace root unless a task explicitly says otherwise.

## Multi-Agent Use

- Multi-agent work is allowed whenever the acting agent judges it useful for quality, speed, review, or independent inspection.
- When using subagents, keep tasks bounded and report material findings in the final answer or an agent log.

## Agent Logs

- For non-trivial implementation, audit, review, eval, retrieval, deployment-prep, or design-decision work, save a Markdown report under `agent_logs/codex/` or `agent_logs/claude/`.
- Use `agent_logs/templates/agent_log_template.md`.
- Filename format: `agent_logs/codex/YYYY-MM-DD-short-task-slug.md`.
- Example for the current Azure prep work: `agent_logs/codex/2026-05-07-azure-remote-mcp-prep.md`.

## What To Log

- Goal and scope.
- Files created and files modified.
- Commands run.
- Test results and eval results.
- Important decisions and tradeoffs.
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
