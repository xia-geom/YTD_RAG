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

The default download policy processes at most 20 IDs per run. For a larger seed list, pass an explicit cap:

```bash
python3 -m math_rag.cli download-seed arxiv_seed_core.txt --limit 50
```

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

Before ingesting, inspect the download summary. `Papers failed` should be `0`, and `Papers processed` should match the number of unique seed IDs you expected. IDs beyond the run limit are reported as `skipped_limit`; unavailable papers are reported as `not_found`, `metadata_unavailable`, or `metadata_only`.

Existing paper folders are skipped by default and are never silently overwritten. Use `--skip-existing` when you want that behavior explicitly in scripts. Use `--force` only when intentionally replacing an existing folder. Rerunning an unversioned ID does not check for a newer arXiv version while the existing folder is present; pin `vN` for reproducibility, and use `--force` only for an intentional refresh. Repeated IDs in a seed file are downloaded once.

The downloader is intentionally polite: it uses one client, no parallel downloads, the configured delay between arXiv requests, and a single conservative retry when arXiv responds with HTTP 429. Source and PDF downloads are attempted independently. TeX source is preferred for ingestion; PDF is used as a fallback; if neither is available, `metadata.yaml` is still written and the paper is skipped by ingest. PDF fallback requires `pypdf`, installed by `python3 -m pip install -e ".[preferred,dev]"`; otherwise ingest prints a warning and skips PDF-only papers.

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

Customize `metadata/discovery_config.yaml` to change seed authors, seed keywords, arXiv categories, ranking weights, manual whitelist, manual blacklist, download limits, and request delay. Keep rate limits conservative; the example delay is 3 seconds between requests. Whitelist and blacklist values are substring matches against arXiv ID, title, and author names.

To avoid polluting the corpus, keep `download_policy.require_approval: true`, review ranking reasons, use `manual_blacklist` for irrelevant recurring matches, and only set `action: download` for papers you want in the local research corpus.

## Stats

```bash
python3 -m math_rag.cli stats
```

This reports source count, chunk count, and chunk types in the local index.

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
