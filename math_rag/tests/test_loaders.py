"""Tests for corpus discovery, including PDF-vs-TeX shadowing for personal notes."""

from __future__ import annotations

from math_rag.loaders import discover_files


def test_discover_files_skips_pdf_when_sibling_tex_exists(tmp_path):
    notes = tmp_path / "my_notes" / "tables"
    notes.mkdir(parents=True)
    (notes / "kenergy_table.tex").write_text("\\section{K-energy}\nContent.\n", encoding="utf-8")
    (notes / "kenergy_table.pdf").write_bytes(b"%PDF-1.4\n%dummy\n")
    (notes / "kenergy_table.aux").write_text("aux", encoding="utf-8")  # unsupported, ignored anyway

    discovered = [p.name for p in discover_files(tmp_path)]

    assert "kenergy_table.tex" in discovered
    assert "kenergy_table.pdf" not in discovered


def test_discover_files_keeps_pdf_when_no_sibling_text(tmp_path):
    notes = tmp_path / "papers"
    notes.mkdir()
    (notes / "scan_only.pdf").write_bytes(b"%PDF-1.4\n%dummy\n")

    discovered = [p.name for p in discover_files(tmp_path)]

    assert "scan_only.pdf" in discovered


def test_discover_files_does_not_shadow_pdf_in_arxiv_governed_folders(tmp_path):
    """arXiv folders use metadata.yaml + should_ingest_arxiv_file to decide PDF vs source.
    The generic shadow filter must not apply there."""

    arxiv = tmp_path / "corpus" / "arxiv" / "1234.5678"
    source = arxiv / "source"
    source.mkdir(parents=True)
    (source / "paper.tex").write_text("Hello.\n", encoding="utf-8")
    (arxiv / "paper.pdf").write_bytes(b"%PDF-1.4\n")
    (arxiv / "metadata.yaml").write_text(
        "arxiv_id: '1234.5678'\nprimary_ingestion: tex\n", encoding="utf-8"
    )

    discovered = [str(p.relative_to(tmp_path)) for p in discover_files(tmp_path)]

    # paper.pdf is in a different directory than paper.tex, so the generic filter
    # would not have shadowed it anyway, but should_ingest_arxiv_file=False because
    # primary_ingestion=tex and the PDF is not under source/. Ensure we aren't
    # accidentally re-introducing it via the shadowing logic either.
    assert "corpus/arxiv/1234.5678/source/paper.tex" in discovered
    assert "corpus/arxiv/1234.5678/paper.pdf" not in discovered
