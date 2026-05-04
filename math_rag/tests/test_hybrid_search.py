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


def test_hybrid_search_demotes_citation_context_below_real_text():
    chunks = [
        Chunk(
            chunk_id="bib",
            source_path="paperA/source/biblio.bib",
            chunk_type="citation_context",
            content=(
                "@article{chen-cheng-1, author = {Chen, X. and Cheng, J.}, "
                "title = {Chen-Cheng a priori estimates for cscK metrics}}"
            ),
        ),
        Chunk(
            chunk_id="real",
            source_path="paperB/source/source.tex",
            chunk_type="theorem",
            content=(
                "Theorem (Chen-Cheng). The Mabuchi energy is proper. "
                "We give a priori estimates for cscK metrics."
            ),
        ),
    ]

    results = HybridSearch(chunks).search("Chen-Cheng cscK estimates", top_k=2)

    assert results[0].chunk.chunk_id == "real", (
        f"expected real .tex theorem to outrank biblio.bib, got top={results[0].chunk.chunk_id}"
    )


def test_hybrid_search_matches_unaccented_query_to_accented_content():
    chunks = [
        Chunk(
            chunk_id="accented",
            source_path="notes.tex",
            chunk_type="text",
            content="The Poincaré type Kähler metric appears in the cusp model.",
        ),
        Chunk(
            chunk_id="other",
            source_path="other.tex",
            chunk_type="text",
            content="A generic paragraph about algebraic geometry.",
        ),
    ]

    results = HybridSearch(chunks).search("Poincare Kahler cusp", top_k=2)

    assert results[0].chunk.chunk_id == "accented"
    assert results[0].keyword_score > 0


def test_hybrid_search_demotion_can_be_disabled():
    chunks = [
        Chunk(chunk_id="bib", source_path="a.bib", chunk_type="citation_context", content="Chen-Cheng cscK"),
        Chunk(chunk_id="text", source_path="b.tex", chunk_type="text", content="Chen-Cheng cscK"),
    ]
    results = HybridSearch(chunks, citation_context_demotion=1.0).search("Chen-Cheng cscK", top_k=2)
    assert {r.chunk.chunk_id for r in results} == {"bib", "text"}


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
