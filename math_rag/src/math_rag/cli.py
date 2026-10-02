"""Command line interface for math_rag."""

from __future__ import annotations

import argparse

from .answer import build_answer
from .citations import format_result_header
from .config import DEFAULT_INDEX_DIR
from .discovery import discover_candidates
from .downloader import DEFAULT_SEED_MAX_PAPERS, download_approved_papers, download_arxiv_ids, download_seed_file
from .evidence_eval import (
    format_candidate_evidence_inspection_markdown,
    inspect_candidate_evidence_eval,
    write_candidate_evidence_inspection_markdown,
    write_candidate_evidence_triage_markdown,
)
from .eval import evaluate_retrieval, format_eval_report
from .metadata_enrichment import DETERMINISTIC_ENRICHMENT_BACKEND
from .paper_store import (
    DEFAULT_ARXIV_CORPUS_DIR,
    DEFAULT_CANDIDATES_PATH,
    PaperCandidate,
    load_candidate_groups,
)
from .rag_service import IndexNotFoundError, export_enrichment_batch, index_stats, ingest_path, retrieve
from .text_cleaning import make_snippet


def run_ingest(
    corpus_path: str,
    index_dir: str = DEFAULT_INDEX_DIR,
    metadata: str | None = None,
    enrich_metadata: bool = False,
    refresh_enrichment_cache: bool = False,
    enrichment_backend: str = DETERMINISTIC_ENRICHMENT_BACKEND,
    agent_enrichment_jsonl: str | None = None,
) -> int:
    try:
        result = ingest_path(
            corpus_path,
            index_dir=index_dir,
            metadata=metadata,
            enrich_metadata=enrich_metadata,
            refresh_enrichment_cache=refresh_enrichment_cache,
            enrichment_backend=enrichment_backend,
            agent_enrichment_jsonl=agent_enrichment_jsonl,
        )
    except ValueError as exc:
        print(str(exc))
        return 1
    if result["chunk_count"]:
        print(f"Ingested {result['chunk_count']} chunks from {corpus_path}")
        print(f"Index written to {result['index_path']}")
    else:
        print(f"No supported documents were ingested from {corpus_path}.")
        print("Add .tex, .md, .txt, .bib, or .pdf files and run ingest again.")
    for warning in result["warnings"]:
        print(f"Warning: {warning}")
    return 0


def run_export_enrichment_batch(
    corpus_path: str,
    output: str,
    metadata: str | None = None,
    max_content_chars: int = 4000,
) -> int:
    if max_content_chars < 3:
        print("--max-content-chars must be at least 3.")
        return 1
    result = export_enrichment_batch(
        corpus_path,
        output=output,
        metadata=metadata,
        max_content_chars=max_content_chars,
    )
    print(f"Exported {result['chunk_count']} chunks to {result['output_path']}")
    for warning in result["warnings"]:
        print(f"Warning: {warning}")
    return 0


def run_search(query: str, index_dir: str = DEFAULT_INDEX_DIR, mode: str = "hybrid", top_k: int = 10) -> int:
    try:
        results = retrieve(query, top_k=top_k, mode=mode, index_dir=index_dir)
    except IndexNotFoundError as exc:
        print(str(exc))
        return 1
    if not results:
        print("No matching chunks found.")
        return 0
    for result in results:
        chunk = result.chunk
        page_line = []
        if chunk.page_number is not None:
            page_line.append(f"p. {chunk.page_number}")
        if chunk.line_start is not None and chunk.line_end is not None:
            page_line.append(f"lines {chunk.line_start}-{chunk.line_end}")
        print(format_result_header(result))
        print(f"    location: {', '.join(page_line) if page_line else 'n/a'}")
        print(f"    snippet: {make_snippet(chunk.content, query)}")
        print("")
    return 0


def run_ask(query: str, index_dir: str = DEFAULT_INDEX_DIR, mode: str = "hybrid", top_k: int = 6) -> int:
    try:
        results = retrieve(query, top_k=top_k, mode=mode, index_dir=index_dir)
    except IndexNotFoundError as exc:
        print(str(exc))
        return 1
    print(build_answer(query, results, top_evidence=top_k))
    return 0


def run_stats(index_dir: str = DEFAULT_INDEX_DIR) -> int:
    stats = index_stats(index_dir=index_dir)
    print(f"Index: {stats['index_path']}")
    print(f"Sources: {stats['source_count']}")
    print(f"Chunks: {stats['chunk_count']}")
    print("Chunk types:")
    if stats["chunk_types"]:
        for chunk_type, count in sorted(stats["chunk_types"].items()):
            print(f"  {chunk_type}: {count}")
    else:
        print("  none")
    return 0


def run_eval(eval_path: str, index_dir: str = DEFAULT_INDEX_DIR, mode: str = "hybrid", top_k: int = 5) -> int:
    try:
        summary = evaluate_retrieval(eval_path, index_dir=index_dir, mode=mode, top_k=top_k)
    except (FileNotFoundError, ValueError, IndexNotFoundError) as exc:
        print(str(exc))
        return 1
    print(format_eval_report(summary))
    return 0


def run_inspect_evidence_eval(
    eval_path: str,
    index_dir: str = DEFAULT_INDEX_DIR,
    mode: str = "hybrid",
    top_k: int = 10,
    out: str | None = None,
    triage_out: str | None = None,
) -> int:
    try:
        report = inspect_candidate_evidence_eval(eval_path, index_dir=index_dir, mode=mode, top_k=top_k)
    except (FileNotFoundError, ValueError, IndexNotFoundError) as exc:
        print(str(exc))
        return 1
    markdown = format_candidate_evidence_inspection_markdown(report)
    print(markdown)
    if out:
        path = write_candidate_evidence_inspection_markdown(report, out)
        print(f"Wrote candidate evidence inspection report to {path}")
    if triage_out:
        path = write_candidate_evidence_triage_markdown(report, triage_out)
        print(f"Wrote candidate evidence triage report to {path}")
    return 0


def run_discover(
    query: str | None = None,
    config: str | None = None,
    output: str = DEFAULT_CANDIDATES_PATH,
    index_dir: str = DEFAULT_INDEX_DIR,
    max_results: int | None = None,
    sort_by: str = "relevance",
    verbose: bool = False,
) -> int:
    result = discover_candidates(
        query=query,
        config_path=config,
        output_path=output,
        index_dir=index_dir,
        max_results=max_results,
        sort_by=sort_by,
    )
    if verbose:
        print(f"arXiv search_query: {result.arxiv_query}")
        print(f"arXiv sort_by: {sort_by}")
    for warning in result.warnings:
        print(f"Warning: {warning}")
    print(f"Wrote {len(result.candidates)} candidate papers to {output}")
    if result.low_confidence_candidates:
        print(f"Excluded {len(result.low_confidence_candidates)} low-confidence papers into low_confidence_candidates.")
    print_candidate_table(result.candidates)
    if result.candidates:
        print("Review the YAML file and set action: download for papers you want to fetch.")
    else:
        print("No candidate papers were discovered. Try broader keywords or check network access.")
    return 0 if not result.warnings else 1


def run_review_candidates(candidates_path: str = DEFAULT_CANDIDATES_PATH) -> int:
    candidates, low_confidence = load_candidate_groups(candidates_path)
    if not candidates and not low_confidence:
        print(f"No candidates found in {candidates_path}.")
        return 1
    if candidates:
        print_candidate_table(candidates)
    else:
        print("No high/medium-confidence candidates in the main list.")
    if low_confidence:
        print(
            f"Low-confidence papers excluded from the main list: {len(low_confidence)}. "
            "They are under low_confidence_candidates in the YAML file."
        )
    print("Set action: download to approve a candidate paper, or action: ignore to skip it.")
    return 0


def run_download_approved(
    candidates_path: str = DEFAULT_CANDIDATES_PATH,
    corpus_dir: str = DEFAULT_ARXIV_CORPUS_DIR,
    config: str | None = None,
    auto_download: bool = False,
    limit: int | None = None,
    overwrite: bool = False,
) -> int:
    results = download_approved_papers(
        candidates_path=candidates_path,
        corpus_arxiv_dir=corpus_dir,
        config_path=config,
        auto_download=auto_download,
        limit=limit,
        overwrite=overwrite,
    )
    if not results:
        print("No papers were approved for download.")
        print("Edit the candidate YAML and set action: download for selected candidate papers.")
        return 0
    _print_download_results(results)
    return 0


def run_download_arxiv(
    arxiv_ids: list[str],
    corpus_dir: str = DEFAULT_ARXIV_CORPUS_DIR,
    config: str | None = None,
    limit: int | None = None,
    force: bool = False,
    skip_existing: bool = False,
) -> int:
    effective_skip_existing = _resolve_skip_existing(force, skip_existing)
    if effective_skip_existing is None:
        return 2
    results = download_arxiv_ids(
        arxiv_ids,
        corpus_arxiv_dir=corpus_dir,
        config_path=config,
        limit=limit,
        force=force,
        skip_existing=effective_skip_existing,
    )
    if not results:
        print("No arXiv IDs were processed.")
        return 0
    _print_download_results(results)
    return 0


def run_download_seed(
    seed_file: str = "arxiv_seed_core.txt",
    corpus_dir: str = DEFAULT_ARXIV_CORPUS_DIR,
    config: str | None = None,
    max_papers: int | None = DEFAULT_SEED_MAX_PAPERS,
    force: bool = False,
    skip_existing: bool = False,
) -> int:
    effective_skip_existing = _resolve_skip_existing(force, skip_existing)
    if effective_skip_existing is None:
        return 2
    try:
        results = download_seed_file(
            seed_file,
            corpus_arxiv_dir=corpus_dir,
            config_path=config,
            max_papers=max_papers,
            force=force,
            skip_existing=effective_skip_existing,
        )
    except FileNotFoundError:
        print(f"Seed file not found: {seed_file}")
        return 1
    if not results:
        print(f"No arXiv IDs found in {seed_file}.")
        return 0
    _print_download_results(results)
    return 0


def _resolve_skip_existing(force: bool, skip_existing: bool) -> bool | None:
    if force and skip_existing:
        print("Choose either --force or --skip-existing, not both.")
        return None
    return skip_existing or not force


def _print_download_results(results: list) -> None:
    downloaded = sum(1 for result in results if result.status in {"downloaded", "metadata_only"})
    skipped = sum(1 for result in results if result.status.startswith("skipped"))
    duplicates = sum(1 for result in results if result.duplicate)
    failed = len(results) - downloaded - skipped
    print(f"Papers processed: {len(results)}")
    print(f"Papers downloaded or recorded: {downloaded}")
    print(f"Papers skipped: {skipped}")
    print(f"Papers failed: {failed}")
    print(f"Duplicates detected: {duplicates}")
    for result in results:
        print(
            f"- {result.arxiv_id}{result.version or ''}: {result.status}; "
            f"source={'yes' if result.source_downloaded else 'no'}; "
            f"pdf={'yes' if result.pdf_downloaded else 'no'}; "
            f"path={result.path or 'n/a'}"
        )
        for error in result.errors:
            print(f"  error: {error}")


def print_candidate_table(candidates: list[PaperCandidate]) -> None:
    print("Rank | Score | Confidence | arXiv ID | Year | Title | Authors | Reasons | Action")
    print("-" * 125)
    for rank, candidate in enumerate(candidates, start=1):
        authors = ", ".join(candidate.authors[:3])
        if len(candidate.authors) > 3:
            authors += " et al."
        reasons = "; ".join(candidate.ranking_reasons[:3])
        print(
            f"{rank} | {candidate.score:.3f} | {candidate.confidence} | {candidate.arxiv_id}{candidate.version or ''} | "
            f"{candidate.year or ''} | {_shorten(candidate.title, 46)} | "
            f"{_shorten(authors, 30)} | {_shorten(reasons, 52)} | {candidate.action}"
        )


def _shorten(value: str, max_chars: int) -> str:
    if len(value) <= max_chars:
        return value
    return value[: max_chars - 3].rstrip() + "..."


def main(argv: list[str] | None = None) -> int:
    """Run the CLI using explicit arguments or the process command line."""

    parser = argparse.ArgumentParser(description="Local-first RAG for mathematical research documents.")
    subparsers = parser.add_subparsers(dest="command", required=True, title="commands")

    ingest_parser = subparsers.add_parser("ingest", help="Build a local index from documents.")
    ingest_parser.add_argument("corpus_path")
    ingest_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    ingest_parser.add_argument("--metadata", default=None)
    ingest_parser.add_argument("--enrich-metadata", action="store_true")
    ingest_parser.add_argument("--refresh-enrichment-cache", action="store_true")
    ingest_parser.add_argument("--enrichment-backend", default=DETERMINISTIC_ENRICHMENT_BACKEND)
    ingest_parser.add_argument("--agent-enrichment-jsonl", default=None)

    export_parser = subparsers.add_parser("export-enrichment-batch", help="Export chunks for offline metadata enrichment.")
    export_parser.add_argument("corpus_path")
    export_parser.add_argument("--output", required=True)
    export_parser.add_argument("--metadata", default=None)
    export_parser.add_argument("--max-content-chars", type=int, default=4000)

    search_parser = subparsers.add_parser("search", help="Find cited passages in the local index.")
    search_parser.add_argument("query")
    search_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    search_parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    search_parser.add_argument("--top-k", type=int, default=10)

    ask_parser = subparsers.add_parser("ask", help="Build an evidence report from retrieved passages.")
    ask_parser.add_argument("query")
    ask_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    ask_parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    ask_parser.add_argument("--top-k", type=int, default=6)

    stats_parser = subparsers.add_parser("stats", help="Show source and chunk counts.")
    stats_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)

    eval_parser = subparsers.add_parser("eval", help="Measure retrieval against gold questions.")
    eval_parser.add_argument("eval_path")
    eval_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    eval_parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    eval_parser.add_argument("--top-k", type=int, default=5)

    inspect_evidence_parser = subparsers.add_parser("inspect-evidence-eval", help="Prepare candidate evidence for review.")
    inspect_evidence_parser.add_argument("eval_path")
    inspect_evidence_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    inspect_evidence_parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    inspect_evidence_parser.add_argument("--top-k", type=int, default=10)
    inspect_evidence_parser.add_argument("--out", default=None)
    inspect_evidence_parser.add_argument("--triage-out", default=None)

    discover_parser = subparsers.add_parser("discover", help="Search arXiv and write candidates for review.")
    discover_parser.add_argument("query", nargs="?")
    discover_parser.add_argument("--config", default=None)
    discover_parser.add_argument("--output", default=DEFAULT_CANDIDATES_PATH)
    discover_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    discover_parser.add_argument("--max-results", type=int, default=None)
    discover_parser.add_argument("--sort-by", default="relevance", choices=["relevance", "newest"])
    discover_parser.add_argument("--verbose", action="store_true")

    review_parser = subparsers.add_parser("review-candidates", help="Display a candidate paper file.")
    review_parser.add_argument("candidates_path", nargs="?", default=DEFAULT_CANDIDATES_PATH)

    download_parser = subparsers.add_parser("download-approved", help="Download approved candidate papers.")
    download_parser.add_argument("candidates_path", nargs="?", default=DEFAULT_CANDIDATES_PATH)
    download_parser.add_argument("--corpus-dir", default=DEFAULT_ARXIV_CORPUS_DIR)
    download_parser.add_argument("--config", default=None)
    download_parser.add_argument("--auto-download", action="store_true")
    download_parser.add_argument("--limit", type=int, default=None)
    download_parser.add_argument("--overwrite", action="store_true")

    download_arxiv_parser = subparsers.add_parser("download-arxiv", help="Download specified arXiv IDs.")
    download_arxiv_parser.add_argument("arxiv_ids", nargs="+")
    download_arxiv_parser.add_argument("--corpus-dir", default=DEFAULT_ARXIV_CORPUS_DIR)
    download_arxiv_parser.add_argument("--config", default=None)
    download_arxiv_parser.add_argument("--limit", type=int, default=None)
    download_arxiv_group = download_arxiv_parser.add_mutually_exclusive_group()
    download_arxiv_group.add_argument("--force", action="store_true", help="Replace an existing paper folder.")
    download_arxiv_group.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip existing paper folders; this is the default behavior.",
    )

    download_seed_parser = subparsers.add_parser("download-seed", help="Download papers from a seed file.")
    download_seed_parser.add_argument("seed_file", nargs="?", default="arxiv_seed_core.txt")
    download_seed_parser.add_argument("--corpus-dir", default=DEFAULT_ARXIV_CORPUS_DIR)
    download_seed_parser.add_argument("--config", default=None)
    download_seed_parser.add_argument(
        "--max-papers",
        "--limit",
        dest="max_papers",
        type=int,
        default=DEFAULT_SEED_MAX_PAPERS,
        help=(
            "Maximum papers to download or record this run; existing and not-found papers do not count "
            f"(default: {DEFAULT_SEED_MAX_PAPERS})."
        ),
    )
    download_seed_group = download_seed_parser.add_mutually_exclusive_group()
    download_seed_group.add_argument("--force", action="store_true", help="Replace existing paper folders.")
    download_seed_group.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip existing paper folders; this is the default behavior.",
    )

    args = parser.parse_args(argv)
    if args.command == "ingest":
        return run_ingest(
            args.corpus_path,
            args.index_dir,
            args.metadata,
            args.enrich_metadata,
            args.refresh_enrichment_cache,
            args.enrichment_backend,
            args.agent_enrichment_jsonl,
        )
    if args.command == "export-enrichment-batch":
        return run_export_enrichment_batch(args.corpus_path, args.output, args.metadata, args.max_content_chars)
    if args.command == "search":
        return run_search(args.query, args.index_dir, args.mode, args.top_k)
    if args.command == "ask":
        return run_ask(args.query, args.index_dir, args.mode, args.top_k)
    if args.command == "stats":
        return run_stats(args.index_dir)
    if args.command == "eval":
        return run_eval(args.eval_path, args.index_dir, args.mode, args.top_k)
    if args.command == "inspect-evidence-eval":
        return run_inspect_evidence_eval(args.eval_path, args.index_dir, args.mode, args.top_k, args.out, args.triage_out)
    if args.command == "discover":
        return run_discover(args.query, args.config, args.output, args.index_dir, args.max_results, args.sort_by, args.verbose)
    if args.command == "review-candidates":
        return run_review_candidates(args.candidates_path)
    if args.command == "download-approved":
        return run_download_approved(
            args.candidates_path,
            args.corpus_dir,
            args.config,
            args.auto_download,
            args.limit,
            args.overwrite,
        )
    if args.command == "download-arxiv":
        return run_download_arxiv(
            args.arxiv_ids,
            args.corpus_dir,
            args.config,
            args.limit,
            args.force,
            args.skip_existing,
        )
    if args.command == "download-seed":
        return run_download_seed(
            args.seed_file,
            args.corpus_dir,
            args.config,
            args.max_papers,
            args.force,
            args.skip_existing,
        )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
