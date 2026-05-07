"""Deterministic metadata enrichment for existing chunks.

This module intentionally does not change chunk boundaries, ids, content, or
types. It only builds a namespaced metadata payload that can later be used by
retrieval/ranking code.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .models import Chunk
from .text_cleaning import normalize_whitespace


ENRICHMENT_VERSION = "metadata_enrichment_v1"
DETERMINISTIC_ENRICHMENT_BACKEND = "deterministic_v1"
AGENT_JSON_ENRICHMENT_BACKEND = "agent_json_v1"
ENRICHMENT_BACKEND = DETERMINISTIC_ENRICHMENT_BACKEND
PROMPT_HASH = ""

AGENT_SEMANTIC_TITLE_MAX_CHARS = 180
AGENT_RETRIEVAL_SUMMARY_MAX_CHARS = 800
AGENT_NOTE_MAX_CHARS = 400
AGENT_TAG_MAX_COUNT = 16
AGENT_TAG_MAX_CHARS = 80

SOURCE_ROLE_PRIMARY_PAPER = "primary_paper"
SOURCE_ROLE_PROJECT_NOTE = "project_note"
SOURCE_ROLE_NAVIGATION_NOTE = "navigation_note"
SOURCE_ROLE_BIBLIOGRAPHY_POINTER = "bibliography_pointer"
SOURCE_ROLE_ENGINEERING_MEMORY = "engineering_memory"


class MetadataEnrichmentBackend:
    """Backend interface for metadata-only enrichment of deterministic chunks."""

    name = DETERMINISTIC_ENRICHMENT_BACKEND
    version = ENRICHMENT_VERSION
    prompt_hash = PROMPT_HASH

    def __init__(self) -> None:
        self.initial_warnings: list[str] = []

    def enrich_chunks(self, chunks: list[Chunk]) -> tuple[dict[str, dict[str, Any]], list[str]]:
        return {chunk.chunk_id: enrich_chunk(chunk) for chunk in chunks}, []

    def mark_chunks_seen(self, chunks: list[Chunk]) -> None:
        return None

    def validate_cached_chunks(self, chunks: list[Chunk]) -> list[str]:
        return []

    def final_warnings(self) -> list[str]:
        return []


class DeterministicEnrichmentBackend(MetadataEnrichmentBackend):
    """Default backend: deterministic local metadata only."""


class AgentJsonEnrichmentBackend(MetadataEnrichmentBackend):
    """Merge precomputed agent JSONL metadata onto deterministic enrichment."""

    name = AGENT_JSON_ENRICHMENT_BACKEND

    def __init__(self, jsonl_path: str | Path | None):
        super().__init__()
        self.jsonl_path = Path(jsonl_path) if jsonl_path else None
        self.records_by_chunk_id: dict[str, dict[str, Any]] = {}
        self.used_chunk_ids: set[str] = set()
        self.prompt_hash = self._load_records()

    def _load_records(self) -> str:
        if self.jsonl_path is None:
            self.initial_warnings.append(
                "agent_json_v1 requires --agent-enrichment-jsonl; using deterministic fallback."
            )
            return "missing-agent-jsonl"
        if not self.jsonl_path.exists():
            self.initial_warnings.append(
                f"Agent enrichment JSONL not found: {self.jsonl_path}; using deterministic fallback."
            )
            return f"missing:{self.jsonl_path.as_posix()}"

        content = self.jsonl_path.read_text(encoding="utf-8", errors="replace")
        prompt_hash = f"sha256:{hashlib.sha256(content.encode('utf-8')).hexdigest()}"
        for line_number, line in enumerate(content.splitlines(), start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                self.initial_warnings.append(
                    f"Malformed agent enrichment JSONL line {line_number}: {exc.msg}; line ignored."
                )
                continue
            if not isinstance(record, dict):
                self.initial_warnings.append(
                    f"Agent enrichment JSONL line {line_number} is not an object; line ignored."
                )
                continue
            chunk_id = _clean_text_field(record.get("chunk_id"), max_chars=512)
            source_path = _clean_text_field(record.get("source_path"), max_chars=2000)
            if not chunk_id or not source_path:
                self.initial_warnings.append(
                    f"Agent enrichment JSONL line {line_number} is missing chunk_id or source_path; line ignored."
                )
                continue
            if chunk_id in self.records_by_chunk_id:
                self.initial_warnings.append(
                    f"Duplicate agent enrichment record for chunk_id {chunk_id}; later record ignored."
                )
                continue
            self.records_by_chunk_id[chunk_id] = self._sanitize_record(record, line_number)
        return prompt_hash

    def _sanitize_record(self, record: dict[str, Any], line_number: int) -> dict[str, Any]:
        sanitized = {
            "chunk_id": _clean_text_field(record.get("chunk_id"), max_chars=512),
            "source_path": _clean_text_field(record.get("source_path"), max_chars=2000),
        }
        for field, max_chars in (
            ("semantic_title", AGENT_SEMANTIC_TITLE_MAX_CHARS),
            ("retrieval_summary", AGENT_RETRIEVAL_SUMMARY_MAX_CHARS),
            ("agent_notes", AGENT_NOTE_MAX_CHARS),
        ):
            if field not in record:
                continue
            value = _clean_text_field(record.get(field), max_chars=max_chars)
            if value:
                sanitized[field] = value
            elif record.get(field) not in (None, ""):
                self.initial_warnings.append(
                    f"Agent enrichment JSONL line {line_number} has invalid {field}; field ignored."
                )
        if "concept_tags" in record:
            tags = _clean_concept_tags(record.get("concept_tags"))
            if tags:
                sanitized["concept_tags"] = tags
            elif record.get("concept_tags") not in (None, []):
                self.initial_warnings.append(
                    f"Agent enrichment JSONL line {line_number} has invalid concept_tags; field ignored."
                )
        if "depends_on_previous" in record:
            if isinstance(record.get("depends_on_previous"), bool):
                sanitized["depends_on_previous"] = record["depends_on_previous"]
            else:
                self.initial_warnings.append(
                    f"Agent enrichment JSONL line {line_number} has invalid depends_on_previous; field ignored."
                )
        return sanitized

    def enrich_chunks(self, chunks: list[Chunk]) -> tuple[dict[str, dict[str, Any]], list[str]]:
        enrichments: dict[str, dict[str, Any]] = {}
        warnings: list[str] = []
        for chunk in chunks:
            deterministic = enrich_chunk(chunk)
            record = self.records_by_chunk_id.get(chunk.chunk_id)
            if record is None:
                enrichments[chunk.chunk_id] = deterministic
                continue

            self.used_chunk_ids.add(chunk.chunk_id)
            record_source = _normalize_source_path(record.get("source_path"))
            chunk_source = _normalize_source_path(chunk.source_path)
            if record_source != chunk_source:
                warnings.append(
                    f"Agent enrichment source_path mismatch for chunk_id {chunk.chunk_id}; record ignored."
                )
                enrichments[chunk.chunk_id] = deterministic
                continue
            enrichments[chunk.chunk_id] = _merge_agent_record(deterministic, record)
        return enrichments, warnings

    def final_warnings(self) -> list[str]:
        warnings: list[str] = []
        for chunk_id in sorted(set(self.records_by_chunk_id) - self.used_chunk_ids):
            warnings.append(f"Agent enrichment record for unknown chunk_id ignored: {chunk_id}")
        return warnings

    def mark_chunks_seen(self, chunks: list[Chunk]) -> None:
        for chunk in chunks:
            if chunk.chunk_id in self.records_by_chunk_id:
                self.used_chunk_ids.add(chunk.chunk_id)

    def validate_cached_chunks(self, chunks: list[Chunk]) -> list[str]:
        warnings: list[str] = []
        for chunk in chunks:
            record = self.records_by_chunk_id.get(chunk.chunk_id)
            if record is None:
                continue
            record_source = _normalize_source_path(record.get("source_path"))
            chunk_source = _normalize_source_path(chunk.source_path)
            if record_source != chunk_source:
                warnings.append(
                    f"Agent enrichment source_path mismatch for chunk_id {chunk.chunk_id}; record ignored."
                )
                continue
            self.used_chunk_ids.add(chunk.chunk_id)
        return warnings


def build_enrichment_backend(
    backend: str = DETERMINISTIC_ENRICHMENT_BACKEND,
    *,
    agent_enrichment_jsonl: str | Path | None = None,
) -> MetadataEnrichmentBackend:
    """Build a metadata enrichment backend by name."""

    if backend == DETERMINISTIC_ENRICHMENT_BACKEND:
        return DeterministicEnrichmentBackend()
    if backend == AGENT_JSON_ENRICHMENT_BACKEND:
        return AgentJsonEnrichmentBackend(agent_enrichment_jsonl)
    raise ValueError(
        f"Unknown enrichment backend {backend!r}; expected "
        f"{DETERMINISTIC_ENRICHMENT_BACKEND!r} or {AGENT_JSON_ENRICHMENT_BACKEND!r}."
    )


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


def enrichment_batch_record(chunk: Chunk, max_content_chars: int = 4000) -> dict[str, Any]:
    """Return a JSON-serializable record for offline agent enrichment."""

    max_content_chars = max(3, int(max_content_chars))
    content = normalize_whitespace(chunk.content)
    if len(content) > max_content_chars:
        content = content[: max_content_chars - 3].rstrip() + "..."
    deterministic = enrich_chunk(chunk)
    return {
        "chunk_id": chunk.chunk_id,
        "source_path": chunk.source_path,
        "title": chunk.title,
        "chunk_type": chunk.chunk_type,
        "section_path": list(chunk.section_path),
        "line_start": chunk.line_start,
        "line_end": chunk.line_end,
        "semantic_title": deterministic["semantic_title"],
        "retrieval_summary": deterministic["retrieval_summary"],
        "concept_tags": deterministic["concept_tags"],
        "content": content,
    }


def _merge_agent_record(deterministic: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    enrichment = dict(deterministic)
    semantic_title = _clean_text_field(record.get("semantic_title"), max_chars=AGENT_SEMANTIC_TITLE_MAX_CHARS)
    if semantic_title:
        enrichment["semantic_title"] = semantic_title
    retrieval_summary = _clean_text_field(
        record.get("retrieval_summary"),
        max_chars=AGENT_RETRIEVAL_SUMMARY_MAX_CHARS,
    )
    if retrieval_summary:
        enrichment["retrieval_summary"] = retrieval_summary
    if isinstance(record.get("depends_on_previous"), bool):
        enrichment["depends_on_previous"] = record["depends_on_previous"]

    agent_tags = _clean_concept_tags(record.get("concept_tags"))
    if agent_tags:
        enrichment["concept_tags"] = _dedupe([*enrichment.get("concept_tags", []), *agent_tags])

    agent_notes = _clean_text_field(record.get("agent_notes"), max_chars=AGENT_NOTE_MAX_CHARS)
    if agent_notes:
        enrichment["agent_notes"] = agent_notes
    return enrichment


def _clean_concept_tags(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    tags: list[str] = []
    for item in value:
        tag = _clean_text_field(item, max_chars=AGENT_TAG_MAX_CHARS)
        if tag:
            tags.append(tag)
        if len(tags) >= AGENT_TAG_MAX_COUNT:
            break
    return _dedupe(tags)


def _clean_text_field(value: object, *, max_chars: int) -> str:
    if not isinstance(value, str):
        return ""
    return normalize_whitespace(value)[:max_chars].strip()


def _normalize_source_path(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return Path(value).as_posix()


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    deduped: list[str] = []
    for value in values:
        if value not in seen:
            deduped.append(value)
            seen.add(value)
    return deduped
