from pathlib import Path

from math_rag.cli import main
from math_rag.evidence_eval import (
    SourceTitleResolver,
    format_candidate_evidence_inspection_markdown,
    format_candidate_evidence_triage_markdown,
    inspect_candidate_evidence_eval,
    load_candidate_evidence_questions,
    write_candidate_evidence_inspection_markdown,
    write_candidate_evidence_triage_markdown,
)
from math_rag.index_store import IndexStore
from math_rag.models import Chunk


RUBRIC = """
    relevance_rubric:
      "3": "Exact theorem/proposition/definition/proof/example."
      "2": "Relevant discussion."
      "1": "Bibliography only."
      "0": "Irrelevant."
"""


def _write_candidate_eval(path: Path) -> Path:
    path.write_text(
        f"""
questions:
  - id: weighted
    topic: weighted Mabuchi
    question: "weighted Mabuchi convex weak geodesics"
    expected_sources:
      - "2007.01345"
    expected_chunk_types:
      - theorem
    expected_terms:
      - "weighted Mabuchi"
      - "weak geodesics"
    preferred_sections:
      - "Convexity"
    review_status: unreviewed
    review_notes: ""
    correction_needed: ""
{RUBRIC}
  - id: negative
    topic: negative/non-established claims
    question: "complete new theorem about Floer homology"
    expected_sources: []
    expected_chunk_types: []
    expected_terms:
      - "Floer homology"
    preferred_sections: []
    negative: true
    review_status: unreviewed
    review_notes: ""
    correction_needed: ""
{RUBRIC}
""",
        encoding="utf-8",
    )
    return path


def _write_fixture_index(index_dir: Path) -> None:
    chunks = [
        Chunk(
            chunk_id="weighted-theorem",
            source_path="corpus/arxiv/2007.01345/source/source.tex",
            chunk_type="theorem",
            section_path=["Convexity"],
            line_start=10,
            line_end=15,
            content="The weighted Mabuchi functional is convex along weak geodesics.",
            metadata={"arxiv_id": "2007.01345"},
        ),
        Chunk(
            chunk_id="negative-theorem",
            source_path="corpus/arxiv/0000.00000/source/source.tex",
            chunk_type="theorem",
            section_path=["Speculation"],
            content="A complete new theorem about Floer homology is mentioned only as a placeholder.",
            metadata={"arxiv_id": "0000.00000"},
        ),
        Chunk(
            chunk_id="citation",
            source_path="corpus/arxiv/9999.99999/source/refs.bib",
            chunk_type="citation_context",
            content="A bibliography entry mentioning weighted Mabuchi.",
            metadata={"arxiv_id": "9999.99999"},
        ),
    ]
    IndexStore(index_dir).save_chunks(chunks)


def _write_arxiv_metadata(root: Path, arxiv_id: str = "2007.01345", title: str = "Convexity of the weighted Mabuchi functional") -> None:
    metadata_dir = root / "corpus" / "arxiv" / arxiv_id
    metadata_dir.mkdir(parents=True)
    (metadata_dir / "metadata.yaml").write_text(f"arxiv_id: '{arxiv_id}'\ntitle: {title!r}\n", encoding="utf-8")


def test_load_candidate_evidence_questions(tmp_path):
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")

    questions = load_candidate_evidence_questions(eval_path)

    assert [question.question_id for question in questions] == ["weighted", "negative"]
    assert questions[0].topic == "weighted Mabuchi"
    assert questions[0].expected_chunk_types == ["theorem"]
    assert questions[0].review_status == "unreviewed"
    assert questions[0].review_notes == ""
    assert questions[0].correction_needed == ""
    assert questions[1].negative is True


def test_load_candidate_evidence_questions_rejects_invalid_review_status(tmp_path):
    eval_path = tmp_path / "bad_candidate.yaml"
    eval_path.write_text(
        f"""
questions:
  - id: bad
    topic: weighted Mabuchi
    question: "weighted Mabuchi convex weak geodesics"
    expected_sources: ["2007.01345"]
    expected_chunk_types: ["theorem"]
    expected_terms: ["weighted Mabuchi"]
    preferred_sections: []
    review_status: reviewed
    review_notes: ""
    correction_needed: ""
{RUBRIC}
""",
        encoding="utf-8",
    )

    import pytest

    with pytest.raises(ValueError, match="invalid review_status"):
        load_candidate_evidence_questions(eval_path)


def test_load_candidate_evidence_questions_accepts_needs_corpus_expansion(tmp_path):
    eval_path = tmp_path / "candidate.yaml"
    eval_path.write_text(
        f"""
questions:
  - id: corpus_gap
    topic: conic/cusp/Poincare metrics
    question: "Where is the missing primary source?"
    expected_sources: ["1109.3159"]
    expected_chunk_types: ["text"]
    expected_terms: ["Poincare type"]
    preferred_sections: []
    review_status: needs_corpus_expansion
    review_notes: "Better primary source is not yet in corpus."
    correction_needed: ""
{RUBRIC}
""",
        encoding="utf-8",
    )

    questions = load_candidate_evidence_questions(eval_path)

    assert questions[0].review_status == "needs_corpus_expansion"


def test_source_title_resolver_reads_arxiv_metadata(tmp_path):
    _write_arxiv_metadata(tmp_path)

    resolver = SourceTitleResolver(tmp_path)

    assert resolver.title_for_reference("2007.01345") == "Convexity of the weighted Mabuchi functional"
    assert resolver.title_for_path("corpus/arxiv/2007.01345/source/source.tex") == "Convexity of the weighted Mabuchi functional"


def test_source_title_resolver_uses_friendly_note_title():
    resolver = SourceTitleResolver()

    title = resolver.title_for_path(
        "corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex"
    )

    assert title == "CP1 one-conic-point notes"


def test_inspect_candidate_evidence_eval_reports_matches(tmp_path):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")

    report = inspect_candidate_evidence_eval(eval_path, index_dir=str(index_dir), top_k=3)
    rows = {row["id"]: row for row in report["rows"]}
    weighted = rows["weighted"]

    assert report["total_questions"] == 2
    assert weighted["review_status"] == "unreviewed"
    assert weighted["review_notes"] == ""
    assert weighted["correction_needed"] == ""
    assert weighted["diagnostics"]["expected_source_in_top_k"] is True
    assert weighted["diagnostics"]["expected_chunk_type_in_top_k"] is True
    assert weighted["diagnostics"]["expected_terms_in_top_k"] is True
    assert weighted["top_chunks"][0]["source_matches_expected"] is True
    assert weighted["top_chunks"][0]["chunk_type_matches_expected"] is True
    assert "weighted Mabuchi" in weighted["top_chunks"][0]["matched_expected_terms"]


def test_inspect_candidate_evidence_eval_flags_negative_manual_review(tmp_path):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")

    report = inspect_candidate_evidence_eval(eval_path, index_dir=str(index_dir), top_k=3)
    rows = {row["id"]: row for row in report["rows"]}

    assert rows["negative"]["negative"] is True
    assert rows["negative"]["diagnostics"]["negative_strong_evidence_manual_review_needed"] is True


def test_format_candidate_evidence_inspection_markdown_includes_manual_placeholders(tmp_path):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")
    report = inspect_candidate_evidence_eval(eval_path, index_dir=str(index_dir), top_k=2)

    markdown = format_candidate_evidence_inspection_markdown(report)

    assert "# Candidate Evidence Eval Inspection" in markdown
    assert "Expected source appeared in top-k" in markdown
    assert "**Review status:** `unreviewed`" in markdown
    assert "Manual relevance notes:" in markdown
    assert "Promote to gold? yes/no" in markdown
    assert "Correction needed:" in markdown


def test_write_candidate_evidence_inspection_markdown(tmp_path):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")
    report = inspect_candidate_evidence_eval(eval_path, index_dir=str(index_dir), top_k=2)
    out_path = tmp_path / "inspection.md"

    written = write_candidate_evidence_inspection_markdown(report, out_path)

    assert written == out_path
    assert out_path.exists()
    assert "Candidate Evidence Eval Inspection" in out_path.read_text(encoding="utf-8")


def test_format_candidate_evidence_triage_markdown_is_human_friendly(tmp_path):
    _write_arxiv_metadata(tmp_path)
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")
    report = inspect_candidate_evidence_eval(eval_path, index_dir=str(index_dir), top_k=3)

    markdown = format_candidate_evidence_triage_markdown(report, workspace_root=tmp_path)

    assert "# Candidate Evidence Triage" in markdown
    assert "Rank means retrieval order, not mathematical importance." in markdown
    assert "- 2007.01345 - Convexity of the weighted Mabuchi functional" in markdown
    assert "1. 2007.01345 - Convexity of the weighted Mabuchi functional" in markdown
    assert "   Convexity - lines 10-15" in markdown
    assert "Best evidence rank:" in markdown
    assert "Negative: true" in markdown
    assert "Status:" not in markdown
    assert "Notes:" not in markdown
    assert "Correction:" not in markdown
    assert "Expected terms" not in markdown
    assert "Expected chunk types" not in markdown
    assert "Source match" not in markdown
    assert "score" not in markdown.lower()


def test_write_candidate_evidence_triage_markdown(tmp_path):
    _write_arxiv_metadata(tmp_path)
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")
    report = inspect_candidate_evidence_eval(eval_path, index_dir=str(index_dir), top_k=2)
    out_path = tmp_path / "triage.md"

    written = write_candidate_evidence_triage_markdown(report, out_path, workspace_root=tmp_path)

    assert written == out_path
    assert out_path.exists()
    assert "Candidate Evidence Triage" in out_path.read_text(encoding="utf-8")


def test_argparse_inspect_evidence_eval_writes_markdown(tmp_path, capsys):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")
    out_path = tmp_path / "inspection.md"

    exit_code = main(
        [
            "inspect-evidence-eval",
            str(eval_path),
            "--index-dir",
            str(index_dir),
            "--top-k",
            "2",
            "--out",
            str(out_path),
        ]
    )
    output = capsys.readouterr().out

    assert exit_code == 0
    assert out_path.exists()
    assert "Candidate Evidence Eval Inspection" in output
    assert "Wrote candidate evidence inspection report to" in output


def test_argparse_inspect_evidence_eval_writes_triage_markdown(tmp_path, capsys):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_candidate_eval(tmp_path / "candidate.yaml")
    out_path = tmp_path / "triage.md"

    exit_code = main(
        [
            "inspect-evidence-eval",
            str(eval_path),
            "--index-dir",
            str(index_dir),
            "--top-k",
            "2",
            "--triage-out",
            str(out_path),
        ]
    )
    output = capsys.readouterr().out

    assert exit_code == 0
    assert out_path.exists()
    assert "Candidate Evidence Triage" in out_path.read_text(encoding="utf-8")
    assert "Wrote candidate evidence triage report to" in output
