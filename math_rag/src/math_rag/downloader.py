"""Download approved arXiv candidate papers into the local corpus."""

from __future__ import annotations

import gzip
import io
import shutil
import tarfile
import urllib.error
from pathlib import Path

from .arxiv_client import ARXIV_PDF_URL, ARXIV_SOURCE_URL, ArxivClient, ArxivPaper, ParsedArxivID, parse_arxiv_id
from .paper_ranker import load_discovery_config
from .paper_store import (
    DEFAULT_ARXIV_CORPUS_DIR,
    DownloadResult,
    PaperCandidate,
    approved_candidates,
    build_paper_metadata,
    is_duplicate,
    load_candidates,
    paper_dir,
    write_paper_metadata,
)


INGESTIBLE_SOURCE_SUFFIXES = {".tex"}


def download_approved_papers(
    candidates_path: str,
    corpus_arxiv_dir: str = DEFAULT_ARXIV_CORPUS_DIR,
    config_path: str | None = None,
    auto_download: bool = False,
    limit: int | None = None,
    overwrite: bool = False,
    client: ArxivClient | None = None,
) -> list[DownloadResult]:
    config = load_discovery_config(config_path)
    policy = config.download_policy
    candidates = load_candidates(candidates_path)
    if auto_download and policy.require_approval:
        auto_download = False
    if auto_download and limit is None:
        limit = min(3, policy.max_papers_per_run)
    if not auto_download:
        selected = approved_candidates(candidates, auto_download=False, limit=limit or policy.max_papers_per_run)
    else:
        selected = approved_candidates(candidates, auto_download=True, limit=limit)
    client = client or ArxivClient(delay_seconds=policy.delay_seconds_between_requests)
    return _download_candidates(
        selected,
        corpus_arxiv_dir,
        policy.download_source,
        policy.download_pdf,
        force=overwrite,
        client=client,
        avoid_duplicates=policy.avoid_duplicates,
    )


def download_seed_file(
    seed_path: str | Path,
    corpus_arxiv_dir: str = DEFAULT_ARXIV_CORPUS_DIR,
    config_path: str | None = None,
    limit: int | None = None,
    force: bool = False,
    skip_existing: bool = True,
    client: ArxivClient | None = None,
) -> list[DownloadResult]:
    return download_arxiv_ids(
        read_seed_arxiv_ids(seed_path),
        corpus_arxiv_dir=corpus_arxiv_dir,
        config_path=config_path,
        limit=limit,
        force=force,
        skip_existing=skip_existing,
        client=client,
    )


def read_seed_arxiv_ids(seed_path: str | Path) -> list[str]:
    ids: list[str] = []
    for line in Path(seed_path).read_text(encoding="utf-8").splitlines():
        value = line.split("#", 1)[0].strip()
        if value:
            ids.append(value)
    return ids


def download_arxiv_ids(
    arxiv_ids: list[str],
    corpus_arxiv_dir: str = DEFAULT_ARXIV_CORPUS_DIR,
    config_path: str | None = None,
    limit: int | None = None,
    force: bool = False,
    skip_existing: bool = True,
    client: ArxivClient | None = None,
) -> list[DownloadResult]:
    config = load_discovery_config(config_path)
    policy = config.download_policy
    client = client or ArxivClient(delay_seconds=policy.delay_seconds_between_requests)
    effective_limit = limit if limit is not None else policy.max_papers_per_run
    entries = _parse_requested_ids(arxiv_ids, effective_limit)

    indexed_results: dict[int, DownloadResult] = {}
    pending: list[tuple[int, ParsedArxivID]] = []
    for index, entry in enumerate(entries):
        if isinstance(entry, DownloadResult):
            indexed_results[index] = entry
            continue
        existing_result = _existing_result(entry, corpus_arxiv_dir, force, skip_existing, policy.avoid_duplicates)
        if existing_result is not None:
            indexed_results[index] = existing_result
        else:
            pending.append((index, entry))

    if pending:
        papers, metadata_errors = _fetch_papers_with_isolation(client, pending)
        for index, parsed in pending:
            metadata_error = metadata_errors.get(parsed.id_with_version)
            if metadata_error:
                indexed_results[index] = DownloadResult(
                    arxiv_id=parsed.arxiv_id,
                    version=parsed.version,
                    status="metadata_unavailable",
                    path=str(paper_dir(corpus_arxiv_dir, parsed.arxiv_id)),
                    errors=[f"metadata unavailable: {metadata_error}"],
                )
                continue
            paper = _find_paper_for_request(parsed, papers)
            if paper is None:
                indexed_results[index] = DownloadResult(
                    arxiv_id=parsed.arxiv_id,
                    version=parsed.version,
                    status="not_found",
                    path=str(paper_dir(corpus_arxiv_dir, parsed.arxiv_id)),
                    errors=["arXiv metadata lookup returned no matching paper."],
                )
                continue
            candidate = _candidate_from_paper(paper, parsed)
            indexed_results[index] = _download_one_safely(
                candidate,
                corpus_arxiv_dir,
                policy.download_source,
                policy.download_pdf,
                force,
                client,
                requested_arxiv_id=parsed.id_with_version,
            )
    return [indexed_results[index] for index in sorted(indexed_results)]


def _fetch_papers_with_isolation(
    client: ArxivClient,
    pending: list[tuple[int, ParsedArxivID]],
) -> tuple[list[ArxivPaper], dict[str, Exception]]:
    requested_ids = [parsed.id_with_version for _, parsed in pending]
    try:
        return client.fetch_by_ids(requested_ids), {}
    except Exception as exc:
        if len(requested_ids) <= 1 or _is_rate_limit_error(exc):
            return [], {identifier: exc for identifier in requested_ids}

    papers: list[ArxivPaper] = []
    errors: dict[str, Exception] = {}
    for identifier in requested_ids:
        try:
            papers.extend(client.fetch_by_ids([identifier]))
        except Exception as exc:
            errors[identifier] = exc
    return papers, errors


def _is_rate_limit_error(exc: Exception) -> bool:
    return isinstance(exc, urllib.error.HTTPError) and exc.code == 429


def _download_candidates(
    candidates: list[PaperCandidate],
    corpus_arxiv_dir: str,
    download_source: bool,
    download_pdf: bool,
    force: bool,
    client: ArxivClient,
    avoid_duplicates: bool = True,
) -> list[DownloadResult]:
    results: list[DownloadResult] = []
    for candidate in candidates:
        if avoid_duplicates and is_duplicate(candidate, corpus_arxiv_dir) and not force:
            results.append(
                DownloadResult(
                    arxiv_id=candidate.arxiv_id,
                    version=candidate.version,
                    status="skipped_duplicate",
                    path=str(paper_dir(corpus_arxiv_dir, candidate.arxiv_id)),
                    duplicate=True,
                )
            )
            continue
        results.append(_download_one_safely(candidate, corpus_arxiv_dir, download_source, download_pdf, force, client))
    return results


def _download_one_safely(
    candidate: PaperCandidate,
    corpus_arxiv_dir: str,
    download_source: bool,
    download_pdf: bool,
    force: bool,
    client: ArxivClient,
    requested_arxiv_id: str | None = None,
) -> DownloadResult:
    try:
        return _download_one(
            candidate,
            corpus_arxiv_dir,
            download_source,
            download_pdf,
            force,
            client,
            requested_arxiv_id=requested_arxiv_id,
        )
    except Exception as exc:
        return DownloadResult(
            arxiv_id=candidate.arxiv_id,
            version=candidate.version,
            status="failed",
            path=str(paper_dir(corpus_arxiv_dir, candidate.arxiv_id)),
            errors=[f"download failed: {exc}"],
        )


def _download_one(
    candidate: PaperCandidate,
    corpus_arxiv_dir: str,
    download_source: bool,
    download_pdf: bool,
    force: bool,
    client: ArxivClient,
    requested_arxiv_id: str | None = None,
) -> DownloadResult:
    root = paper_dir(corpus_arxiv_dir, candidate.arxiv_id)
    if root.exists() and not force:
        return DownloadResult(
            arxiv_id=candidate.arxiv_id,
            version=candidate.version,
            status="skipped_existing_folder",
            path=str(root),
            duplicate=True,
            errors=["Paper folder exists; pass --force or --overwrite to replace it."],
        )
    if root.exists() and force:
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)
    (root / "source").mkdir(exist_ok=True)
    (root / "extracted").mkdir(exist_ok=True)

    errors: list[str] = []
    source_available = False
    ingestible_source_available = False
    pdf_available = False

    if download_source and candidate.source_url:
        try:
            source_bytes = client.download_bytes(candidate.source_url)
            source_available, ingestible_source_available = _store_source_bytes(source_bytes, root / "source")
        except Exception as exc:
            errors.append(f"source unavailable: {exc}")

    if download_pdf and candidate.pdf_url:
        try:
            pdf_bytes = client.download_bytes(candidate.pdf_url)
            if pdf_bytes:
                (root / "paper.pdf").write_bytes(pdf_bytes)
                pdf_available = True
        except Exception as exc:
            errors.append(f"pdf unavailable: {exc}")

    primary_ingestion = "tex" if ingestible_source_available else "pdf" if pdf_available else "metadata"
    metadata = build_paper_metadata(
        candidate,
        source_available=source_available,
        pdf_available=pdf_available,
        primary_ingestion=primary_ingestion,
        topics=_topics_from_reasons(candidate),
        requested_arxiv_id=requested_arxiv_id,
        download_status="downloaded" if source_available or pdf_available else "metadata_only",
        download_errors=errors,
    )
    write_paper_metadata(corpus_arxiv_dir, candidate, metadata)
    status = "downloaded" if source_available or pdf_available else "metadata_only"
    return DownloadResult(
        arxiv_id=candidate.arxiv_id,
        version=candidate.version,
        status=status,
        path=str(root),
        source_downloaded=source_available,
        pdf_downloaded=pdf_available,
        errors=errors,
    )


def _parse_requested_ids(arxiv_ids: list[str], limit: int | None) -> list[ParsedArxivID | DownloadResult]:
    entries: list[ParsedArxivID | DownloadResult] = []
    seen: set[str] = set()
    valid_count = 0
    for raw_id in arxiv_ids:
        try:
            parsed = parse_arxiv_id(raw_id)
        except ValueError as exc:
            entries.append(DownloadResult(arxiv_id=raw_id.strip(), version=None, status="invalid_id", errors=[str(exc)]))
            continue
        if parsed.id_with_version in seen:
            continue
        seen.add(parsed.id_with_version)
        if limit is not None and valid_count >= limit:
            entries.append(
                DownloadResult(
                    arxiv_id=parsed.arxiv_id,
                    version=parsed.version,
                    status="skipped_limit",
                    errors=[f"Download limit reached before {parsed.id_with_version}."],
                )
            )
            continue
        entries.append(parsed)
        valid_count += 1
    return entries


def _existing_result(
    parsed: ParsedArxivID,
    corpus_arxiv_dir: str,
    force: bool,
    skip_existing: bool,
    avoid_duplicates: bool,
) -> DownloadResult | None:
    if force:
        return None
    candidate = PaperCandidate(
        arxiv_id=parsed.arxiv_id,
        version=parsed.version,
        title="",
        authors=[],
        year=None,
        arxiv_categories=[],
        abstract="",
    )
    root = paper_dir(corpus_arxiv_dir, parsed.arxiv_id)
    if avoid_duplicates and is_duplicate(candidate, corpus_arxiv_dir):
        return DownloadResult(
            arxiv_id=parsed.arxiv_id,
            version=parsed.version,
            status="skipped_duplicate",
            path=str(root),
            duplicate=True,
        )
    if skip_existing and root.exists():
        return DownloadResult(
            arxiv_id=parsed.arxiv_id,
            version=parsed.version,
            status="skipped_existing_folder",
            path=str(root),
            duplicate=True,
            errors=["Paper folder exists; pass --force to replace it."],
        )
    return None


def _find_paper_for_request(parsed: ParsedArxivID, papers: list[ArxivPaper]) -> ArxivPaper | None:
    for paper in papers:
        if paper.arxiv_id != parsed.arxiv_id:
            continue
        if parsed.version and paper.version != parsed.version:
            continue
        return paper
    return None


def _candidate_from_paper(paper: ArxivPaper, requested: ParsedArxivID) -> PaperCandidate:
    id_with_version = f"{paper.arxiv_id}{paper.version or ''}"
    return PaperCandidate(
        arxiv_id=paper.arxiv_id,
        version=paper.version,
        title=paper.title,
        authors=paper.authors,
        year=paper.year,
        arxiv_categories=paper.categories,
        abstract=paper.abstract,
        score=1.0,
        confidence="explicit",
        ranking_reasons=[f"explicit arXiv ID: {requested.id_with_version}"],
        status="selected",
        action="download",
        source_url=paper.source_url or f"{ARXIV_SOURCE_URL}/{id_with_version}",
        pdf_url=paper.pdf_url or f"{ARXIV_PDF_URL}/{id_with_version}",
    )


def _store_source_bytes(source_bytes: bytes, source_dir: Path) -> tuple[bool, bool]:
    if not source_bytes:
        return False, False
    source_dir.mkdir(parents=True, exist_ok=True)
    if _try_extract_tar(source_bytes, source_dir):
        return True, _has_ingestible_source(source_dir)
    if _try_extract_gzip(source_bytes, source_dir):
        return True, _has_ingestible_source(source_dir)
    name = "source.tex" if b"\\documentclass" in source_bytes[:5000] else "source.dat"
    (source_dir / name).write_bytes(source_bytes)
    return True, _has_ingestible_source(source_dir)


def _try_extract_tar(source_bytes: bytes, source_dir: Path) -> bool:
    try:
        with tarfile.open(fileobj=io.BytesIO(source_bytes), mode="r:*") as archive:
            for member in archive.getmembers():
                if not member.isfile():
                    continue
                target = _safe_member_path(source_dir, member.name)
                if target is None:
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                source = archive.extractfile(member)
                if source is not None:
                    with target.open("wb") as handle:
                        shutil.copyfileobj(source, handle)
        return any(source_dir.iterdir())
    except tarfile.TarError:
        return False


def _try_extract_gzip(source_bytes: bytes, source_dir: Path) -> bool:
    try:
        decompressed = gzip.decompress(source_bytes)
    except OSError:
        return False
    name = "source.tex" if b"\\documentclass" in decompressed[:5000] else "source"
    (source_dir / name).write_bytes(decompressed)
    return True


def _has_ingestible_source(source_dir: Path) -> bool:
    return any(path.is_file() and path.suffix.lower() in INGESTIBLE_SOURCE_SUFFIXES for path in source_dir.rglob("*"))


def _safe_member_path(base: Path, member_name: str) -> Path | None:
    target = (base / member_name).resolve()
    try:
        target.relative_to(base.resolve())
    except ValueError:
        return None
    return target


def _topics_from_reasons(candidate: PaperCandidate) -> list[str]:
    topics: list[str] = []
    for reason in candidate.ranking_reasons:
        if reason.startswith("matched keyword: "):
            topics.append(reason.removeprefix("matched keyword: "))
    seen: set[str] = set()
    result: list[str] = []
    for topic in topics:
        if topic not in seen:
            seen.add(topic)
            result.append(topic)
    return result[:12]
