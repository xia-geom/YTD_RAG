"""Command line interface for math_rag."""

from __future__ import annotations

import argparse

from .answer import build_answer
from .citations import format_result_header
from .config import DEFAULT_INDEX_DIR
from .discovery import discover_candidates
from .downloader import DEFAULT_SEED_MAX_PAPERS, download_approved_papers, download_arxiv_ids, download_seed_file
from .eval import evaluate_retrieval, format_eval_report
from .paper_store import (
    DEFAULT_ARXIV_CORPUS_DIR,
    DEFAULT_CANDIDATES_PATH,
    PaperCandidate,
    load_candidate_groups,
)
from .rag_service import IndexNotFoundError, index_stats, ingest_path, retrieve
from .text_cleaning import make_snippet


try:  # pragma: no cover - optional dependency
    import typer

    TYPER_AVAILABLE = True
except Exception:  # pragma: no cover - main path in the execution sandbox
    typer = None
    TYPER_AVAILABLE = False

try:  # pragma: no cover - optional dependency
    from rich.console import Console

    console = Console()
except Exception:  # pragma: no cover - main path in the execution sandbox

    class _PlainConsole:
        def print(self, *values: object, **_: object) -> None:
            print(*values)

    console = _PlainConsole()


def run_ingest(corpus_path: str, index_dir: str = DEFAULT_INDEX_DIR, metadata: str | None = None) -> int:
    result = ingest_path(corpus_path, index_dir=index_dir, metadata=metadata)
    if result["chunk_count"]:
        console.print(f"Ingested {result['chunk_count']} chunks from {corpus_path}")
        console.print(f"Index written to {result['index_path']}")
    else:
        console.print(f"No supported documents were ingested from {corpus_path}.")
        console.print("Add .tex, .md, .txt, .bib, or .pdf files and run ingest again.")
    for warning in result["warnings"]:
        console.print(f"Warning: {warning}")
    return 0


def run_search(query: str, index_dir: str = DEFAULT_INDEX_DIR, mode: str = "hybrid", top_k: int = 10) -> int:
    try:
        results = retrieve(query, top_k=top_k, mode=mode, index_dir=index_dir)
    except IndexNotFoundError as exc:
        console.print(str(exc))
        return 1
    if not results:
        console.print("No matching chunks found.")
        return 0
    for result in results:
        chunk = result.chunk
        page_line = []
        if chunk.page_number is not None:
            page_line.append(f"p. {chunk.page_number}")
        if chunk.line_start is not None and chunk.line_end is not None:
            page_line.append(f"lines {chunk.line_start}-{chunk.line_end}")
        console.print(format_result_header(result))
        console.print(f"    location: {', '.join(page_line) if page_line else 'n/a'}")
        console.print(f"    snippet: {make_snippet(chunk.content, query)}")
        console.print("")
    return 0


def run_ask(query: str, index_dir: str = DEFAULT_INDEX_DIR, mode: str = "hybrid", top_k: int = 6) -> int:
    try:
        results = retrieve(query, top_k=top_k, mode=mode, index_dir=index_dir)
    except IndexNotFoundError as exc:
        console.print(str(exc))
        return 1
    console.print(build_answer(query, results, top_evidence=top_k))
    return 0


def run_stats(index_dir: str = DEFAULT_INDEX_DIR) -> int:
    stats = index_stats(index_dir=index_dir)
    console.print(f"Index: {stats['index_path']}")
    console.print(f"Sources: {stats['source_count']}")
    console.print(f"Chunks: {stats['chunk_count']}")
    console.print("Chunk types:")
    if stats["chunk_types"]:
        for chunk_type, count in sorted(stats["chunk_types"].items()):
            console.print(f"  {chunk_type}: {count}")
    else:
        console.print("  none")
    return 0


def run_eval(eval_path: str, index_dir: str = DEFAULT_INDEX_DIR, mode: str = "hybrid", top_k: int = 5) -> int:
    try:
        summary = evaluate_retrieval(eval_path, index_dir=index_dir, mode=mode, top_k=top_k)
    except (FileNotFoundError, ValueError, IndexNotFoundError) as exc:
        console.print(str(exc))
        return 1
    console.print(format_eval_report(summary))
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
        console.print(f"arXiv search_query: {result.arxiv_query}")
        console.print(f"arXiv sort_by: {sort_by}")
    for warning in result.warnings:
        console.print(f"Warning: {warning}")
    console.print(f"Wrote {len(result.candidates)} candidate papers to {output}")
    if result.low_confidence_candidates:
        console.print(f"Excluded {len(result.low_confidence_candidates)} low-confidence papers into low_confidence_candidates.")
    print_candidate_table(result.candidates)
    if result.candidates:
        console.print("Review the YAML file and set action: download for papers you want to fetch.")
    else:
        console.print("No candidate papers were discovered. Try broader keywords or check network access.")
    return 0 if not result.warnings else 1


def run_review_candidates(candidates_path: str = DEFAULT_CANDIDATES_PATH) -> int:
    candidates, low_confidence = load_candidate_groups(candidates_path)
    if not candidates and not low_confidence:
        console.print(f"No candidates found in {candidates_path}.")
        return 1
    if candidates:
        print_candidate_table(candidates)
    else:
        console.print("No high/medium-confidence candidates in the main list.")
    if low_confidence:
        console.print(
            f"Low-confidence papers excluded from the main list: {len(low_confidence)}. "
            "They are under low_confidence_candidates in the YAML file."
        )
    console.print("Set action: download to approve a candidate paper, or action: ignore to skip it.")
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
        console.print("No papers were approved for download.")
        console.print("Edit the candidate YAML and set action: download for selected candidate papers.")
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
        console.print("No arXiv IDs were processed.")
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
        console.print(f"Seed file not found: {seed_file}")
        return 1
    if not results:
        console.print(f"No arXiv IDs found in {seed_file}.")
        return 0
    _print_download_results(results)
    return 0


def _resolve_skip_existing(force: bool, skip_existing: bool) -> bool | None:
    if force and skip_existing:
        console.print("Choose either --force or --skip-existing, not both.")
        return None
    return skip_existing or not force


def _print_download_results(results: list) -> None:
    downloaded = sum(1 for result in results if result.status in {"downloaded", "metadata_only"})
    skipped = sum(1 for result in results if result.status.startswith("skipped"))
    duplicates = sum(1 for result in results if result.duplicate)
    failed = len(results) - downloaded - skipped
    console.print(f"Papers processed: {len(results)}")
    console.print(f"Papers downloaded or recorded: {downloaded}")
    console.print(f"Papers skipped: {skipped}")
    console.print(f"Papers failed: {failed}")
    console.print(f"Duplicates detected: {duplicates}")
    for result in results:
        console.print(
            f"- {result.arxiv_id}{result.version or ''}: {result.status}; "
            f"source={'yes' if result.source_downloaded else 'no'}; "
            f"pdf={'yes' if result.pdf_downloaded else 'no'}; "
            f"path={result.path or 'n/a'}"
        )
        for error in result.errors:
            console.print(f"  error: {error}")


def print_candidate_table(candidates: list[PaperCandidate]) -> None:
    console.print("Rank | Score | Confidence | arXiv ID | Year | Title | Authors | Reasons | Action")
    console.print("-" * 125)
    for rank, candidate in enumerate(candidates, start=1):
        authors = ", ".join(candidate.authors[:3])
        if len(candidate.authors) > 3:
            authors += " et al."
        reasons = "; ".join(candidate.ranking_reasons[:3])
        console.print(
            f"{rank} | {candidate.score:.3f} | {candidate.confidence} | {candidate.arxiv_id}{candidate.version or ''} | "
            f"{candidate.year or ''} | {_shorten(candidate.title, 46)} | "
            f"{_shorten(authors, 30)} | {_shorten(reasons, 52)} | {candidate.action}"
        )


def _shorten(value: str, max_chars: int) -> str:
    if len(value) <= max_chars:
        return value
    return value[: max_chars - 3].rstrip() + "..."


if TYPER_AVAILABLE:  # pragma: no cover - optional dependency
    app = typer.Typer(help="Local-first RAG for mathematical research documents.")

    @app.command()
    def ingest(
        corpus_path: str,
        index_dir: str = typer.Option(DEFAULT_INDEX_DIR, help="Local index directory."),
        metadata: str | None = typer.Option(None, help="Optional metadata YAML file."),
    ) -> None:
        raise typer.Exit(run_ingest(corpus_path, index_dir, metadata))

    @app.command()
    def search(
        query: str,
        index_dir: str = typer.Option(DEFAULT_INDEX_DIR, help="Local index directory."),
        mode: str = typer.Option("hybrid", help="keyword, vector, or hybrid."),
        top_k: int = typer.Option(10, help="Number of chunks to show."),
    ) -> None:
        raise typer.Exit(run_search(query, index_dir, mode, top_k))

    @app.command()
    def ask(
        query: str,
        index_dir: str = typer.Option(DEFAULT_INDEX_DIR, help="Local index directory."),
        mode: str = typer.Option("hybrid", help="keyword, vector, or hybrid."),
        top_k: int = typer.Option(6, help="Number of chunks to inspect."),
    ) -> None:
        raise typer.Exit(run_ask(query, index_dir, mode, top_k))

    @app.command()
    def stats(index_dir: str = typer.Option(DEFAULT_INDEX_DIR, help="Local index directory.")) -> None:
        raise typer.Exit(run_stats(index_dir))

    @app.command("eval")
    def eval_cmd(
        eval_path: str,
        index_dir: str = typer.Option(DEFAULT_INDEX_DIR, help="Local index directory."),
        mode: str = typer.Option("hybrid", help="keyword, vector, or hybrid."),
        top_k: int = typer.Option(5, help="Number of retrieved chunks to score."),
    ) -> None:
        raise typer.Exit(run_eval(eval_path, index_dir, mode, top_k))

    @app.command()
    def discover(
        query: str | None = typer.Argument(None, help="Search query for arXiv discovery."),
        config: str | None = typer.Option(None, help="Discovery config YAML."),
        output: str = typer.Option(DEFAULT_CANDIDATES_PATH, help="Candidate YAML output path."),
        index_dir: str = typer.Option(DEFAULT_INDEX_DIR, help="Existing local index for corpus keyword hints."),
        max_results: int | None = typer.Option(None, help="Maximum candidate papers to store."),
        sort_by: str = typer.Option("relevance", help="relevance or newest."),
        verbose: bool = typer.Option(False, help="Print the arXiv search_query used."),
    ) -> None:
        raise typer.Exit(run_discover(query, config, output, index_dir, max_results, sort_by, verbose))

    @app.command()
    def review_candidates(candidates_path: str = typer.Argument(DEFAULT_CANDIDATES_PATH)) -> None:
        raise typer.Exit(run_review_candidates(candidates_path))

    @app.command()
    def download_approved(
        candidates_path: str = typer.Argument(DEFAULT_CANDIDATES_PATH),
        corpus_dir: str = typer.Option(DEFAULT_ARXIV_CORPUS_DIR, help="arXiv corpus directory."),
        config: str | None = typer.Option(None, help="Discovery/download config YAML."),
        auto_download: bool = typer.Option(False, help="Explicitly allow capped download of pending candidates."),
        limit: int | None = typer.Option(None, help="Maximum papers to download this run."),
        overwrite: bool = typer.Option(False, help="Overwrite existing paper folders."),
    ) -> None:
        raise typer.Exit(run_download_approved(candidates_path, corpus_dir, config, auto_download, limit, overwrite))

    @app.command()
    def download_arxiv(
        arxiv_ids: list[str] = typer.Argument(..., help="One or more arXiv IDs."),
        corpus_dir: str = typer.Option(DEFAULT_ARXIV_CORPUS_DIR, help="arXiv corpus directory."),
        config: str | None = typer.Option(None, help="Discovery/download config YAML."),
        limit: int | None = typer.Option(None, help="Maximum IDs to download this run."),
        force: bool = typer.Option(False, help="Replace an existing paper folder."),
        skip_existing: bool = typer.Option(False, help="Skip existing paper folders; this is the default behavior."),
    ) -> None:
        raise typer.Exit(run_download_arxiv(arxiv_ids, corpus_dir, config, limit, force, skip_existing))

    @app.command()
    def download_seed(
        seed_file: str = typer.Argument("arxiv_seed_core.txt", help="Seed file with one arXiv ID per line."),
        corpus_dir: str = typer.Option(DEFAULT_ARXIV_CORPUS_DIR, help="arXiv corpus directory."),
        config: str | None = typer.Option(None, help="Discovery/download config YAML."),
        max_papers: int = typer.Option(
            DEFAULT_SEED_MAX_PAPERS,
            "--max-papers",
            "--limit",
            help=(
                "Maximum papers to download or record this run; existing and not-found papers do not count "
                f"(default: {DEFAULT_SEED_MAX_PAPERS})."
            ),
        ),
        force: bool = typer.Option(False, help="Replace existing paper folders."),
        skip_existing: bool = typer.Option(False, help="Skip existing paper folders; this is the default behavior."),
    ) -> None:
        raise typer.Exit(run_download_seed(seed_file, corpus_dir, config, max_papers, force, skip_existing))


def _argparse_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local-first RAG for mathematical research documents.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest")
    ingest_parser.add_argument("corpus_path")
    ingest_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    ingest_parser.add_argument("--metadata", default=None)

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    search_parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    search_parser.add_argument("--top-k", type=int, default=10)

    ask_parser = subparsers.add_parser("ask")
    ask_parser.add_argument("query")
    ask_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    ask_parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    ask_parser.add_argument("--top-k", type=int, default=6)

    stats_parser = subparsers.add_parser("stats")
    stats_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)

    eval_parser = subparsers.add_parser("eval")
    eval_parser.add_argument("eval_path")
    eval_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    eval_parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    eval_parser.add_argument("--top-k", type=int, default=5)

    discover_parser = subparsers.add_parser("discover")
    discover_parser.add_argument("query", nargs="?")
    discover_parser.add_argument("--config", default=None)
    discover_parser.add_argument("--output", default=DEFAULT_CANDIDATES_PATH)
    discover_parser.add_argument("--index-dir", default=DEFAULT_INDEX_DIR)
    discover_parser.add_argument("--max-results", type=int, default=None)
    discover_parser.add_argument("--sort-by", default="relevance", choices=["relevance", "newest"])
    discover_parser.add_argument("--verbose", action="store_true")

    review_parser = subparsers.add_parser("review-candidates")
    review_parser.add_argument("candidates_path", nargs="?", default=DEFAULT_CANDIDATES_PATH)

    download_parser = subparsers.add_parser("download-approved")
    download_parser.add_argument("candidates_path", nargs="?", default=DEFAULT_CANDIDATES_PATH)
    download_parser.add_argument("--corpus-dir", default=DEFAULT_ARXIV_CORPUS_DIR)
    download_parser.add_argument("--config", default=None)
    download_parser.add_argument("--auto-download", action="store_true")
    download_parser.add_argument("--limit", type=int, default=None)
    download_parser.add_argument("--overwrite", action="store_true")

    download_arxiv_parser = subparsers.add_parser("download-arxiv")
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

    download_seed_parser = subparsers.add_parser("download-seed")
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
        return run_ingest(args.corpus_path, args.index_dir, args.metadata)
    if args.command == "search":
        return run_search(args.query, args.index_dir, args.mode, args.top_k)
    if args.command == "ask":
        return run_ask(args.query, args.index_dir, args.mode, args.top_k)
    if args.command == "stats":
        return run_stats(args.index_dir)
    if args.command == "eval":
        return run_eval(args.eval_path, args.index_dir, args.mode, args.top_k)
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


def main(argv: list[str] | None = None) -> int:
    if TYPER_AVAILABLE:  # pragma: no cover - optional dependency
        app()
        return 0
    return _argparse_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
