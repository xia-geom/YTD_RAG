"""Exercise the public CLI against a temporary corpus and index."""

import pytest

from math_rag.cli import main


def test_local_workflow_uses_explicit_arguments(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    # main(argv) must not read the host process arguments, regardless of which
    # optional packages happen to be installed.
    monkeypatch.setattr("sys.argv", ["math-rag", "unknown-command"])
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text(
        "# Toric geometry\n\nThe Mabuchi functional on a toric polytope.\n",
        encoding="utf-8",
    )
    index = tmp_path / "index"

    assert main(["ingest", str(corpus), "--index-dir", str(index)]) == 0
    assert (index / "index.json").is_file()
    assert "Ingested" in capsys.readouterr().out

    assert main(["search", "Mabuchi", "--index-dir", str(index), "--top-k", "1"]) == 0
    search_output = capsys.readouterr().out
    assert "notes.md" in search_output
    assert "Mabuchi functional" in search_output

    assert main(["ask", "Mabuchi", "--index-dir", str(index), "--top-k", "1"]) == 0
    answer = capsys.readouterr().out
    assert "Retrieved evidence:" in answer
    assert "Not established by retrieved sources:" in answer
    assert "notes.md" in answer

    assert main(["stats", "--index-dir", str(index)]) == 0
    assert "Sources: 1" in capsys.readouterr().out


def test_search_missing_index_reports_actionable_failure(tmp_path, capsys):
    assert main(["search", "Mabuchi", "--index-dir", str(tmp_path / "missing")]) == 1
    assert "Run: python -m math_rag.cli ingest corpus/" in capsys.readouterr().out


@pytest.mark.parametrize(
    "arguments",
    [
        [],
        ["unknown-command"],
        ["search", "Mabuchi", "--mode", "unknown"],
        ["download-arxiv", "1711.08424", "--force", "--skip-existing"],
        ["download-seed", "--force", "--skip-existing"],
    ],
)
def test_invalid_arguments_exit_before_running_command(arguments):
    with pytest.raises(SystemExit) as exc:
        main(arguments)
    assert exc.value.code == 2
