"""Download approved arXiv candidate papers into the local corpus."""

from __future__ import annotations

import gzip
import io
import shutil
import tarfile
import time
from pathlib import Path

from .arxiv_client import ArxivClient
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


INGESTIBLE_SOURCE_SUFFIXES = {".tex", ".bib", ".md", ".txt"}


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

    results: list[DownloadResult] = []
    for index, candidate in enumerate(selected):
        if policy.avoid_duplicates and is_duplicate(candidate, corpus_arxiv_dir) and not overwrite:
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
        results.append(_download_one(candidate, corpus_arxiv_dir, policy.download_source, policy.download_pdf, overwrite, client))
        if index < len(selected) - 1 and policy.delay_seconds_between_requests > 0:
            time.sleep(policy.delay_seconds_between_requests)
    return results


def _download_one(
    candidate: PaperCandidate,
    corpus_arxiv_dir: str,
    download_source: bool,
    download_pdf: bool,
    overwrite: bool,
    client: ArxivClient,
) -> DownloadResult:
    root = paper_dir(corpus_arxiv_dir, candidate.arxiv_id)
    if root.exists() and not overwrite:
        return DownloadResult(
            arxiv_id=candidate.arxiv_id,
            version=candidate.version,
            status="skipped_existing_folder",
            path=str(root),
            duplicate=True,
            errors=["Paper folder exists; pass --overwrite to replace it."],
        )
    if root.exists() and overwrite:
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
