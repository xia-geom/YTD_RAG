"""Shared service layer for the local math_rag RAG system.

The CLI and the MCP server both call into this module so that retrieval logic,
the conservative answer discipline, and source/chunk lookups are defined in one
place rather than duplicated.

Every function in this module returns plain JSON-serialisable dictionaries.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

from .answer import LOW_CONFIDENCE_THRESHOLD, retrieval_confidence
from .citations import format_citation, format_location, format_section_path, unique_sources
from .config import DEFAULT_INDEX_DIR, load_settings
from .hybrid_search import search_chunks
from .index_store import IndexStore
from .loaders import load_corpus
from .metadata_enrichment_cache import ENRICHMENT_CACHE_DIRNAME
from .models import Chunk, SearchResult
from .symbol_normalization import normalize_search_text
from .text_cleaning import make_snippet, salient_terms


MAX_SNIPPET_CHARS = 360
MAX_CHUNK_CONTENT_CHARS = 8000
MAX_RESULTS_PER_CALL = 50
MAX_SOURCES_PER_CALL = 500


class IndexNotFoundError(RuntimeError):
    """Raised when the local RAG index is missing or empty."""


def _load_chunks(index_dir: str) -> list[Chunk]:
    store = IndexStore(index_dir)
    chunks = store.load_chunks()
    if not chunks:
        raise IndexNotFoundError(
            f"No index found or index is empty at {store.index_path}. "
            "Run: python -m math_rag.cli ingest corpus/"
        )
    return chunks


def _truncate(text: str, max_chars: int) -> tuple[str, bool]:
    if text is None:
        return "", False
    if len(text) <= max_chars:
        return text, False
    return text[: max_chars - 3].rstrip() + "...", True


def _filter_by_source(chunks: Iterable[Chunk], source_filter: list[str] | None) -> list[Chunk]:
    if not source_filter:
        return list(chunks)
    needles = [s for s in (n.strip() for n in source_filter) if s]
    if not needles:
        return list(chunks)
    matched: list[Chunk] = []
    for chunk in chunks:
        path = chunk.source_path
        if any(needle in path for needle in needles):
            matched.append(chunk)
    return matched


def _result_to_dict(result: SearchResult, query: str) -> dict[str, Any]:
    chunk = result.chunk
    snippet, _ = _truncate(make_snippet(chunk.content, query, max_chars=MAX_SNIPPET_CHARS), MAX_SNIPPET_CHARS)
    return {
        "chunk_id": chunk.chunk_id,
        "source_path": chunk.source_path,
        "title": chunk.title,
        "chunk_type": chunk.chunk_type,
        "section_path": list(chunk.section_path or []),
        "page_number": chunk.page_number,
        "line_start": chunk.line_start,
        "line_end": chunk.line_end,
        "score": float(result.score),
        "keyword_score": float(result.keyword_score),
        "vector_score": float(result.vector_score),
        "rank": result.rank,
        "snippet": snippet,
        "citation": format_citation(chunk),
    }


def _matched_terms(question: str, result: SearchResult) -> list[str]:
    content = normalize_search_text(result.chunk.content)
    return [term for term in salient_terms(question) if normalize_search_text(term) in content]


def retrieve(
    query: str,
    *,
    top_k: int = 8,
    mode: str = "hybrid",
    index_dir: str = DEFAULT_INDEX_DIR,
    source_filter: list[str] | None = None,
) -> list[SearchResult]:
    """Run retrieval against the local index and return raw SearchResult objects.

    The CLI uses this for line-by-line console output; the MCP server uses
    :func:`search_corpus` and :func:`ask_corpus`, which both delegate here.
    """

    settings = load_settings(index_dir)
    chunks = _load_chunks(index_dir)
    chunks = _filter_by_source(chunks, source_filter)
    if not chunks:
        return []
    return search_chunks(
        chunks, query, mode=mode, top_k=top_k, vector_backend=settings.embedding_backend
    )


def search_corpus(
    query: str,
    top_k: int = 8,
    source_filter: list[str] | None = None,
    *,
    index_dir: str = DEFAULT_INDEX_DIR,
    mode: str = "hybrid",
) -> dict[str, Any]:
    """Run hybrid retrieval over the local index and return JSON-friendly results."""

    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    top_k = max(1, min(int(top_k), MAX_RESULTS_PER_CALL))
    raw_results = retrieve(
        query,
        top_k=top_k,
        mode=mode,
        index_dir=index_dir,
        source_filter=source_filter,
    )
    results = [_result_to_dict(r, query) for r in raw_results]
    return {
        "query": query,
        "top_k": top_k,
        "mode": mode,
        "source_filter": source_filter or [],
        "results": results,
        "truncated": len(raw_results) >= top_k,
    }


def ask_corpus(
    question: str,
    top_k: int = 8,
    strict: bool = True,
    *,
    index_dir: str = DEFAULT_INDEX_DIR,
    mode: str = "hybrid",
    source_filter: list[str] | None = None,
) -> dict[str, Any]:
    """Return a structured retrieval-grounded answer that mirrors build_answer.

    The output preserves the same conservative discipline used by the CLI's
    ``ask`` command: evidence, inference, and not-established are kept
    separate, and the corpus is never claimed to verify any proof.
    """

    if not isinstance(question, str) or not question.strip():
        raise ValueError("question must be a non-empty string")
    top_k = max(1, min(int(top_k), MAX_RESULTS_PER_CALL))
    raw_results = retrieve(
        question,
        top_k=top_k,
        mode=mode,
        index_dir=index_dir,
        source_filter=source_filter,
    )
    confidence = retrieval_confidence(question, raw_results)

    retrieved_evidence = [_result_to_dict(r, question) for r in raw_results]

    if confidence == "low" or not raw_results:
        short_answer = (
            "I do not find enough evidence in the retrieved corpus to answer this reliably. "
            "This is a retrieval failure, not a mathematical conclusion."
        )
        what_supports = ["Nothing specific is established by the retrieved passages."]
        reasonable_inference = ["No reliable inference should be drawn from this retrieval result."]
        not_established = [
            "The corpus search did not establish the requested statement, proof, comparison, or novelty claim.",
            "This requires human verification and likely broader search terms or more documents.",
        ]
    else:
        short_answer = (
            "The corpus contains retrieved passages that appear relevant to the question. "
            "The structured fields below are based only on those passages and do not verify any proof or theorem."
        )
        what_supports = []
        for result in raw_results:
            terms = _matched_terms(question, result)
            citation = format_citation(result.chunk)
            if terms:
                what_supports.append(
                    f"The source contains retrieved text overlapping the query terms "
                    f"{', '.join(terms[:6])} {citation}."
                )
            else:
                what_supports.append(
                    f"The source was retrieved as relevant by the local index {citation}."
                )
        best = raw_results[0]
        reasonable_inference = [
            (
                f"A cautious next step is to inspect {best.chunk.source_path} around "
                f"{format_location(best.chunk)}; it is the strongest retrieved match, "
                f"not a verified mathematical conclusion {format_citation(best.chunk)}."
            )
        ]
        not_established = [
            "The retrieved passages do not establish correctness of any proof.",
            (
                "They do not establish novelty, completeness of hypotheses, or equivalence of theorem "
                "statements unless those points are explicitly present in the cited text."
            ),
            "This requires human verification in the surrounding source context.",
        ]

    sources_inspected = unique_sources(raw_results)

    payload: dict[str, Any] = {
        "question": question,
        "short_answer": short_answer,
        "retrieval_confidence": confidence,
        "strict": bool(strict),
        "top_k": top_k,
        "retrieved_evidence": retrieved_evidence,
        "what_corpus_supports": what_supports,
        "reasonable_inference": reasonable_inference,
        "not_established_by_retrieved_sources": not_established,
        "sources_inspected": sources_inspected,
        "low_confidence_threshold": LOW_CONFIDENCE_THRESHOLD,
        "warning": (
            "math_rag never verifies a proof. All claims must be checked in the cited source."
        ),
    }
    return payload


def get_chunk(chunk_id: str, *, index_dir: str = DEFAULT_INDEX_DIR) -> dict[str, Any]:
    """Return the full content and metadata for a single indexed chunk."""

    if not isinstance(chunk_id, str) or not chunk_id.strip():
        raise ValueError("chunk_id must be a non-empty string")
    chunks = _load_chunks(index_dir)
    for chunk in chunks:
        if chunk.chunk_id == chunk_id:
            content, content_truncated = _truncate(chunk.content or "", MAX_CHUNK_CONTENT_CHARS)
            return {
                "chunk_id": chunk.chunk_id,
                "source_path": chunk.source_path,
                "title": chunk.title,
                "chunk_type": chunk.chunk_type,
                "section_path": list(chunk.section_path or []),
                "section_path_string": format_section_path(chunk),
                "page_number": chunk.page_number,
                "line_start": chunk.line_start,
                "line_end": chunk.line_end,
                "content": content,
                "content_truncated": content_truncated,
                "metadata": dict(chunk.metadata or {}),
                "symbols": list(chunk.symbols or []),
                "topics": list(chunk.topics or []),
                "citation": format_citation(chunk),
            }
    raise KeyError(f"chunk_id {chunk_id!r} not found in index")


def list_sources(
    source_filter: list[str] | None = None,
    *,
    index_dir: str = DEFAULT_INDEX_DIR,
) -> dict[str, Any]:
    """Return a summary of indexed sources."""

    chunks = _load_chunks(index_dir)
    chunks = _filter_by_source(chunks, source_filter)
    grouped: dict[str, dict[str, Any]] = {}
    for chunk in chunks:
        entry = grouped.setdefault(
            chunk.source_path,
            {
                "source_path": chunk.source_path,
                "title": chunk.title,
                "chunk_count": 0,
                "chunk_types": {},
            },
        )
        entry["chunk_count"] += 1
        types = entry["chunk_types"]
        types[chunk.chunk_type] = types.get(chunk.chunk_type, 0) + 1
        if not entry.get("title") and chunk.title:
            entry["title"] = chunk.title
    sources = sorted(grouped.values(), key=lambda item: item["source_path"])
    truncated = False
    if len(sources) > MAX_SOURCES_PER_CALL:
        sources = sources[:MAX_SOURCES_PER_CALL]
        truncated = True
    return {
        "sources": sources,
        "number_of_sources": len(grouped),
        "number_of_chunks": sum(entry["chunk_count"] for entry in grouped.values()),
        "source_filter": source_filter or [],
        "truncated": truncated,
    }


def ingest_path(
    path: str = "corpus/",
    *,
    index_dir: str = DEFAULT_INDEX_DIR,
    metadata: str | None = None,
    enrich_metadata: bool = False,
    refresh_enrichment_cache: bool = False,
) -> dict[str, Any]:
    """Re-ingest a corpus path into the local index."""

    corpus_path = Path(path)
    enrichment_cache_dir = Path(index_dir) / ENRICHMENT_CACHE_DIRNAME
    chunks, warnings = load_corpus(
        corpus_path,
        metadata,
        enrich_metadata=enrich_metadata,
        enrichment_cache_dir=enrichment_cache_dir,
        refresh_enrichment_cache=refresh_enrichment_cache,
    )
    store = IndexStore(index_dir)
    store.save_chunks(chunks)
    return {
        "corpus_path": str(corpus_path),
        "index_path": str(store.index_path),
        "chunk_count": len(chunks),
        "warnings": list(warnings),
    }


def index_stats(*, index_dir: str = DEFAULT_INDEX_DIR) -> dict[str, Any]:
    """Return summary statistics for the local index, without raising on empty."""

    return IndexStore(index_dir).stats()
