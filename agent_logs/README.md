# Agent Logs

`agent_logs/` stores engineering memory from coding-agent work on this project.

These logs exist because ChatGPT, Codex, and Claude Code do not share private chat history automatically. When an agent produces a useful final report, review, test summary, eval result, design decision, or limitation analysis, save the useful part here as Markdown so it can be searched later through `math_rag`.

## What To Save

- Codex final reports
- Claude Code reviews
- git diff summaries
- pytest outputs
- eval results
- implementation plans
- design decisions
- known limitations
- recommended next steps

## What Not To Save

- private credentials, API keys, or tokens
- raw private chat logs unless they are intentionally curated
- large noisy transcripts with no durable project value
- mathematical claims copied here as if they were paper evidence
- arXiv/source downloads, which belong under `corpus/`

## Evidence Boundary

Agent logs are engineering memory, not mathematical theorem evidence. They may explain why the codebase changed, what tests passed, or what an agent recommended. They should not be cited as evidence that a theorem is true, that a paper proves a claim, or that a mathematical argument is complete.

Mathematical sources remain under `corpus/`. Agent logs remain under `agent_logs/`.

When ingested, chunks from this folder are tagged with:

```yaml
source_kind: agent_log
```

## Structure

```text
agent_logs/
  codex/
  claude/
  decisions/
  templates/
```

Use `codex/` for Codex reports, `claude/` for Claude Code reviews, and `decisions/` for durable project decisions.

## Save A Report

```bash
cp /path/to/report.md agent_logs/codex/2026-05-04-symbol-normalization.md
```

Use a date prefix and a short slug so logs sort naturally.

## Ingest Logs

From `WORKSPACE_ROOT`:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest agent_logs/
```

This rebuilds the default index over the logs alone. To avoid replacing the mathematical corpus index, use a separate index directory:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest agent_logs/ --index-dir .math_rag_agent_logs_index
math_rag/.venv/bin/python -m math_rag.cli search "why hits@1 dropped" --index-dir .math_rag_agent_logs_index
```

To search both mathematical corpus and agent logs in one index, ingest a parent folder that contains both, or use separate indexes deliberately.

## Search Logs

```bash
math_rag/.venv/bin/python -m math_rag.cli search "why hits@1 dropped"
math_rag/.venv/bin/python -m math_rag.cli search "symbol normalization Codex report"
math_rag/.venv/bin/python -m math_rag.cli search "MCP server final report"
```

MCP prompt example:

```text
Use math-rag to find the latest Codex report about symbol normalization and summarize what changed.
```

Remember: search results from `agent_logs/` are project memory, not mathematical evidence.
