from math_rag.answer import build_answer
from math_rag.hybrid_search import HybridSearch, search_chunks
from math_rag.models import Chunk, SearchResult


class WeakVectorSearch:
    def __init__(self, chunks):
        self.chunks = chunks

    def search(self, query, top_k=10):
        unrelated = self.chunks[1]
        exact = self.chunks[0]
        return [
            SearchResult(chunk=unrelated, score=1.0, vector_score=1.0, rank=1),
            SearchResult(chunk=exact, score=0.01, vector_score=0.01, rank=2),
        ][:top_k]


def test_hybrid_search_keeps_exact_keyword_hits_above_weak_vector_similarity():
    chunks = [
        Chunk(
            chunk_id="exact",
            source_path="notes.tex",
            chunk_type="text",
            content="These notes discuss Chen-Cheng estimates for cscK metrics.",
        ),
        Chunk(
            chunk_id="semantic",
            source_path="other.tex",
            chunk_type="text",
            content="A generic discussion of geometric analysis and estimates.",
        ),
    ]

    results = HybridSearch(chunks, vector_search=WeakVectorSearch(chunks)).search("Chen-Cheng", top_k=2)

    assert results[0].chunk.chunk_id == "exact"
    assert results[0].keyword_score > 0


def test_empty_or_weak_retrieval_does_not_hallucinate_answer():
    answer = build_answer("Prove the missing theorem about cusp limits.", [])

    assert "do not find enough evidence" in answer
    assert "not a mathematical conclusion" in answer
    assert "No chunks were retrieved" in answer
    assert "Not established by retrieved sources" in answer


def test_weak_non_empty_retrieval_is_reported_as_not_established():
    weak_chunk = Chunk(
        chunk_id="weak",
        source_path="generic.tex",
        chunk_type="text",
        content="This theorem is included as a generic placeholder with no cusp or conic content.",
        line_start=3,
        line_end=4,
    )
    weak_result = SearchResult(chunk=weak_chunk, score=0.9, keyword_score=0.9, rank=1)

    answer = build_answer("Prove the missing theorem about weighted Mabuchi energy.", [weak_result])

    assert "do not find enough evidence" in answer
    assert "Nothing specific is established" in answer
    assert "generic.tex" in answer


def test_empty_corpus_search_returns_empty_results():
    assert HybridSearch([]).search("Chen-Cheng") == []
    assert search_chunks([], "Chen-Cheng", mode="hybrid") == []


def test_answer_output_carries_page_and_line_citations():
    chunk = Chunk(
        chunk_id="cited",
        source_path="notes.tex",
        chunk_type="text",
        section_path=["Weighted energy"],
        page_number=12,
        line_start=20,
        line_end=25,
        content="The weighted Mabuchi energy is discussed in these notes.",
    )
    result = SearchResult(chunk=chunk, score=1.0, keyword_score=1.0, rank=1)

    answer = build_answer("What does the corpus say about weighted Mabuchi energy?", [result])

    assert "[notes.tex, Weighted energy, p. 12, lines 20-25]" in answer
