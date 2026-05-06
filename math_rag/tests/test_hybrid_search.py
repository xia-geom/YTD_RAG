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


class FixedSearch:
    def __init__(self, results):
        self.results = results

    def search(self, query, top_k=10):
        return self.results[:top_k]


def _result(chunk, score):
    return SearchResult(chunk=chunk, score=score, keyword_score=score)


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


def test_hybrid_search_demotes_navigation_notes_for_mathematical_queries():
    navigation_note = Chunk(
        chunk_id="paper-index",
        source_path="corpus/my_notes/project_paper_index.md",
        chunk_type="text",
        content="Hisamoto discusses toric coercivity and uniform K-stability.",
    )
    primary_paper = Chunk(
        chunk_id="primary-paper",
        source_path="corpus/arxiv/1610.07998/source/source.tex",
        chunk_type="theorem",
        content="The toric coercivity theorem relates uniform K-stability to K-energy properness.",
    )
    keyword = FixedSearch([_result(navigation_note, 1.0), _result(primary_paper, 0.8)])

    results = HybridSearch(
        [navigation_note, primary_paper],
        keyword_search=keyword,
        vector_search=FixedSearch([]),
    ).search("Where does the corpus discuss toric coercivity?", top_k=2)

    assert results[0].chunk.chunk_id == "primary-paper"


def test_hybrid_search_allows_navigation_notes_for_paper_list_queries():
    navigation_note = Chunk(
        chunk_id="paper-index",
        source_path="corpus/my_notes/project_paper_index.md",
        chunk_type="text",
        content="Hisamoto discusses toric coercivity and uniform K-stability.",
    )
    primary_paper = Chunk(
        chunk_id="primary-paper",
        source_path="corpus/arxiv/1610.07998/source/source.tex",
        chunk_type="theorem",
        content="The toric coercivity theorem relates uniform K-stability to K-energy properness.",
    )
    keyword = FixedSearch([_result(navigation_note, 1.0), _result(primary_paper, 0.8)])

    results = HybridSearch(
        [navigation_note, primary_paper],
        keyword_search=keyword,
        vector_search=FixedSearch([]),
    ).search("Which papers discuss toric coercivity?", top_k=2)

    assert results[0].chunk.chunk_id == "paper-index"


def test_hybrid_search_boosts_project_notes_for_notes_queries():
    primary_paper = Chunk(
        chunk_id="primary-paper",
        source_path="corpus/arxiv/2208.12493/source/source.tex",
        chunk_type="text",
        content="Toric Kahler geometry uses moment polytopes and symplectic potentials.",
    )
    project_note = Chunk(
        chunk_id="project-note",
        source_path="corpus/my_notes/toric_manifolds_mixed_conic_cusp/tables/kenergy_table.tex",
        chunk_type="text",
        content="A dictionary between Kahler geometry and toric moment-polytope expressions.",
    )
    keyword = FixedSearch([_result(primary_paper, 1.0), _result(project_note, 0.9)])

    results = HybridSearch(
        [primary_paper, project_note],
        keyword_search=keyword,
        vector_search=FixedSearch([]),
    ).search("Where do my notes give a dictionary for toric geometry?", top_k=2)

    assert results[0].chunk.chunk_id == "project-note"


def test_hybrid_search_demotes_engineering_memory_for_math_queries():
    engineering_log = Chunk(
        chunk_id="agent-log",
        source_path="agent_logs/codex/2026-05-06-retrieval-precision-audit.md",
        chunk_type="text",
        content="The eval report mentions Mabuchi energy retrieval.",
    )
    primary_paper = Chunk(
        chunk_id="primary-paper",
        source_path="corpus/arxiv/1510.01260/source/source.tex",
        chunk_type="text",
        content="The extended K-energy is convex on finite energy spaces.",
    )
    keyword = FixedSearch([_result(engineering_log, 1.0), _result(primary_paper, 0.8)])

    results = HybridSearch(
        [engineering_log, primary_paper],
        keyword_search=keyword,
        vector_search=FixedSearch([]),
    ).search("Where does the corpus discuss extended K-energy convexity?", top_k=2)

    assert results[0].chunk.chunk_id == "primary-paper"


def test_source_diversity_prefers_competitive_new_sources():
    source_a_first = Chunk(chunk_id="a1", source_path="corpus/arxiv/1111.1111/source/main.tex", content="Mabuchi")
    source_a_second = Chunk(chunk_id="a2", source_path="corpus/arxiv/1111.1111/source/appendix.tex", content="Mabuchi")
    source_b = Chunk(chunk_id="b1", source_path="corpus/arxiv/2222.2222/source/main.tex", content="Mabuchi")
    keyword = FixedSearch([
        _result(source_a_first, 10.0),
        _result(source_a_second, 9.0),
        _result(source_b, 8.5),
    ])

    results = HybridSearch(
        [source_a_first, source_a_second, source_b],
        keyword_search=keyword,
        vector_search=FixedSearch([]),
    ).search("Mabuchi energy", top_k=2)

    assert [result.chunk.chunk_id for result in results] == ["a1", "b1"]


def test_source_diversity_does_not_promote_very_weak_new_sources():
    source_a_first = Chunk(chunk_id="a1", source_path="corpus/arxiv/1111.1111/source/main.tex", content="Mabuchi")
    source_a_second = Chunk(chunk_id="a2", source_path="corpus/arxiv/1111.1111/source/appendix.tex", content="Mabuchi")
    source_b = Chunk(chunk_id="b1", source_path="corpus/arxiv/2222.2222/source/main.tex", content="Mabuchi")
    keyword = FixedSearch([
        _result(source_a_first, 10.0),
        _result(source_a_second, 9.0),
        _result(source_b, 0.1),
    ])

    results = HybridSearch(
        [source_a_first, source_a_second, source_b],
        keyword_search=keyword,
        vector_search=FixedSearch([]),
    ).search("Mabuchi energy", top_k=2)

    assert [result.chunk.chunk_id for result in results] == ["a1", "a2"]


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
