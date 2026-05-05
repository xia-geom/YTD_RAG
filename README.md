# YTD_RAG

This is the workspace/research root for the local mathematical RAG project.

There are two roots:

- `YTD_RAG/` is the workspace root. It contains `corpus/`, `.math_rag_index/`, `eval/`, `metadata/`, `agent_logs/`, `research_profile.md`, and agent configuration such as `.claude/`.
- `YTD_RAG/math_rag/` is the Python package root. It contains `pyproject.toml`, `src/math_rag/`, `tests/`, `scripts/`, and the package README.

## Normal Workflow From Workspace Root

```bash
cd /absolute/path/to/YTD_RAG

math_rag/.venv/bin/python -m math_rag.cli ingest corpus/
math_rag/.venv/bin/python -m math_rag.cli stats
math_rag/.venv/bin/python -m math_rag.cli search "Mabuchi energy convexity"
math_rag/.venv/bin/python -m math_rag.cli ask "What does the corpus say about Mabuchi energy convexity?"
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_gold_questions.yaml
```

## Equivalent Commands From Package Root

```bash
cd /absolute/path/to/YTD_RAG/math_rag
export MATH_RAG_INDEX_DIR=../.math_rag_index

python3 -m math_rag.cli ingest ../corpus/
python3 -m math_rag.cli stats
python3 -m math_rag.cli search "Mabuchi energy convexity"
python3 -m math_rag.cli ask "What does the corpus say about Mabuchi energy convexity?"
python3 -m math_rag.cli eval ../eval/toric_gold_questions.yaml
```

The package documentation lives at `math_rag/README.md`.

## Agent Logs Workflow

`agent_logs/` stores engineering memory from Codex and Claude Code work: final reports, reviews, test outputs, eval results, design decisions, known limitations, and next-step recommendations.

Agent logs are not mathematical theorem evidence. Mathematical sources remain under `corpus/`; engineering/project memory remains under `agent_logs/`.

Save a curated report:

```bash
cp /path/to/report.md agent_logs/codex/2026-05-04-symbol-normalization.md
```

Ingest and search logs:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest agent_logs/
math_rag/.venv/bin/python -m math_rag.cli search "why hits@1 dropped"
math_rag/.venv/bin/python -m math_rag.cli search "symbol normalization Codex report"
math_rag/.venv/bin/python -m math_rag.cli search "MCP server final report"
```

`ingest agent_logs/` rebuilds the selected index over logs alone. Use `--index-dir .math_rag_agent_logs_index` when you want a separate engineering-memory index.

When ingested, chunks under `agent_logs/` are tagged with `source_kind: agent_log`.
