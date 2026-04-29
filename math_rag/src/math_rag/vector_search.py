"""Local vector-style retrieval.

The default backend is a deterministic sparse cosine retriever. It is not a
domain embedding model, but it keeps the first version local and install-free.
The class boundary is intentionally narrow so sentence-transformers or another
embedding backend can be added later without changing the answer layer.
"""

from __future__ import annotations

import math
from collections import Counter

from .models import Chunk, SearchResult
from .text_cleaning import salient_terms, tokenize


DOMAIN_EXPANSIONS = {
    "cscK": ["constant", "scalar", "curvature", "kahler", "kähler"],
    "poincare": ["poincare", "poincaré", "cusp"],
    "poincaré": ["poincare", "poincaré", "cusp"],
    "cone": ["conic", "angle", "beta"],
    "conic": ["cone", "angle", "beta"],
    "k-energy": ["mabuchi", "energy"],
    "mabuchi": ["k-energy", "functional"],
    "toric": ["polytope", "moment", "symplectic"],
    "weighted": ["lahdili", "extremal"],
}


class VectorSearch:
    def __init__(self, chunks: list[Chunk], backend: str = "local"):
        self.chunks = chunks
        self.backend = backend
        self.vectors = [self._vectorize(chunk.content) for chunk in chunks]
        self.norms = [self._norm(vector) for vector in self.vectors]

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        if not self.chunks:
            return []
        query_vector = self._vectorize(query)
        query_norm = self._norm(query_vector)
        if query_norm == 0:
            return []
        scored: list[tuple[int, float]] = []
        for idx, vector in enumerate(self.vectors):
            denom = query_norm * self.norms[idx]
            if denom == 0:
                continue
            score = self._dot(query_vector, vector) / denom
            if score > 0:
                scored.append((idx, score))
        scored.sort(key=lambda item: item[1], reverse=True)
        results: list[SearchResult] = []
        for rank, (idx, score) in enumerate(scored[:top_k], start=1):
            results.append(SearchResult(chunk=self.chunks[idx], score=score, vector_score=score, rank=rank))
        return results

    @classmethod
    def _vectorize(cls, text: str) -> Counter[str]:
        tokens = salient_terms(text) or tokenize(text)
        expanded: list[str] = []
        for token in tokens:
            expanded.append(token)
            expanded.extend(DOMAIN_EXPANSIONS.get(token, []))
        return Counter(expanded)

    @staticmethod
    def _dot(left: Counter[str], right: Counter[str]) -> float:
        if len(left) > len(right):
            left, right = right, left
        return float(sum(value * right.get(token, 0) for token, value in left.items()))

    @staticmethod
    def _norm(vector: Counter[str]) -> float:
        return math.sqrt(sum(value * value for value in vector.values()))

