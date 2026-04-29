"""Citation formatting for retrieved chunks."""

from __future__ import annotations

from .models import Chunk, SearchResult


def format_section_path(chunk: Chunk) -> str:
    return " > ".join(part for part in chunk.section_path if part) if chunk.section_path else "unsectioned"


def format_location(chunk: Chunk) -> str:
    parts = [chunk.source_path]
    if chunk.section_path:
        parts.append(format_section_path(chunk))
    if chunk.page_number is not None:
        parts.append(f"p. {chunk.page_number}")
    if chunk.line_start is not None and chunk.line_end is not None:
        if chunk.line_start == chunk.line_end:
            parts.append(f"line {chunk.line_start}")
        else:
            parts.append(f"lines {chunk.line_start}-{chunk.line_end}")
    elif chunk.line_start is not None:
        parts.append(f"line {chunk.line_start}")
    return ", ".join(parts)


def format_citation(chunk: Chunk) -> str:
    return f"[{format_location(chunk)}]"


def format_result_header(result: SearchResult) -> str:
    chunk = result.chunk
    return (
        f"{result.rank or '-'} | score={result.score:.3f} | "
        f"{chunk.source_path} | {chunk.chunk_type} | {format_section_path(chunk)}"
    )


def unique_sources(results: list[SearchResult]) -> list[str]:
    seen: set[str] = set()
    sources: list[str] = []
    for result in results:
        source = result.chunk.source_path
        if source not in seen:
            seen.add(source)
            sources.append(source)
    return sources

