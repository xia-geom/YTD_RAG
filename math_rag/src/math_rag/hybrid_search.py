"""Hybrid retrieval that keeps exact keyword hits first-class."""

from __future__ import annotations

import re

from .keyword_search import KeywordSearch
from .models import Chunk, SearchResult
from .symbol_normalization import normalize_search_text
from .vector_search import VectorSearch


CITATION_CONTEXT_DEMOTION = 0.4
NAVIGATION_NOTE_DEMOTION = 0.35
ENGINEERING_MEMORY_DEMOTION = 0.6
BIBLIOGRAPHY_POINTER_DEMOTION = 0.75
PRIMARY_PAPER_BOOST = 1.05
PROJECT_NOTE_QUERY_BOOST = 1.2
SOURCE_DIVERSITY_MIN_RATIO = 0.8

NAVIGATION_QUERY_PATTERNS = (
    re.compile(r"\b(?:which|what)\s+papers\b"),
    re.compile(r"\b(?:which|what)\s+sources\b"),
    re.compile(r"\bpaper\s+list\b"),
    re.compile(r"\bsource\s+list\b"),
    re.compile(r"\bbibliograph(?:y|ic)\b"),
    re.compile(r"\breading\s+map\b"),
    re.compile(r"\bproject\s+paper\s+index\b"),
    re.compile(r"\bexact\s+papers\b"),
    re.compile(r"\brecord(?:s|ed)?\s+the\s+requested\b"),
)
PROJECT_NOTE_QUERY_PATTERNS = (
    re.compile(r"\bmy\s+notes\b"),
    re.compile(r"\btable\b"),
    re.compile(r"\bdictionary\b"),
    re.compile(r"\bcp\s*(?:\^\s*\{?\s*)?1\}?\b"),
    re.compile(r"\bmoment\s+polytope\b"),
    re.compile(r"\bmoment\s+interval\b"),
    re.compile(r"\bpolytope\s*\[\s*-?1\s*,\s*1\s*\]"),
    re.compile(r"\bnotation\b"),
)
ARXIV_SOURCE_RE = re.compile(r"(?:^|/)corpus/arxiv/([^/]+)(?:/|$)")


class HybridSearch:
    def __init__(
        self,
        chunks: list[Chunk],
        keyword_search: KeywordSearch | None = None,
        vector_search: VectorSearch | None = None,
        citation_context_demotion: float = CITATION_CONTEXT_DEMOTION,
    ):
        self.chunks = chunks
        self.keyword_search = keyword_search or KeywordSearch(chunks)
        self.vector_search = vector_search or VectorSearch(chunks)
        self.citation_context_demotion = citation_context_demotion

    def search(
        self,
        query: str,
        top_k: int = 10,
        keyword_weight: float = 0.7,
        vector_weight: float = 0.3,
    ) -> list[SearchResult]:
        if not self.chunks:
            return []
        keyword_results = self.keyword_search.search(query, top_k=max(top_k * 4, 20))
        vector_results = self.vector_search.search(query, top_k=max(top_k * 4, 20))
        if not keyword_results and not vector_results:
            return []

        max_keyword = max((result.keyword_score or result.score for result in keyword_results), default=1.0) or 1.0
        max_vector = max((result.vector_score or result.score for result in vector_results), default=1.0) or 1.0

        merged: dict[str, SearchResult] = {}
        order: dict[str, int] = {}

        for position, result in enumerate(keyword_results, start=1):
            chunk_id = result.chunk.chunk_id
            normalized = (result.keyword_score or result.score) / max_keyword
            score = keyword_weight * normalized + 1.0 / (60 + position)
            merged[chunk_id] = SearchResult(
                chunk=result.chunk,
                score=score,
                keyword_score=result.keyword_score or result.score,
                vector_score=0.0,
            )
            order.setdefault(chunk_id, position)

        for position, result in enumerate(vector_results, start=1):
            chunk_id = result.chunk.chunk_id
            normalized = (result.vector_score or result.score) / max_vector
            score = vector_weight * normalized + 1.0 / (60 + position)
            if chunk_id in merged:
                existing = merged[chunk_id]
                existing.score += score
                existing.vector_score = result.vector_score or result.score
            else:
                merged[chunk_id] = SearchResult(
                    chunk=result.chunk,
                    score=score,
                    keyword_score=0.0,
                    vector_score=result.vector_score or result.score,
                )
                order.setdefault(chunk_id, 1000 + position)

        if self.citation_context_demotion < 1.0:
            for result in merged.values():
                if result.chunk.chunk_type == "citation_context":
                    result.score *= self.citation_context_demotion

        self._apply_source_role_weights(merged.values(), query)
        ranked = sorted(merged.values(), key=lambda result: (result.score, result.keyword_score), reverse=True)
        ranked = _diversify_by_source(ranked, top_k)
        for rank, result in enumerate(ranked, start=1):
            result.rank = rank
        return ranked

    @staticmethod
    def _apply_source_role_weights(results, query: str) -> None:
        navigation_query = _is_navigation_query(query)
        project_note_query = _is_project_note_query(query)
        for result in results:
            multiplier = _source_role_multiplier(result.chunk, navigation_query, project_note_query)
            result.score *= multiplier


def search_chunks(
    chunks: list[Chunk],
    query: str,
    mode: str = "hybrid",
    top_k: int = 10,
    vector_backend: str = "local",
) -> list[SearchResult]:
    mode = mode.lower()
    if mode == "keyword":
        return KeywordSearch(chunks).search(query, top_k=top_k)
    if mode == "vector":
        return VectorSearch(chunks, backend=vector_backend).search(query, top_k=top_k)
    if mode == "hybrid":
        return HybridSearch(chunks, vector_search=VectorSearch(chunks, backend=vector_backend)).search(query, top_k=top_k)
    raise ValueError(f"Unknown search mode {mode!r}; expected keyword, vector, or hybrid.")


def _diversify_by_source(
    ranked: list[SearchResult],
    top_k: int,
    min_score_ratio: float = SOURCE_DIVERSITY_MIN_RATIO,
) -> list[SearchResult]:
    """Prefer source diversity when the alternative is competitively scored."""

    if top_k <= 0:
        return []
    remaining = list(ranked)
    selected: list[SearchResult] = []
    seen_sources: set[str] = set()

    while remaining and len(selected) < top_k:
        candidate = remaining.pop(0)
        candidate_source = _source_key(candidate.chunk)
        if candidate_source not in seen_sources:
            selected.append(candidate)
            seen_sources.add(candidate_source)
            continue

        alternative_index = _find_diverse_alternative(
            remaining,
            seen_sources,
            minimum_score=candidate.score * min_score_ratio,
        )
        if alternative_index is None:
            selected.append(candidate)
            continue

        alternative = remaining.pop(alternative_index)
        selected.append(alternative)
        seen_sources.add(_source_key(alternative.chunk))
        remaining.insert(0, candidate)
    return selected


def _find_diverse_alternative(
    ranked: list[SearchResult],
    seen_sources: set[str],
    minimum_score: float,
) -> int | None:
    for index, result in enumerate(ranked):
        if result.score < minimum_score:
            return None
        if _source_key(result.chunk) not in seen_sources:
            return index
    return None


def _source_role_multiplier(chunk: Chunk, navigation_query: bool, project_note_query: bool) -> float:
    role = _source_role(chunk)
    if role == "navigation_note":
        return 1.0 if navigation_query else NAVIGATION_NOTE_DEMOTION
    if role == "bibliography_pointer":
        return 1.0 if navigation_query else BIBLIOGRAPHY_POINTER_DEMOTION
    if role == "engineering_memory":
        return ENGINEERING_MEMORY_DEMOTION
    if role == "primary_paper":
        return PRIMARY_PAPER_BOOST
    if role == "project_note" and project_note_query:
        return PROJECT_NOTE_QUERY_BOOST
    return 1.0


def _source_role(chunk: Chunk) -> str | None:
    metadata = chunk.metadata if isinstance(chunk.metadata, dict) else {}
    enrichment = metadata.get("enrichment")
    if isinstance(enrichment, dict):
        role = enrichment.get("source_role")
        if isinstance(role, str) and role:
            return role
        if enrichment.get("is_navigation_note") is True:
            return "navigation_note"

    source_path = chunk.source_path.replace("\\", "/")
    if "agent_logs/" in source_path:
        return "engineering_memory"
    if source_path.endswith("corpus/my_notes/project_paper_index.md") or source_path == "corpus/my_notes/project_paper_index.md":
        return "navigation_note"
    if source_path.endswith("corpus/my_notes/requested_non_arxiv_sources.md") or source_path == (
        "corpus/my_notes/requested_non_arxiv_sources.md"
    ):
        return "bibliography_pointer"
    if "corpus/arxiv/" in source_path:
        return "primary_paper"
    if "corpus/my_notes/" in source_path:
        return "project_note"
    return None


def _source_key(chunk: Chunk) -> str:
    source_path = chunk.source_path.replace("\\", "/")
    match = ARXIV_SOURCE_RE.search(source_path)
    if match:
        return f"arxiv:{match.group(1)}"
    return source_path


def _is_navigation_query(query: str) -> bool:
    normalized = normalize_search_text(query)
    return any(pattern.search(normalized) for pattern in NAVIGATION_QUERY_PATTERNS)


def _is_project_note_query(query: str) -> bool:
    normalized = normalize_search_text(query)
    return any(pattern.search(normalized) for pattern in PROJECT_NOTE_QUERY_PATTERNS)
