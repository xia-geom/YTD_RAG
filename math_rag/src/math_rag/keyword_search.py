"""Keyword/BM25 retrieval for exact mathematical names and symbols."""

from __future__ import annotations

import math
from collections import Counter

from .models import Chunk, SearchResult
from .text_cleaning import salient_terms, tokenize


class KeywordSearch:
    def __init__(self, chunks: list[Chunk]):
        self.chunks = chunks
        self.tokenized = [tokenize(chunk.content) for chunk in chunks]
        self.doc_lengths = [len(tokens) for tokens in self.tokenized]
        self.avgdl = sum(self.doc_lengths) / len(self.doc_lengths) if self.doc_lengths else 0.0
        self.term_frequencies = [Counter(tokens) for tokens in self.tokenized]
        self.doc_frequency: Counter[str] = Counter()
        for tokens in self.tokenized:
            self.doc_frequency.update(set(tokens))

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        if not self.chunks:
            return []
        query_tokens = tokenize(query)
        query_terms = salient_terms(query)
        scores: list[tuple[int, float]] = []
        for idx, chunk in enumerate(self.chunks):
            score = self._bm25_score(idx, query_tokens)
            score += self._exact_boost(chunk, query, query_terms)
            if score > 0:
                scores.append((idx, score))
        scores.sort(key=lambda item: item[1], reverse=True)
        results: list[SearchResult] = []
        for rank, (idx, score) in enumerate(scores[:top_k], start=1):
            results.append(SearchResult(chunk=self.chunks[idx], score=score, keyword_score=score, rank=rank))
        return results

    def _bm25_score(self, doc_index: int, query_tokens: list[str]) -> float:
        if not query_tokens or not self.avgdl:
            return 0.0
        score = 0.0
        k1 = 1.5
        b = 0.75
        freqs = self.term_frequencies[doc_index]
        dl = self.doc_lengths[doc_index]
        total_docs = len(self.chunks)
        for token in query_tokens:
            tf = freqs.get(token, 0)
            if tf == 0:
                continue
            df = self.doc_frequency.get(token, 0)
            idf = math.log(1 + (total_docs - df + 0.5) / (df + 0.5))
            denom = tf + k1 * (1 - b + b * dl / self.avgdl)
            score += idf * (tf * (k1 + 1)) / denom
        return score

    @staticmethod
    def _exact_boost(chunk: Chunk, query: str, query_terms: list[str]) -> float:
        lower_content = chunk.content.lower()
        lower_query = query.lower().strip()
        boost = 0.0
        if lower_query and lower_query in lower_content:
            boost += 3.0
        for term in query_terms:
            if term.lower() in lower_content:
                boost += 0.35
        for symbol in chunk.symbols:
            if symbol.lower() in lower_query:
                boost += 0.8
        return boost

