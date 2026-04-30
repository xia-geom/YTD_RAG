# math_rag

`math_rag` is a local-first retrieval assistant for mathematical research notes. It ingests private LaTeX, Markdown, text, BibTeX, and PDF files, chunks them with math-aware heuristics, builds a local searchable index, and answers questions by showing retrieved passages with citations.

RAG means retrieval-augmented generation. In this project, the important part is retrieval: the system searches your own corpus and uses only retrieved chunks to prepare a structured report. It is not a proof checker and does not certify theorem correctness.

## Install

Use Python 3.11 or newer. From this project directory, a typical local setup is:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

The base install is dependency-light and local. To install preferred terminal, metadata, PDF, and test libraries:

```bash
python3 -m pip install -e ".[preferred,dev]"
```

For future local embedding experiments, install the optional embedding dependency:

```bash
python3 -m pip install -e ".[full]"
```

The current first-version vector search is a deterministic sparse local retriever. `sentence-transformers` is declared as an optional dependency for later embedding backends, not required for the default workflow.

## Add Documents

Place files in `corpus/` or pass another folder to the CLI. Supported first-version formats:

- `.tex`
- `.md`, `.markdown`
- `.txt`
- `.bib`
- `.pdf` if `pypdf` is installed

Optional metadata can be stored in `metadata/documents.yaml`; see `metadata/documents.example.yaml`.

## Build The Index

```bash
python3 -m math_rag.cli ingest corpus/
```

The default index is local and written to `.math_rag_index/index.json`. Re-running ingest rebuilds the local index from the selected corpus folder.

If the corpus is empty, the command prints a helpful message and writes an empty local index.

## Search

Hybrid search is the default because mathematical retrieval needs both exact names/symbols and expanded sparse-vector similarity:

```bash
python3 -m math_rag.cli search "Mabuchi energy convexity"
python3 -m math_rag.cli search "Chen-Cheng" --mode keyword
python3 -m math_rag.cli search "cusp limit of conic toric metrics" --mode vector
```

Search output includes rank, score, source path, chunk type, section path, page or line information when available, and a short snippet.

## Ask

```bash
python3 -m math_rag.cli ask "What sources discuss cusp limits of conic metrics?"
```

Without an LLM backend, `ask` produces a retrieval-based structured report:

- short answer
- retrieved evidence
- what the corpus supports
- reasonable inference
- not established by retrieved sources
- possible relevance to your research
- sources inspected

The answer layer is deliberately conservative. It says when evidence is weak and avoids asserting mathematical truth beyond retrieved passages.

## Seeded arXiv Corpus

For an initial research corpus, prefer a curated arXiv seed list over broad discovery. A seed list starts from papers you already trust, avoids noisy query matches, and makes the first corpus reproducible. Use discovery later to expand the corpus after the core papers are in place.

Create `arxiv_seed_core.txt` in this project directory with one arXiv ID per line:

```text
# comments and blank lines are ignored
1711.08424
1711.08424v2
math/0407486
dg-ga/9711014
```

Download the seed list:

```bash
python3 -m math_rag.cli download-seed arxiv_seed_core.txt
```

By default, `download-seed` downloads or records at most 10 new papers per run. Existing downloaded papers and `not_found` papers do not count against this cap. For a larger seed list, pass an explicit cap:

```bash
python3 -m math_rag.cli download-seed arxiv_seed_core.txt --max-papers 50
```

`--limit 50` is also accepted as an alias for `--max-papers 50`.

Or pass a download config you have edited:

```bash
python3 -m math_rag.cli download-seed arxiv_seed_core.txt --config metadata/discovery_config.yaml
```

Or download a few exact IDs directly:

```bash
python3 -m math_rag.cli download-arxiv 1711.08424 math/0407486 dg-ga/9711014
```

Then ingest the corpus:

```bash
python3 -m math_rag.cli ingest corpus/
python3 -m math_rag.cli stats
```

`download-seed` and `download-arxiv` use exact arXiv IDs, not search queries. Unversioned IDs such as `1711.08424` resolve to the version returned by arXiv at download time; use `1711.08424v2` when you need a fixed version. Old-style IDs such as `math/0407486` and `dg-ga/9711014` should be written verbatim in the seed file. Folder names are made filesystem-safe, so those examples are stored as `corpus/arxiv/math_0407486/` and `corpus/arxiv/dg-ga_9711014/`, while metadata preserves the original arXiv ID.

Before ingesting, inspect the download summary. `Papers failed` should be `0`, and `Papers processed` should match the number of unique seed IDs you expected. IDs beyond the successful download/record cap are reported as `skipped_limit`; unavailable papers are reported as `not_found`, `metadata_unavailable`, or `metadata_only`.

Existing paper folders are skipped by default and are never silently overwritten. Use `--skip-existing` when you want that behavior explicitly in scripts. Use `--force` only when intentionally replacing an existing folder. Rerunning an unversioned ID does not check for a newer arXiv version while the existing folder is present; pin `vN` for reproducibility, and use `--force` only for an intentional refresh. Repeated IDs in a seed file are downloaded once.

The downloader is intentionally polite: it uses one client, serializes arXiv requests, enforces at least 4 seconds between arXiv requests, and applies the same throttling to source and PDF downloads. When arXiv responds with HTTP 429, it backs off for 10 minutes, then 30 minutes, then 1 hour before giving up. Request, throttle, and backoff events are logged with UTC timestamps. Source and PDF downloads are attempted independently. TeX source is preferred for ingestion; PDF is used as a fallback; if neither is available, `metadata.yaml` is still written and the paper is skipped by ingest. PDF fallback requires `pypdf`, installed by `python3 -m pip install -e ".[preferred,dev]"`; otherwise ingest prints a warning and skips PDF-only papers.

## Automatic Paper Discovery And Download

`math_rag` can help discover candidate papers from arXiv, rank them, and download only the papers you approve. The workflow is intentionally not autonomous:

```text
discover -> rank -> review/approve -> download -> ingest -> search/ask
```

Run discovery with a query:

```bash
python3 -m math_rag.cli discover "constant scalar curvature Kahler toric" --verbose
```

Or use a configuration file:

```bash
cp metadata/discovery_config.example.yaml metadata/discovery_config.yaml
python3 -m math_rag.cli discover --config metadata/discovery_config.yaml
```

Discovery is conservative and phrase-aware. It protects mathematical phrases such as `constant scalar curvature Kähler`, `toric Kähler`, `Abreu equation`, `Mabuchi energy`, `weak geodesic`, `conic Kähler`, and `K-stability`. Generic words such as `toric`, `Kähler`, `curvature`, `equation`, `metric`, and `energy` are not enough by themselves to make a paper relevant.

Discovery queries the official arXiv Atom metadata API and writes `discovered_papers.yaml`. This sends your discovery query and config-derived search terms to arXiv. Pass `--verbose` to inspect the exact arXiv `search_query`; default sorting is `--sort-by relevance`, with `--sort-by newest` available when you explicitly want recent submissions. Entries are candidate papers, not endorsed or important papers. Each entry includes provenance, score, confidence, ranking reasons, and:

```yaml
confidence: high
status: pending
action: pending
```

When `exclude_low_confidence_by_default: true`, low-confidence matches are written separately under `low_confidence_candidates` rather than the main `candidates` list. This is meant to demote papers matching only weak tokens, for example generic scalar curvature, toric variety, PDE, matroid, CAD, or topology papers.

Review candidates in the terminal:

```bash
python3 -m math_rag.cli review-candidates discovered_papers.yaml
```

Then manually edit selected entries:

```yaml
action: download
```

or:

```yaml
action: ignore
```

Download only approved papers:

```bash
python3 -m math_rag.cli download-approved discovered_papers.yaml
```

By default, `download_policy.require_approval: true` blocks downloads of pending candidates, even if `--auto-download` is passed. To use the explicit escape hatch for a small capped run, set `require_approval: false` in a temporary config and pass `--auto-download --limit N`. Keep `N` small.

Approved arXiv papers are stored under:

```text
corpus/arxiv/<arxiv_id>/
  metadata.yaml
  source/
  paper.pdf
  extracted/
```

The downloader avoids duplicate arXiv ID/version folders by default, separates source from PDF, records source/PDF availability, and writes `primary_ingestion` to metadata.

TeX source is preferred for mathematical RAG because it preserves theorem environments, labels, references, equations, macros, and line numbers better than PDF text extraction. The PDF is still kept for page citation and human verification. If TeX source is unavailable, ingestion falls back to the PDF page by page. If both are unavailable, metadata is stored but the paper is not ingested.

Customize `metadata/discovery_config.yaml` to change seed authors, seed keywords, arXiv categories, ranking weights, manual whitelist, manual blacklist, download limits, and request delay. Keep rate limits conservative; the example delay is 4 seconds between requests, and lower configured values are clamped to 4 seconds. Whitelist and blacklist values are substring matches against arXiv ID, title, and author names.

To avoid polluting the corpus, keep `download_policy.require_approval: true`, review ranking reasons, use `manual_blacklist` for irrelevant recurring matches, and only set `action: download` for papers you want in the local research corpus.

## Using math_rag from Codex or Claude Code

`math_rag` ships with a local stdio MCP (Model Context Protocol) server so that agentic coding tools such as Codex and Claude Code can query the local RAG system directly, without you running CLI commands by hand.

MCP is the right integration layer here: it gives the agent a small set of typed tools (`rag_search`, `rag_ask`, `rag_get_chunk`, `rag_list_sources`) over stdio, the agent never gets shell access to the corpus, and the same service layer that backs the CLI also backs MCP, so the conservative answer discipline is preserved.

### Read-only by default

The MCP server exposes only read-only tools by default:

- `rag_search` — hybrid retrieval over the local index, returns ranked chunks with `source_path`, `chunk_type`, `section_path`, `page_number`, `line_start`/`line_end`, `score`, and `snippet`.
- `rag_ask` — retrieval-grounded structured answer with separate `retrieved_evidence`, `what_corpus_supports`, `reasonable_inference`, `not_established_by_retrieved_sources`, and `sources_inspected` fields. Never claims to verify a proof.
- `rag_get_chunk` — full content and metadata for one chunk id returned by `rag_search`.
- `rag_list_sources` — summary of indexed sources, optionally filtered by substring.

Write tools (`rag_ingest`, etc.) are **disabled** unless you explicitly opt in by setting:

```bash
export MATH_RAG_MCP_ALLOW_WRITE_TOOLS=true
```

The server will only attempt to read or write paths inside the resolved project root.

### Resolving the project root

The server determines the project root in this order:

1. `MATH_RAG_ROOT=/absolute/path/to/YTD_RAG/math_rag`
2. The current working directory, if it contains `pyproject.toml`, `corpus/`, and `src/math_rag/`.

If neither is satisfied, the server prints a clear error and exits.

You can also override the index location with `MATH_RAG_INDEX_DIR`.

### Connect from Codex

```bash
codex mcp add math-rag -- \
  /absolute/path/to/YTD_RAG/math_rag/.venv/bin/python \
  -m math_rag.mcp_server
```

If you installed `math_rag` in an editable mode where Python does not auto-pick up `__editable__.*.pth` files (Python 3.13 ignores `.pth` filenames starting with `__`), set `PYTHONPATH` and `MATH_RAG_ROOT` explicitly:

```bash
codex mcp add math-rag --env MATH_RAG_ROOT=/absolute/path/to/YTD_RAG/math_rag \
  --env PYTHONPATH=/absolute/path/to/YTD_RAG/math_rag/src -- \
  /absolute/path/to/YTD_RAG/math_rag/.venv/bin/python \
  -m math_rag.mcp_server
```

### Connect from Claude Code

```bash
claude mcp add --transport stdio math-rag -- \
  /absolute/path/to/YTD_RAG/math_rag/.venv/bin/python \
  -m math_rag.mcp_server
```

### Example prompts

In Codex or Claude Code, ask:

- "Use math-rag to search for Poincaré type cscK uniqueness and summarize the relevant sources."
- "Before editing my introduction, query math-rag for Berman-Darvas-Lu, Chen-Cheng, Lahdili, and Apostolov-Auvray-Sektnan."
- "Use math-rag to find all corpus evidence about conic approximations of Poincaré type cscK metrics."

The agent will call `rag_search` and `rag_ask`, receive structured JSON, and cite the retrieved sources back to you with page and line numbers.

### Security limits

- Default tool surface is read-only. No shell execution. No arbitrary file reads. No filesystem traversal.
- arXiv discovery and download are **never** exposed via MCP. They remain CLI-only and require explicit human approval per the existing download policy.
- The server caps the size of every tool response and instructs the caller to use `rag_get_chunk` for full content. Snippets and chunks pulled through MCP carry the same source path and line-number provenance as the CLI.
- Source-filter arguments accept substrings only, never raw shell or path-traversal strings.

## Stats

```bash
python3 -m math_rag.cli stats
```

This reports source count, chunk count, and chunk types in the local index.

## Validating The Corpus

Before adding ranking features, embeddings, or answer-generation layers, validate that the current corpus retrieves the sources you already expect. This evaluation is retrieval-only: it checks whether known evidence appears near the top of search results. It does not certify theorem statements, proof correctness, novelty, or completeness.

The commands below assume you are running from the workspace root that contains the downloaded `corpus/`, root `.math_rag_index/`, and `eval/toric_gold_questions.yaml`. If you run from inside this `math_rag/` package directory, adjust the paths, for example `../corpus/`, `../.math_rag_index`, and `../eval/toric_gold_questions.yaml`.

Rebuild the index from the corpus you want to test:

```bash
python3 -m math_rag.cli ingest corpus/
python3 -m math_rag.cli stats
```

Check the stats output for the number of sources, total chunks, and chunk types. TeX and BibTeX chunks should normally carry line numbers. PDF fallback chunks carry page numbers when `pypdf` is installed. If a PDF-only paper is skipped, install the preferred dependencies and ingest again:

```bash
python3 -m pip install -e ".[preferred,dev]"
python3 -m math_rag.cli ingest corpus/
```

Run search sanity checks with known queries:

```bash
python3 -m math_rag.cli search "Poincare type constant scalar curvature"
python3 -m math_rag.cli search "conical approximation Poincare type"
python3 -m math_rag.cli search "toric extremal Poincare type metrics"
python3 -m math_rag.cli search "Mabuchi energy weak geodesic"
python3 -m math_rag.cli search "extended K-energy finite energy"
python3 -m math_rag.cli search "Abreu equation toric"
python3 -m math_rag.cli search "weighted Mabuchi functional Lahdili"
python3 -m math_rag.cli search "polytope [-1,1]"
python3 -m math_rag.cli search "cone angle beta"
python3 -m math_rag.cli search "symplectic potential"
```

For each query, inspect whether the top results are mathematically sensible, whether they are primary paper passages or only bibliography hits, and whether source paths include line or page provenance.

Run ask sanity checks after search looks reasonable:

```bash
python3 -m math_rag.cli ask "What does the corpus say about conical approximations of Poincare type cscK metrics?"
python3 -m math_rag.cli ask "What does the corpus say about toric extremal Poincare type metrics?"
python3 -m math_rag.cli ask "What is the relation between Berman-Darvas-Lu convexity and weak geodesics?"
python3 -m math_rag.cli ask "What does the corpus say about weighted Mabuchi convexity?"
python3 -m math_rag.cli ask "What does the corpus say about the Abreu equation in toric Kähler geometry?"
```

The answer should keep retrieved evidence, corpus-supported statements, reasonable inference, and "not established by retrieved sources" separate. It should cite retrieved sources and should not claim to verify proofs.

Run the gold retrieval evaluation:

```bash
python3 -m math_rag.cli eval eval/toric_gold_questions.yaml
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

The eval output reports one row per question:

```text
Question ID | Hit? | First expected rank | Expected sources | Top sources
```

`Hit?` is `yes` when at least one expected source appears in the top-k retrieved chunks. `First expected rank` is the first rank where that happens. Negative questions are listed as `negative` and are excluded from hit-rate denominators.

Interpret the summary metrics as retrieval checks:

- `hits@1`: expected source is the first result.
- `hits@3`: expected source appears in the first three results.
- `hits@5`: expected source appears in the first five results.

High hit@k means the index and ranking can find known evidence. Low hit@k means query wording, chunking, ranking, or corpus coverage needs attention before answer quality can be trusted. The `missing expected sources` section is especially important: it identifies gold-source IDs that are not present in the current index at all.

## Mathematical Behavior

The LaTeX chunker tracks `section`, `subsection`, and `subsubsection` hierarchy and creates separate chunks for environments such as `definition`, `theorem`, `lemma`, `proposition`, `proof`, `example`, `remark`, `equation`, `align`, and `conjecture`.

Keyword search preserves LaTeX commands, symbols, citation keys, author names, and hyphenated names such as `Chen-Cheng` and `Berman-Darvas-Lu`. The local vector search is a deterministic sparse fallback with a few math-domain expansions. Heavier local embedding backends can be added later behind the `VectorSearch` boundary.

## Extension Points

The first version is intentionally small. Natural places to extend it are:

- `loaders.py` for more file formats or better BibTeX parsing;
- `latex_chunker.py` for custom theorem environments and `\input`/`\include` handling;
- `pdf_loader.py` for OCR or layout-aware PDF extraction;
- `vector_search.py` for a real local embedding backend;
- `hybrid_search.py` for rank tuning on your corpus;
- `answer.py` for an optional local or remote LLM backend with the same evidence discipline;
- `models.py` and `metadata/documents.yaml` for richer research metadata;
- separate proof-checking integrations, kept distinct from RAG answers.

## Privacy

The default mode is local-only:

- no OpenAI key is required;
- no API key is hard-coded;
- `.env` is ignored by git;
- the corpus and index stay on the local machine unless you explicitly add a remote backend later.

The discovery and download commands are explicit exceptions to fully local execution: they contact arXiv and send search terms or arXiv IDs to arXiv. They do not send your private corpus contents unless you choose query terms copied from private notes.

Treat the corpus as private unpublished research material.

## Limitations

This is not a proof checker. It does not verify proofs, fill gaps, establish novelty, or decide whether a theorem is correct. It can only say that retrieved sources contain similar claims, definitions, examples, or references.

PDF extraction quality depends on the PDF text layer and may be poor for scans or heavily formatted mathematics. LaTeX parsing is heuristic and may miss custom environments or macros. Hybrid ranking will need tuning on your real corpus.

## Tests

With development dependencies installed:

```bash
python3 -m pytest
```

The tests cover LaTeX environment chunking, citation formatting, hybrid retrieval preserving exact keyword hits, and weak retrieval avoiding unsupported answers.
