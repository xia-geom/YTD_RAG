"""Deterministic metadata enrichment for existing chunks.

This module intentionally does not change chunk boundaries, ids, content, or
types. It only builds a namespaced metadata payload that can later be used by
retrieval/ranking code.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .models import Chunk
from .text_cleaning import normalize_whitespace


ENRICHMENT_VERSION = "metadata_enrichment_v1"
ENRICHMENT_BACKEND = "deterministic_v1"
PROMPT_HASH = ""

SOURCE_ROLE_PRIMARY_PAPER = "primary_paper"
SOURCE_ROLE_PROJECT_NOTE = "project_note"
SOURCE_ROLE_NAVIGATION_NOTE = "navigation_note"
SOURCE_ROLE_BIBLIOGRAPHY_POINTER = "bibliography_pointer"
SOURCE_ROLE_ENGINEERING_MEMORY = "engineering_memory"


def enrich_chunk(chunk: Chunk) -> dict[str, Any]:
    """Return deterministic enrichment metadata for an existing chunk."""

    source_role = source_role_for_path(chunk.source_path)
    is_navigation_note = source_role == SOURCE_ROLE_NAVIGATION_NOTE
    return {
        "semantic_title": semantic_title_for_chunk(chunk),
        "retrieval_summary": retrieval_summary_for_chunk(chunk),
        "source_role": source_role,
        "is_navigation_note": is_navigation_note,
        "depends_on_previous": chunk.chunk_type == "proof",
        "concept_tags": enrichment_concept_tags(chunk),
    }


def source_role_for_path(source_path: str) -> str:
    """Classify source role using conservative path heuristics."""

    normalized = Path(source_path).as_posix()
    parts = set(Path(normalized).parts)
    if "agent_logs" in parts:
        return SOURCE_ROLE_ENGINEERING_MEMORY
    if normalized == "corpus/my_notes/project_paper_index.md" or normalized.endswith(
        "/corpus/my_notes/project_paper_index.md"
    ):
        return SOURCE_ROLE_NAVIGATION_NOTE
    if normalized == "corpus/my_notes/requested_non_arxiv_sources.md" or normalized.endswith(
        "/corpus/my_notes/requested_non_arxiv_sources.md"
    ):
        return SOURCE_ROLE_BIBLIOGRAPHY_POINTER
    if "corpus" in parts and "arxiv" in parts:
        return SOURCE_ROLE_PRIMARY_PAPER
    if normalized.startswith("corpus/my_notes/") or "/corpus/my_notes/" in normalized:
        return SOURCE_ROLE_PROJECT_NOTE
    return SOURCE_ROLE_PROJECT_NOTE


def semantic_title_for_chunk(chunk: Chunk) -> str:
    """Build a short deterministic title-like label."""

    if chunk.section_path:
        title = " > ".join(value for value in chunk.section_path if value)
    elif chunk.title:
        title = chunk.title
    else:
        title = Path(chunk.source_path).stem.replace("_", " ")
    title = normalize_whitespace(title)
    if chunk.chunk_type and chunk.chunk_type != "text":
        return f"{chunk.chunk_type}: {title}" if title else chunk.chunk_type
    return title


def retrieval_summary_for_chunk(chunk: Chunk, max_chars: int = 360) -> str:
    """Return a compact original-text-derived retrieval summary."""

    content = normalize_whitespace(chunk.content)
    if len(content) <= max_chars:
        return content
    return content[: max_chars - 3].rstrip() + "..."


def enrichment_concept_tags(chunk: Chunk) -> list[str]:
    """Reuse existing concept/topic tags without replacing original metadata."""

    tags: list[str] = []
    metadata = chunk.metadata if isinstance(chunk.metadata, dict) else {}
    for value in metadata.get("concept_tags", []):
        if isinstance(value, str) and value and value not in tags:
            tags.append(value)
    for value in chunk.topics:
        if isinstance(value, str) and value and value not in tags:
            tags.append(value)
    return tags
