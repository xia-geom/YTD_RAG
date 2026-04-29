from math_rag.citations import format_citation
from math_rag.models import Chunk


def test_citation_formatting_includes_source_section_page_and_lines():
    chunk = Chunk(
        chunk_id="c1",
        source_path="corpus/notes.tex",
        chunk_type="theorem",
        section_path=["Conic metrics", "Poincare limit"],
        page_number=7,
        line_start=41,
        line_end=49,
        content="A retrieved theorem statement.",
    )

    citation = format_citation(chunk)

    assert "corpus/notes.tex" in citation
    assert "Conic metrics > Poincare limit" in citation
    assert "p. 7" in citation
    assert "lines 41-49" in citation


def test_citation_formatting_handles_missing_optional_location():
    chunk = Chunk(chunk_id="c2", source_path="corpus/a.bib", chunk_type="citation_context", content="Citation key.")

    assert format_citation(chunk) == "[corpus/a.bib]"

