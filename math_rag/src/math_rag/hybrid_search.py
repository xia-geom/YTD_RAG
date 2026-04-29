"""Hybrid retrieval that keeps exact keyword hits first-class."""

from __future__ import annotations

from .keyword_search import KeywordSearch
from .models import Chunk, SearchResult
from .vector_search import VectorSearch


class HybridSearch:
    def __init__(
        self,
        chunks: list[Chunk],
        keyword_search: KeywordSearch | None = None,
        vector_search: VectorSearch | None = None,
    ):
        self.chunks = chunks
        self.keyword_search = keyword_search or KeywordSearch(chunks)
        self.vector_search = vector_search or VectorSearch(chunks)

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

        ranked = sorted(merged.values(), key=lambda result: (result.score, result.keyword_score), reverse=True)
        for rank, result in enumerate(ranked[:top_k], start=1):
            result.rank = rank
        return ranked[:top_k]


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
