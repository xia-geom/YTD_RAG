"""PDF text extraction."""

from __future__ import annotations

import hashlib
from pathlib import Path

from .models import Chunk, DocumentMetadata
from .text_cleaning import extract_symbols, normalize_whitespace


def _chunk_id(source_path: str, page_number: int, offset: int, content: str) -> str:
    digest = hashlib.sha1(f"{source_path}:{page_number}:{offset}:{content[:80]}".encode("utf-8")).hexdigest()[:16]
    return f"pdf-{digest}"


def _page_groups(text: str, max_chars: int = 2500) -> list[str]:
    paragraphs = [para.strip() for para in text.split("\n\n") if para.strip()]
    if not paragraphs:
        cleaned = normalize_whitespace(text)
        return [cleaned] if cleaned else []
    groups: list[str] = []
    current: list[str] = []
    current_len = 0
    for para in paragraphs:
        if current and current_len + len(para) > max_chars:
            groups.append("\n\n".join(current))
            current = []
            current_len = 0
        current.append(para)
        current_len += len(para)
    if current:
        groups.append("\n\n".join(current))
    return groups


def load_pdf_chunks(path: str | Path, metadata: DocumentMetadata | None = None) -> list[Chunk]:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception as exc:  # pragma: no cover - depends on optional package
        raise RuntimeError("PDF ingestion requires the optional package pypdf. Install with: pip install -e '.[preferred]'") from exc

    source_path = str(path)
    reader = PdfReader(source_path)
    chunks: list[Chunk] = []
    title = metadata.title if metadata else None
    topics = list(metadata.topics) if metadata else []

    for page_index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        for offset, group in enumerate(_page_groups(text), start=1):
            content = group.strip()
            if not content:
                continue
            chunks.append(
                Chunk(
                    chunk_id=_chunk_id(source_path, page_index, offset, content),
                    source_path=source_path,
                    title=title,
                    chunk_type="text",
                    section_path=[],
                    page_number=page_index,
                    content=content,
                    metadata={"source_format": "pdf", "page_group": offset},
                    symbols=extract_symbols(content),
                    topics=topics,
                )
            )
    return chunks

