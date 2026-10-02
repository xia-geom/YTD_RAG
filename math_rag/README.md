# math_rag command reference

See the [workspace README](../README.md) for installation and the
[architecture](../ARCHITECTURE.md) for module responsibilities. Run the examples
from the workspace root, using `math_rag/.venv/bin/python -m math_rag.cli`.
The installed `math-rag` command invokes the same parser.

## Commands

Use `<command> --help` for the complete option list.

| Command | Purpose |
| --- | --- |
| `ingest PATH` | Replace the selected index with chunks from PATH |
| `search QUERY` | Show ranked passages with source locations |
| `ask QUERY` | Format retrieved evidence, inference, and limitations |
| `stats` | Show indexed source and chunk counts |
| `eval FILE` | Evaluate source-level retrieval against a YAML benchmark |
| `inspect-evidence-eval FILE` | Inspect candidate passage evidence and optional triage reports |
| `export-enrichment-batch PATH --output FILE` | Export chunks for offline metadata enrichment |
| `discover [QUERY]` | Query arXiv and write candidates for review |
| `review-candidates [FILE]` | Display candidate rankings and approval status |
| `download-approved [FILE]` | Download approved candidates |
| `download-arxiv ID [ID ...]` | Download exact arXiv IDs |
| `download-seed [FILE]` | Download IDs from a seed file (default `arxiv_seed_core.txt`) |

Index commands accept `--index-dir` (default `.math_rag_index` relative to the
working directory). Search/ask/eval accept `--mode keyword|vector|hybrid` and
`--top-k`. Hybrid is the default; vector is sparse cosine search, not neural
embeddings. Use explicit `--index-dir ../.math_rag_index` if running inside
`math_rag/` instead of the workspace root.

## Ingestion and enrichment

Supported inputs: `.tex`, `.md`, `.markdown`, `.txt`, `.bib`, and `.pdf` with
the `pdf` extra. Metadata defaults to `metadata/documents.yaml`; override it
with `--metadata`. See [documents.example.yaml](../metadata/documents.example.yaml).

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/ --enrich-metadata
math_rag/.venv/bin/python -m math_rag.cli export-enrichment-batch corpus/ --output /tmp/enrichment_batch.jsonl
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/ \
  --enrich-metadata --enrichment-backend agent_json_v1 \
  --agent-enrichment-jsonl /tmp/enrichment.jsonl
```

Enrichment adds metadata without changing source content, chunk IDs, boundaries,
or line spans. `deterministic_v1` is the default backend. `agent_json_v1` reads
a local JSONL file and falls back to deterministic metadata for invalid records;
it never calls a model API. `--refresh-enrichment-cache` recomputes the cache.

`ingest` rebuilds the chosen index. For engineering logs, always select a
separate `.math_rag_agent_logs_index` as shown in the workspace README.

## Paper acquisition

These commands contact arXiv with queries or IDs. A curated seed file contains
one ID per line; comments and blank lines are ignored. Versioned and old-style
IDs are supported.

```bash
math_rag/.venv/bin/python -m math_rag.cli download-seed arxiv_seed_core.txt --max-papers 50
math_rag/.venv/bin/python -m math_rag.cli download-arxiv 1711.08424v2 math/0407486
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/
```

Seed download defaults to at most 10 new papers per run. Existing paper folders
are skipped unless `--force` is explicitly supplied. `--skip-existing` and
`--force` are mutually exclusive. Downloads fetch source and PDF by default and
apply arXiv delays/backoff. Ingestion prefers TeX source and uses PDF as fallback.

For broader discovery:

```bash
math_rag/.venv/bin/python -m math_rag.cli discover "constant scalar curvature Kahler toric" --verbose
math_rag/.venv/bin/python -m math_rag.cli review-candidates discovered_papers.yaml
# Review the YAML and set action: download on selected entries.
math_rag/.venv/bin/python -m math_rag.cli download-approved discovered_papers.yaml
```

Discovery writes its review queue in the working directory. Use `--config` with
[discovery_config.example.yaml](../metadata/discovery_config.example.yaml) to
customize discovery/download policy. Keep `download_policy.require_approval`
enabled; pending candidates remain blocked even with `--auto-download`.

## Evaluation

```bash
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
math_rag/.venv/bin/python -m math_rag.cli inspect-evidence-eval eval/candidate_evidence_questions.yaml \
  --out /tmp/evidence-inspection.md --triage-out /tmp/evidence-triage.md
```

The stable core benchmark reports source-level hits@1, hits@3, and hits@5;
negative questions are excluded from those denominators. A source hit does not
prove that the correct passage was found. See [eval/README.md](../eval/README.md)
and the [evidence evaluation notes](../eval/evidence_eval_README.md).

## Local MCP

Launch `math_rag.mcp_server` with the project Python and explicit environment:

```bash
MATH_RAG_PACKAGE_ROOT="$PWD/math_rag" \
MATH_RAG_WORKSPACE_ROOT="$PWD" \
MATH_RAG_INDEX_DIR="$PWD/.math_rag_index" \
math_rag/.venv/bin/python -m math_rag.mcp_server
```

Configure those same executable, module arguments, and environment values in
your local MCP client. Read-only tools are `rag_search`, `rag_ask`,
`rag_get_chunk`, and `rag_list_sources`. Responses are bounded; use
`rag_get_chunk` to inspect a retrieved ID.

`MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true` additionally exposes `rag_ingest`, which
accepts workspace-relative paths and rejects traversal outside the workspace.
`MATH_RAG_ROOT` remains a legacy root fallback; prefer the explicit settings
above. No shell, arbitrary-file, or arXiv download tools are exposed.

## Remote MCP and migration notes

Remote Azure serving is paused. The supported HTTP entrypoint is
`math_rag.mcp_http_server`; see [HTTP configuration](../docs/remote_mcp_server.md).
The older `remote_mcp_server` adapter and `math-rag-mcp-remote` executable remain
for compatibility. They are not the Azure Dockerfile's entrypoint.

The cleanup standardizes on argparse and dataclasses. Existing valid JSON
indexes retain the same schema and need no rebuild. Runtime type coercion from
optional Pydantic models is no longer applied; metadata should use the types
shown in the examples.

The old `scripts/build_index.py`, `scripts/search.py`, and `scripts/ask.py`
launchers were removed; use CLI `ingest`, `search`, and `ask` respectively.
The old `preferred`, `embeddings`, and `full` extras were removed. Install only
what you use: `./math_rag[pdf,remote-mcp,dev]` enables all supported extras.
There is no implemented sentence-transformers backend. `MATH_RAG_LOCAL_ONLY`
was unused and has been removed; local operation does not depend on that flag.
