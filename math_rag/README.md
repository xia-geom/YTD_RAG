# math_rag

`math_rag` is a local-first retrieval assistant for mathematical research notes. It ingests LaTeX, Markdown, text, BibTeX, and PDF files, chunks them with math-aware heuristics, builds a local searchable index, and answers questions by showing retrieved passages with citations.

RAG means retrieval-augmented generation. In this project, the important part is retrieval: the system searches your own corpus and uses only retrieved chunks to prepare a structured report. It is not a proof checker and does not certify theorem correctness.

## Roots And Layout

This repository intentionally has two roots:

- `WORKSPACE_ROOT`: the directory containing `corpus/`, `.math_rag_index/`, `eval/`, `metadata/`, `agent_logs/`, and `research_profile.md`.
- `PACKAGE_ROOT`: the directory containing `pyproject.toml`, `src/math_rag/`, `tests/`, and this README.

In the current checkout:

```text
WORKSPACE_ROOT/
  corpus/
  .math_rag_index/
  eval/
  metadata/
  agent_logs/
  research_profile.md
  math_rag/              <- PACKAGE_ROOT
    pyproject.toml
    src/math_rag/
    tests/
    scripts/
```

When a command is shown below, its working directory is stated explicitly. If you run from `PACKAGE_ROOT` but want to use the workspace index, set `MATH_RAG_INDEX_DIR=../.math_rag_index` or pass `--index-dir ../.math_rag_index`.

## Minimum Successful Demo

From `WORKSPACE_ROOT`:

```bash
cd /absolute/path/to/YTD_RAG

math_rag/.venv/bin/python -m math_rag.cli ingest corpus/
math_rag/.venv/bin/python -m math_rag.cli stats
math_rag/.venv/bin/python -m math_rag.cli search "Mabuchi energy convexity"
math_rag/.venv/bin/python -m math_rag.cli ask "What does the corpus say about Mabuchi energy convexity?"
```

Equivalent from `PACKAGE_ROOT`:

```bash
cd /absolute/path/to/YTD_RAG/math_rag
export MATH_RAG_INDEX_DIR=../.math_rag_index

python3 -m math_rag.cli ingest ../corpus/
python3 -m math_rag.cli stats
python3 -m math_rag.cli search "Mabuchi energy convexity"
python3 -m math_rag.cli ask "What does the corpus say about Mabuchi energy convexity?"
```

## Install

Recommended Python versions are 3.11 or 3.12. Python 3.13 may work, but editable installs may require explicitly setting `PYTHONPATH`, especially for MCP usage.

From `PACKAGE_ROOT`:

```bash
cd /absolute/path/to/YTD_RAG/math_rag

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

The base install is dependency-light and local. To install preferred terminal, metadata, PDF, and test libraries:

```bash
python3 -m pip install -e ".[preferred,dev]"
```

For future local embedding experiments:

```bash
python3 -m pip install -e ".[full]"
```

In this first version, `--mode vector` does not use neural embeddings. It is a deterministic sparse vector-style retriever. Dense embedding backends can be added later.

## Add Documents

Place research files under `WORKSPACE_ROOT/corpus/`, or pass another folder to the CLI. Supported first-version formats:

- `.tex`
- `.md`, `.markdown`
- `.txt`
- `.bib`
- `.pdf` if `pypdf` is installed

Optional document metadata can be stored under `WORKSPACE_ROOT/metadata/documents.yaml`; see `WORKSPACE_ROOT/metadata/documents.example.yaml`.

## Build The Index

From `WORKSPACE_ROOT`:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/
math_rag/.venv/bin/python -m math_rag.cli stats
```

From `PACKAGE_ROOT`:

```bash
export MATH_RAG_INDEX_DIR=../.math_rag_index
python3 -m math_rag.cli ingest ../corpus/
python3 -m math_rag.cli stats
```

The default index is local and written to `.math_rag_index/index.json` relative to the current working directory unless `MATH_RAG_INDEX_DIR` or `--index-dir` is set.

## Search And Ask

Hybrid search is the default because mathematical retrieval needs exact names/symbols and sparse similarity:

```bash
# From WORKSPACE_ROOT
math_rag/.venv/bin/python -m math_rag.cli search "Mabuchi energy convexity"
math_rag/.venv/bin/python -m math_rag.cli search "Chen-Cheng" --mode keyword
math_rag/.venv/bin/python -m math_rag.cli search "cusp limit of conic toric metrics" --mode vector
```

Again, `--mode vector` means the deterministic sparse vector-style retriever, not sentence-transformers or dense neural embeddings.

Ask uses retrieved chunks to produce a conservative structured report:

```bash
# From WORKSPACE_ROOT
math_rag/.venv/bin/python -m math_rag.cli ask "What sources discuss cusp limits of conic metrics?"
```

The answer layer separates retrieved evidence, corpus-supported statements, cautious inference, and claims not established by the retrieved sources.

## Seeded arXiv Corpus

For an initial research corpus, prefer a curated arXiv seed list over broad discovery. A seed list starts from papers you already trust, avoids noisy query matches, and makes the first corpus reproducible.

Privacy note: these commands contact arXiv. Discovery sends search queries/config-derived terms; download sends arXiv IDs. Private corpus contents are not sent unless you put private information into the query/config yourself.

From `WORKSPACE_ROOT`, create `arxiv_seed_core.txt` with one arXiv ID per line:

```text
# comments and blank lines are ignored
1711.08424
1711.08424v2
math/0407486
dg-ga/9711014
```

Download the seed list:

```bash
math_rag/.venv/bin/python -m math_rag.cli download-seed arxiv_seed_core.txt
```

By default, `download-seed` downloads or records at most 10 new papers per run. For a larger seed list:

```bash
math_rag/.venv/bin/python -m math_rag.cli download-seed arxiv_seed_core.txt --max-papers 50
```

Download exact IDs directly:

```bash
math_rag/.venv/bin/python -m math_rag.cli download-arxiv 1711.08424 math/0407486 dg-ga/9711014
```

Then ingest:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/
math_rag/.venv/bin/python -m math_rag.cli stats
```

Unversioned IDs resolve to the version returned by arXiv at download time; use `vN` when reproducibility matters. Old-style IDs are preserved in metadata and stored in filesystem-safe folders. Existing paper folders are skipped by default and are never silently overwritten; use `--force` only for intentional replacement.

The downloader is polite: it serializes arXiv requests, enforces a delay between requests, backs off on HTTP 429, and records metadata. TeX source is preferred for ingestion; PDF is used as fallback when available.

## Automatic Paper Discovery And Download

`math_rag` can discover candidate papers from arXiv, rank them, and download only papers you approve:

```text
discover -> rank -> review/approve -> download -> ingest -> search/ask
```

Privacy note: these commands contact arXiv. Discovery sends search queries/config-derived terms; download sends arXiv IDs. Private corpus contents are not sent unless you put private information into the query/config yourself.

From `WORKSPACE_ROOT`:

```bash
math_rag/.venv/bin/python -m math_rag.cli discover "constant scalar curvature Kahler toric" --verbose
```

Or from `PACKAGE_ROOT` with a workspace metadata config:

```bash
cp ../metadata/discovery_config.example.yaml ../metadata/discovery_config.yaml
python3 -m math_rag.cli discover --config ../metadata/discovery_config.yaml --index-dir ../.math_rag_index
```

Discovery writes `discovered_papers.yaml` in the current working directory. Review candidates:

```bash
math_rag/.venv/bin/python -m math_rag.cli review-candidates discovered_papers.yaml
```

Then manually edit selected entries:

```yaml
action: download
```

Download only approved papers:

```bash
math_rag/.venv/bin/python -m math_rag.cli download-approved discovered_papers.yaml
```

By default, `download_policy.require_approval: true` blocks downloads of pending candidates, even if `--auto-download` is passed. Keep this enabled for normal use.

## MCP Integration

`math_rag` ships with a local stdio MCP server so Codex or Claude Code can query the local RAG index directly.

The MCP server exposes read-only tools by default:

- `rag_search`: search the indexed corpus and return ranked chunks with snippets and provenance.
- `rag_ask`: produce a retrieval-grounded structured answer.
- `rag_get_chunk`: return full content and metadata for one indexed chunk id.
- `rag_list_sources`: list indexed sources, optionally filtered by substring.

The agent cannot freely read arbitrary files or execute shell commands. It can only query content already included in the `math_rag` index through bounded RAG tools. "Read-only" means no filesystem writes and no ingestion/write tools unless explicitly enabled; it does not mean the agent sees nothing from the corpus.

When `MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true`, the following additional tool is exposed:

- `rag_ingest`: re-ingest a local corpus path into the configured index.

`rag_ingest` accepts only relative paths and validates them with `Path.resolve()` against the workspace root. Absolute paths and path traversal outside the workspace root are rejected.

### MCP Root Resolution

Use explicit environment variables:

- `MATH_RAG_PACKAGE_ROOT`: path to `YTD_RAG/math_rag`.
- `MATH_RAG_WORKSPACE_ROOT`: path to `YTD_RAG`.
- `MATH_RAG_INDEX_DIR`: optional override; defaults to `MATH_RAG_WORKSPACE_ROOT/.math_rag_index`.

`MATH_RAG_ROOT` is still accepted as a legacy fallback. If it points to the package root, the server uses its parent as the workspace root when that parent looks like the workspace. Prefer the explicit variables above.

Codex example:

```bash
codex mcp add math-rag \
  --env MATH_RAG_PACKAGE_ROOT=/absolute/path/to/YTD_RAG/math_rag \
  --env MATH_RAG_WORKSPACE_ROOT=/absolute/path/to/YTD_RAG \
  --env MATH_RAG_INDEX_DIR=/absolute/path/to/YTD_RAG/.math_rag_index \
  --env PYTHONPATH=/absolute/path/to/YTD_RAG/math_rag/src \
  -- \
  /absolute/path/to/YTD_RAG/math_rag/.venv/bin/python \
  -m math_rag.mcp_server
```

Claude Code example:

```bash
claude mcp add --transport stdio math-rag -- \
  /absolute/path/to/YTD_RAG/math_rag/.venv/bin/python \
  -m math_rag.mcp_server
```

For Claude Code, configure the same environment variables in the place where that MCP command is launched.

Security limits:

- No shell execution is exposed by MCP.
- No arbitrary filesystem reads are exposed by MCP.
- arXiv discovery/download tools are not exposed through MCP.
- Tool responses are capped in size; use `rag_get_chunk` for a specific retrieved chunk.
- Source filters are substrings used against indexed source paths, not shell commands.

## Evaluation

Before changing ranking, embeddings, or answer-generation layers, validate whether the corpus retrieves sources you already expect.

From `WORKSPACE_ROOT`:

```bash
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
```

Gold files use this shape:

```yaml
questions:
  - id: abreu_equation
    question: "Where does the corpus discuss the Abreu equation?"
    expected_sources:
      - "math_0407486"
      - "0805.0128"

  - id: negative_new_theorem
    question: "Does the corpus contain a complete proof of my own new theorem?"
    expected_sources: []
    negative: true
```

The current eval is source-level retrieval evaluation:

- it checks whether expected source identifiers appear in the top-k source paths;
- it reports `hits@1`, `hits@3`, `hits@5`;
- negative questions are excluded from the hit-rate denominators.

It does not guarantee that the correct passage inside the paper was retrieved. Future eval could add expected text patterns, expected chunk types, or passage-level checks.

Metrics from different eval versions should not be compared blindly. A stable core eval is for regression tracking; expanded/topic evals are for checking coverage as the corpus grows.

## Agent Logs Workflow

Agent logs are curated Markdown records of coding-agent work: Codex final reports, Claude Code reviews, git diff summaries, pytest outputs, eval results, design decisions, known limitations, and recommended next steps.

Direct access to private Codex or Claude Code chat state is not assumed. Save only the useful final/report material manually under `WORKSPACE_ROOT/agent_logs/`:

```text
agent_logs/
  codex/
  claude/
  decisions/
  templates/
```

Agent logs are engineering memory, not mathematical theorem evidence. They must not be cited as evidence for theorem statements, proof correctness, novelty, priority, or literature claims. Use papers, drafts, notes, and reviewed source documents for mathematical evidence.

Save a Codex report:

```bash
# From WORKSPACE_ROOT
cp /path/to/report.md agent_logs/codex/2026-05-04-symbol-normalization.md
```

Ingest logs:

```bash
# From WORKSPACE_ROOT
math_rag/.venv/bin/python -m math_rag.cli ingest agent_logs/
```

This rebuilds the selected index over logs alone. Use a separate index when you want to keep the mathematical corpus index intact:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest agent_logs/ --index-dir .math_rag_agent_logs_index
math_rag/.venv/bin/python -m math_rag.cli search "why hits@1 dropped" --index-dir .math_rag_agent_logs_index
```

Search logs:

```bash
math_rag/.venv/bin/python -m math_rag.cli search "why hits@1 dropped"
math_rag/.venv/bin/python -m math_rag.cli search "symbol normalization Codex report"
math_rag/.venv/bin/python -m math_rag.cli search "MCP server final report"
```

MCP prompt example:

```text
Use math-rag to find the latest Codex report about symbol normalization and summarize what changed.
```

When ingested, files under `agent_logs/` are tagged in chunk metadata with `source_kind: agent_log`. The regular mathematical corpus under `corpus/` is not tagged this way.

## Mathematical Behavior

The LaTeX chunker tracks section hierarchy and creates separate chunks for theorem-like environments. It also detects common theorem aliases declared by `\newtheorem`.

Search preserves mathematical terms and symbols, and adds conservative search-only metadata such as normalized symbols and broad concept tags. Original chunk content is not rewritten.

## Privacy

The default ingest/search/ask workflow is local-only:

- no OpenAI key is required;
- no API key is hard-coded;
- `.env` is ignored by git;
- the corpus and index stay on the local machine unless you explicitly add a remote backend later.

The arXiv discovery and download commands are explicit exceptions: they contact arXiv and send search terms or arXiv IDs. They do not send your private corpus contents unless you put private information into the query/config yourself.

Treat the corpus as private unpublished research material.

## Limitations

This is not a proof checker. It does not verify proofs, fill gaps, establish novelty, or decide whether a theorem is correct. It can only say that retrieved sources contain similar claims, definitions, examples, or references.

PDF extraction quality depends on the PDF text layer and may be poor for scans or heavily formatted mathematics. LaTeX parsing is heuristic and may miss custom environments or macros. Hybrid ranking still needs corpus-specific tuning.

## Tests

From `PACKAGE_ROOT` with development dependencies installed:

```bash
python3 -m pytest
```

The tests cover LaTeX chunking, citation formatting, hybrid retrieval, eval behavior, downloader safety, MCP read-only behavior, and MCP root/path validation.
