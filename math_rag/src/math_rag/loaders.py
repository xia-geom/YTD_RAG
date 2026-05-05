"""Document loading and first-pass chunking."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

from .config import SUPPORTED_SUFFIXES
from .latex_chunker import chunk_latex_file, make_chunk_id
from .models import Chunk, DocumentMetadata, metadata_from_dict
from .paper_store import load_yaml_file
from .pdf_loader import load_pdf_chunks
from .text_cleaning import extract_symbols


PDF_SHADOWING_SUFFIXES = {".tex", ".md", ".markdown"}
AGENT_LOG_DIR_NAME = "agent_logs"


def discover_files(corpus_path: str | Path) -> list[Path]:
    root = Path(corpus_path)
    if root.is_file():
        return [root] if root.suffix.lower() in SUPPORTED_SUFFIXES else []
    if not root.exists():
        return []
    files: list[Path] = []
    arxiv_governed: set[Path] = set()
    for path in root.rglob("*"):
        if any(part.startswith(".") for part in path.parts):
            continue
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        arxiv_decision = should_ingest_arxiv_file(path)
        if arxiv_decision is False:
            continue
        if arxiv_decision is True:
            arxiv_governed.add(path)
        files.append(path)

    text_stems_by_dir: dict[Path, set[str]] = {}
    for path in files:
        if path in arxiv_governed:
            continue
        if path.suffix.lower() in PDF_SHADOWING_SUFFIXES:
            text_stems_by_dir.setdefault(path.parent, set()).add(path.stem)

    filtered: list[Path] = []
    for path in files:
        if (
            path.suffix.lower() == ".pdf"
            and path not in arxiv_governed
            and path.stem in text_stems_by_dir.get(path.parent, set())
        ):
            continue
        filtered.append(path)
    return sorted(filtered)


def load_metadata_map(metadata_path: str | Path | None = None) -> dict[str, DocumentMetadata]:
    if metadata_path is None:
        metadata_path = Path("metadata/documents.yaml")
    path = Path(metadata_path)
    if not path.exists():
        return {}
    try:
        import yaml  # type: ignore
    except Exception:
        return {}
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    documents = raw.get("documents", raw) if isinstance(raw, dict) else {}
    result: dict[str, DocumentMetadata] = {}
    for source_path, values in documents.items():
        if not isinstance(values, dict):
            continue
        data = {"source_path": str(source_path), **values}
        result[str(source_path)] = metadata_from_dict(data)
        result[str(Path(source_path))] = result[str(source_path)]
    return result


def default_metadata(path: Path) -> DocumentMetadata:
    suffix = path.suffix.lower()
    document_type = "other"
    if suffix == ".bib":
        document_type = "bibtex"
    elif suffix in {".md", ".markdown"}:
        document_type = "markdown"
    return DocumentMetadata(source_path=str(path), title=path.stem.replace("_", " "), document_type=document_type)


def metadata_for_path(path: Path, metadata_map: dict[str, DocumentMetadata]) -> DocumentMetadata:
    keys = [str(path), path.as_posix(), str(Path(path.name)), path.name]
    for key in keys:
        if key in metadata_map:
            meta = metadata_map[key]
            meta.source_path = str(path)  # type: ignore[misc]
            return meta
    arxiv_metadata = arxiv_metadata_for_path(path)
    if arxiv_metadata:
        return DocumentMetadata(
            source_path=str(path),
            title=arxiv_metadata.get("title") or path.stem.replace("_", " "),
            authors=list(arxiv_metadata.get("authors") or []),
            year=arxiv_metadata.get("year"),
            document_type="paper",
            topics=list(arxiv_metadata.get("topics") or []),
            notes=f"arXiv {arxiv_metadata.get('arxiv_id')} {arxiv_metadata.get('version') or ''}".strip(),
        )
    return default_metadata(path)


def load_file(path: str | Path, metadata: DocumentMetadata | None = None) -> list[Chunk]:
    file_path = Path(path)
    meta = metadata or default_metadata(file_path)
    suffix = file_path.suffix.lower()
    if suffix == ".tex":
        chunks = chunk_latex_file(file_path, meta)
    elif suffix in {".md", ".markdown", ".txt"}:
        chunks = load_text_chunks(file_path, meta)
    elif suffix == ".bib":
        chunks = load_bibtex_chunks(file_path, meta)
    elif suffix == ".pdf":
        chunks = load_pdf_chunks(file_path, meta)
    else:
        chunks = []
    decorate_arxiv_chunks(file_path, chunks)
    decorate_agent_log_chunks(file_path, chunks)
    return chunks


def should_ingest_arxiv_file(path: Path) -> bool | None:
    metadata = arxiv_metadata_for_path(path)
    if not metadata:
        return None
    primary = metadata.get("primary_ingestion")
    if primary == "tex":
        return "source" in path.parts and path.suffix.lower() in {".tex", ".bib", ".md", ".txt"}
    if primary == "pdf":
        return path.name == "paper.pdf"
    if primary == "metadata":
        return False
    return None


def arxiv_metadata_for_path(path: Path) -> dict[str, Any] | None:
    for parent in [path.parent, *path.parents]:
        metadata_path = parent / "metadata.yaml"
        if metadata_path.exists():
            data = load_yaml_file(metadata_path)
            if data.get("arxiv_id"):
                return data
    return None


def decorate_arxiv_chunks(path: Path, chunks: list[Chunk]) -> None:
    metadata = arxiv_metadata_for_path(path)
    if not metadata:
        return
    ingestion_source = "pdf" if path.suffix.lower() == ".pdf" else "tex"
    for chunk in chunks:
        chunk.metadata.update(
            {
                "arxiv_id": metadata.get("arxiv_id"),
                "arxiv_version": metadata.get("version"),
                "primary_ingestion": metadata.get("primary_ingestion"),
                "ingestion_source": ingestion_source,
                "downloaded_at": metadata.get("downloaded_at"),
                "source_available": metadata.get("source_available"),
                "pdf_available": metadata.get("pdf_available"),
                "requested_arxiv_id": metadata.get("requested_arxiv_id"),
                "download_status": metadata.get("download_status"),
                "source_url": metadata.get("source_url"),
                "pdf_url": metadata.get("pdf_url"),
            }
        )


def is_agent_log_path(path: Path) -> bool:
    return AGENT_LOG_DIR_NAME in path.parts


def decorate_agent_log_chunks(path: Path, chunks: list[Chunk]) -> None:
    if not is_agent_log_path(path):
        return
    for chunk in chunks:
        chunk.metadata["source_kind"] = "agent_log"


def load_corpus(
    corpus_path: str | Path,
    metadata_path: str | Path | None = None,
) -> tuple[list[Chunk], list[str]]:
    metadata_map = load_metadata_map(metadata_path)
    chunks: list[Chunk] = []
    warnings: list[str] = []
    for path in discover_files(corpus_path):
        metadata = metadata_for_path(path, metadata_map)
        try:
            chunks.extend(load_file(path, metadata))
        except Exception as exc:
            warnings.append(f"Skipped {path}: {exc}")
    return chunks, warnings


HEADING_RE = re.compile(r"^(?P<level>#{1,6})\s+(?P<title>.+?)\s*$")


def load_text_chunks(path: Path, metadata: DocumentMetadata) -> list[Chunk]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    chunks: list[Chunk] = []
    section_path: list[str] = []
    buffer: list[tuple[int, str]] = []

    def flush() -> None:
        nonlocal buffer
        if not buffer:
            return
        content = "".join(line for _, line in buffer).strip()
        if content:
            line_start = buffer[0][0]
            line_end = buffer[-1][0]
            chunks.append(
                Chunk(
                    chunk_id=make_chunk_id(str(path), line_start, line_end, "text", content),
                    source_path=str(path),
                    title=metadata.title,
                    chunk_type="text",
                    section_path=list(section_path),
                    line_start=line_start,
                    line_end=line_end,
                    content=content,
                    metadata={"source_format": path.suffix.lower().lstrip(".") or "text"},
                    symbols=extract_symbols(content),
                    topics=list(metadata.topics),
                )
            )
        buffer = []

    for index, line in enumerate(lines, start=1):
        heading = HEADING_RE.match(line)
        if heading:
            flush()
            level = len(heading.group("level"))
            section_path = section_path[: level - 1] + [heading.group("title").strip()]
        buffer.append((index, line))
        if sum(len(raw) for _, raw in buffer) > 2500 and not line.strip():
            flush()
    flush()
    return chunks


ENTRY_START_RE = re.compile(r"@(?P<type>[A-Za-z]+)\s*\{\s*(?P<key>[^,\s]+)\s*,", re.MULTILINE)
FIELD_RE = re.compile(r"(?P<name>[A-Za-z][A-Za-z0-9_-]*)\s*=\s*(?P<value>\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|[^,\n]+)", re.MULTILINE)


def _find_bib_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    for match in ENTRY_START_RE.finditer(text):
        start = match.start()
        brace_index = text.find("{", match.start())
        depth = 0
        end = len(text)
        for pos in range(brace_index, len(text)):
            if text[pos] == "{":
                depth += 1
            elif text[pos] == "}":
                depth -= 1
                if depth == 0:
                    end = pos + 1
                    break
        entries.append((match.group("type"), match.group("key"), text[start:end]))
    return entries


def _clean_bib_value(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    if (value.startswith("{") and value.endswith("}")) or (value.startswith('"') and value.endswith('"')):
        value = value[1:-1]
    return re.sub(r"\s+", " ", value).strip()


def parse_bibtex_entry(entry_text: str) -> dict[str, str]:
    return {match.group("name").lower(): _clean_bib_value(match.group("value")) for match in FIELD_RE.finditer(entry_text)}


def load_bibtex_chunks(path: Path, metadata: DocumentMetadata) -> list[Chunk]:
    text = path.read_text(encoding="utf-8", errors="replace")
    chunks: list[Chunk] = []
    for entry_type, key, entry_text in _find_bib_entries(text):
        fields = parse_bibtex_entry(entry_text)
        title = fields.get("title") or key
        authors = fields.get("author", "")
        year = fields.get("year", "")
        venue = fields.get("journal") or fields.get("booktitle") or fields.get("eprint") or fields.get("archiveprefix", "")
        content = "\n".join(
            part
            for part in [
                f"Citation key: {key}",
                f"Entry type: {entry_type}",
                f"Title: {title}",
                f"Authors: {authors}" if authors else "",
                f"Year: {year}" if year else "",
                f"Venue/arXiv: {venue}" if venue else "",
                entry_text.strip(),
            ]
            if part
        )
        line_start = text[: text.find(entry_text)].count("\n") + 1
        line_end = line_start + entry_text.count("\n")
        digest = hashlib.sha1(f"{path}:{key}:{entry_text[:100]}".encode("utf-8")).hexdigest()[:16]
        chunks.append(
            Chunk(
                chunk_id=f"bib-{digest}",
                source_path=str(path),
                title=title,
                chunk_type="citation_context",
                section_path=[],
                line_start=line_start,
                line_end=line_end,
                content=content,
                metadata={
                    "source_format": "bibtex",
                    "citation_key": key,
                    "entry_type": entry_type,
                    "fields": fields,
                },
                symbols=extract_symbols(content),
                topics=list(metadata.topics),
            )
        )
    return chunks
