# YTD_RAG

A local research tool for searching mathematical papers and notes. It turns
LaTeX, Markdown, text, BibTeX, and optional PDFs into a JSON index, then retrieves
passages with citations. `ask` formats retrieved evidence; it does not call an
LLM or verify proofs.

**Start here:** [Architecture](ARCHITECTURE.md) ·
[Command reference](math_rag/README.md) · [Evaluation](eval/README.md)

## Setup

Run all commands from this workspace root. Python 3.11 or newer is required.

```bash
python3 -m venv math_rag/.venv
math_rag/.venv/bin/python -m pip install -e './math_rag[dev]'
```

Add `[pdf]` for PDF extraction or `[remote-mcp]` for the optional HTTP server.
For example: `math_rag/.venv/bin/python -m pip install -e './math_rag[pdf,dev]'`.

## Everyday workflow

Place research files in `corpus/`, then:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/
math_rag/.venv/bin/python -m math_rag.cli stats
math_rag/.venv/bin/python -m math_rag.cli search "Mabuchi energy convexity"
math_rag/.venv/bin/python -m math_rag.cli ask "What does the corpus say about Mabuchi energy convexity?"
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
```

`ingest` replaces the selected index. The CLI defaults to
`.math_rag_index/` relative to the working directory; use `--index-dir` for
another index. Optional document metadata belongs in `metadata/documents.yaml`.

Search and ingestion stay local. The optional arXiv discovery and download
commands contact arXiv with your search terms or paper IDs.

## Where things live

| Path | Purpose |
| --- | --- |
| `math_rag/src/math_rag/` | Python implementation |
| `math_rag/tests/` | Automated checks |
| `corpus/`, `.math_rag_index/` | Local research data and generated index; not committed |
| `metadata/`, `research_profile.md` | Corpus metadata and discovery preferences |
| `eval/` | Retrieval benchmarks and evidence review |
| `docs/`, `deploy/azure/` | Optional remote MCP reference and deployment assets |
| `findings/` | Historical deployment investigations, dated within each file |
| `agent_logs/` | Engineering history; never mathematical evidence |

## MCP support

The local stdio server is `python -m math_rag.mcp_server`. See the
[local MCP configuration](math_rag/README.md#local-mcp) for workspace/index paths.

Remote serving was **paused on 2026-05-18** by disabling Container App ingress.
That is the last recorded deployment state, not a fresh cloud check. The last
remote index was reviewed public-safe data. Local RAG is the normal workflow.

The supported HTTP entrypoint is `math_rag.mcp_http_server`, with exactly
`search` and `fetch` in ChatGPT mode. Start with the
[HTTP reference](docs/remote_mcp_server.md) and
[deployment gates](docs/azure_remote_mcp_readiness.md) before resuming it.
Public/container deployments require backend bearer authentication; no-auth
mode is for localhost. Do not expose the private index through the old public
backend path. A private deployment requires network isolation and OAuth/JWT
validation; the existing fixture path does not provide these guarantees.

## Development

```bash
math_rag/.venv/bin/python -m pytest math_rag/tests
```

For retrieval changes, also run `stats` and the core eval shown above.
Keep corpus files, indexes, PDFs, virtualenvs, caches, `.env`, and secrets out of
Git and container images. Preserve local research data during cleanup.

Save completed engineering work following [agent_logs/README.md](agent_logs/README.md).
Use a separate index when searching those reports:

```bash
math_rag/.venv/bin/python -m math_rag.cli ingest agent_logs/ --index-dir .math_rag_agent_logs_index
math_rag/.venv/bin/python -m math_rag.cli search "MCP status" --index-dir .math_rag_agent_logs_index
```
