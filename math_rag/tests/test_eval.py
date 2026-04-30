from pathlib import Path

import pytest

from math_rag.cli import _argparse_main
from math_rag.eval import evaluate_retrieval, format_eval_report, load_gold_questions
from math_rag.index_store import IndexStore
from math_rag.models import Chunk


def _write_eval(path: Path, text: str) -> Path:
    path.write_text(text, encoding="utf-8")
    return path


def _write_fixture_index(index_dir: Path) -> None:
    chunks = [
        Chunk(
            chunk_id="weighted",
            source_path="corpus/arxiv/2007.01345/source/source.tex",
            chunk_type="text",
            content="The weighted Mabuchi functional is convex along weak geodesics.",
            metadata={"arxiv_id": "2007.01345"},
        ),
        Chunk(
            chunk_id="abreu",
            source_path="corpus/arxiv/math_0407486/source/intest.tex",
            chunk_type="text",
            content="Donaldson proves interior estimates for solutions of Abreu's equation on a polytope.",
            metadata={"arxiv_id": "math/0407486"},
        ),
        Chunk(
            chunk_id="generic",
            source_path="corpus/arxiv/0000.00000/source/source.tex",
            chunk_type="text",
            content="A generic discussion of metrics and energy without the expected paper.",
            metadata={"arxiv_id": "0000.00000"},
        ),
    ]
    IndexStore(index_dir).save_chunks(chunks)


def test_load_gold_questions_supports_positive_and_negative_entries(tmp_path):
    eval_path = _write_eval(
        tmp_path / "gold.yaml",
        """
questions:
  - id: weighted
    question: "Where is weighted Mabuchi convexity?"
    expected_sources:
      - "2007.01345"
  - id: negative
    question: "Does this prove a new theorem?"
    expected_sources: []
    negative: true
""",
    )

    questions = load_gold_questions(eval_path)

    assert [question.question_id for question in questions] == ["weighted", "negative"]
    assert questions[0].expected_sources == ["2007.01345"]
    assert questions[1].negative is True


def test_load_gold_questions_requires_expected_sources_unless_negative(tmp_path):
    eval_path = _write_eval(
        tmp_path / "bad.yaml",
        """
questions:
  - id: bad
    question: "No relevance judgement?"
    expected_sources: []
""",
    )

    with pytest.raises(ValueError, match="expected_sources"):
        load_gold_questions(eval_path)


def test_evaluate_retrieval_computes_hits_and_missing_sources(tmp_path):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_eval(
        tmp_path / "gold.yaml",
        """
questions:
  - id: weighted
    question: "weighted Mabuchi convex weak geodesics"
    expected_sources:
      - "2007.01345"
  - id: abreu
    question: "Abreu equation interior estimates polytope"
    expected_sources:
      - "math_0407486"
  - id: missing
    question: "Poincare type toric extremal metrics"
    expected_sources:
      - "1711.08424"
  - id: negative
    question: "Does this prove a complete new theorem?"
    expected_sources: []
    negative: true
""",
    )

    summary = evaluate_retrieval(eval_path, index_dir=str(index_dir), top_k=3)

    assert summary["total_questions"] == 4
    assert summary["evaluated_questions"] == 3
    assert summary["negative_questions"] == 1
    assert summary["hits_at"][1]["hits"] == 2
    assert summary["hits_at"][3]["hits"] == 2
    assert summary["missing_expected_sources"] == ["1711.08424"]
    rows = {row["question_id"]: row for row in summary["rows"]}
    assert rows["weighted"]["hit"] is True
    assert rows["abreu"]["first_expected_rank"] == 1
    assert rows["missing"]["hit"] is False
    assert rows["negative"]["hit"] is None


def test_format_eval_report_has_stable_schema(tmp_path):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_eval(
        tmp_path / "gold.yaml",
        """
questions:
  - id: weighted
    question: "weighted Mabuchi convex weak geodesics"
    expected_sources:
      - "2007.01345"
""",
    )
    summary = evaluate_retrieval(eval_path, index_dir=str(index_dir), top_k=5)

    report = format_eval_report(summary)

    assert report.splitlines()[0] == "Question ID | Hit? | First expected rank | Expected sources | Top sources"
    assert "Total questions: 1" in report
    assert "hits@1: 1/1 = 1.000" in report
    assert "Missing expected sources:" in report
    assert "Worst failures:" in report


def test_argparse_eval_command_runs_on_fixture_index(tmp_path, capsys):
    index_dir = tmp_path / "index"
    _write_fixture_index(index_dir)
    eval_path = _write_eval(
        tmp_path / "gold.yaml",
        """
questions:
  - id: weighted
    question: "weighted Mabuchi convex weak geodesics"
    expected_sources:
      - "2007.01345"
  - id: negative
    question: "Does this prove a complete new theorem?"
    expected_sources: []
    negative: true
""",
    )

    exit_code = _argparse_main(["eval", str(eval_path), "--index-dir", str(index_dir), "--top-k", "3"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "Question ID | Hit?" in output
    assert "weighted | yes | 1" in output
    assert "negative | negative | -" in output
