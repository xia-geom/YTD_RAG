from __future__ import annotations

import json

from math_rag.loaders import load_corpus
from math_rag.metadata_enrichment_cache import MetadataEnrichmentCache


def test_deterministic_ingest_without_enrichment_is_unchanged(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text("# Notes\n\nMabuchi energy and toric geometry.\n", encoding="utf-8")

    chunks, warnings = load_corpus(corpus)

    assert warnings == []
    assert chunks
    assert "enrichment" not in chunks[0].metadata


def test_enrichment_preserves_deterministic_chunk_fields(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text("# Notes\n\nMabuchi energy and toric geometry.\n", encoding="utf-8")

    base_chunks, _ = load_corpus(corpus)
    enriched_chunks, warnings = load_corpus(
        corpus,
        enrich_metadata=True,
        enrichment_cache_dir=tmp_path / "cache",
    )

    assert warnings == []
    assert len(enriched_chunks) == len(base_chunks)
    for base, enriched in zip(base_chunks, enriched_chunks, strict=True):
        assert enriched.chunk_id == base.chunk_id
        assert enriched.content == base.content
        assert enriched.line_start == base.line_start
        assert enriched.line_end == base.line_end
        assert enriched.chunk_type == base.chunk_type
        assert "enrichment" in enriched.metadata


def test_project_paper_index_gets_navigation_note_role(tmp_path):
    path = tmp_path / "corpus" / "my_notes" / "project_paper_index.md"
    path.parent.mkdir(parents=True)
    path.write_text("# Project Paper Index\n\nA reading map.\n", encoding="utf-8")

    chunks, warnings = load_corpus(
        tmp_path / "corpus",
        enrich_metadata=True,
        enrichment_cache_dir=tmp_path / "cache",
    )

    assert warnings == []
    enrichment = chunks[0].metadata["enrichment"]
    assert enrichment["source_role"] == "navigation_note"
    assert enrichment["is_navigation_note"] is True


def test_arxiv_chunks_get_primary_paper_role(tmp_path):
    arxiv = tmp_path / "corpus" / "arxiv" / "1234.5678"
    source = arxiv / "source"
    source.mkdir(parents=True)
    tex = source / "paper.tex"
    tex.write_text("\\section{Intro}\nToric cscK metrics.\n", encoding="utf-8")
    (arxiv / "paper.pdf").write_bytes(b"%PDF-1.4\n")
    (arxiv / "metadata.yaml").write_text(
        "arxiv_id: '1234.5678'\nprimary_ingestion: tex\npdf_available: true\n",
        encoding="utf-8",
    )

    chunks, warnings = load_corpus(
        tmp_path / "corpus",
        enrich_metadata=True,
        enrichment_cache_dir=tmp_path / "cache",
    )

    assert warnings == []
    assert chunks
    assert chunks[0].metadata["enrichment"]["source_role"] == "primary_paper"


def test_cache_hit_reuses_enrichment_metadata(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text("# Notes\n\nMabuchi energy.\n", encoding="utf-8")
    cache = MetadataEnrichmentCache(tmp_path / "cache")

    chunks, _ = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)
    cache_path = cache.cache_path_for_source(note)
    payload = json.loads(cache_path.read_text(encoding="utf-8"))
    payload["enrichments_by_chunk_id"][chunks[0].chunk_id]["semantic_title"] = "cached sentinel"
    cache_path.write_text(json.dumps(payload), encoding="utf-8")

    cached_chunks, warnings = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)

    assert warnings == []
    assert cached_chunks[0].metadata["enrichment"]["semantic_title"] == "cached sentinel"


def test_changed_source_hash_invalidates_cache(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text("# Notes\n\nMabuchi energy.\n", encoding="utf-8")
    cache = MetadataEnrichmentCache(tmp_path / "cache")

    chunks, _ = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)
    cache_path = cache.cache_path_for_source(note)
    payload = json.loads(cache_path.read_text(encoding="utf-8"))
    payload["enrichments_by_chunk_id"][chunks[0].chunk_id]["semantic_title"] = "stale sentinel"
    cache_path.write_text(json.dumps(payload), encoding="utf-8")
    note.write_text("# Notes\n\nMabuchi energy changed.\n", encoding="utf-8")

    refreshed_chunks, warnings = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)

    assert warnings == []
    assert refreshed_chunks[0].metadata["enrichment"]["semantic_title"] != "stale sentinel"


def test_enrichment_version_change_invalidates_cache(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text("# Notes\n\nMabuchi energy.\n", encoding="utf-8")
    cache = MetadataEnrichmentCache(tmp_path / "cache")

    chunks, _ = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)
    cache_path = cache.cache_path_for_source(note)
    payload = json.loads(cache_path.read_text(encoding="utf-8"))
    payload["enrichment_version"] = "old_version"
    payload["enrichments_by_chunk_id"][chunks[0].chunk_id]["semantic_title"] = "stale sentinel"
    cache_path.write_text(json.dumps(payload), encoding="utf-8")

    refreshed_chunks, warnings = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)

    assert warnings == []
    assert refreshed_chunks[0].metadata["enrichment"]["semantic_title"] != "stale sentinel"


def test_refresh_enrichment_cache_ignores_valid_cache(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text("# Notes\n\nMabuchi energy.\n", encoding="utf-8")
    cache = MetadataEnrichmentCache(tmp_path / "cache")

    chunks, _ = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)
    cache_path = cache.cache_path_for_source(note)
    payload = json.loads(cache_path.read_text(encoding="utf-8"))
    payload["enrichments_by_chunk_id"][chunks[0].chunk_id]["semantic_title"] = "cached sentinel"
    cache_path.write_text(json.dumps(payload), encoding="utf-8")

    refreshed_chunks, warnings = load_corpus(
        corpus,
        enrich_metadata=True,
        enrichment_cache_dir=cache.cache_dir,
        refresh_enrichment_cache=True,
    )

    assert warnings == []
    assert refreshed_chunks[0].metadata["enrichment"]["semantic_title"] != "cached sentinel"


def test_malformed_cache_falls_back_to_recomputing_enrichment(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    note = corpus / "notes.md"
    note.write_text("# Notes\n\nMabuchi energy.\n", encoding="utf-8")
    cache = MetadataEnrichmentCache(tmp_path / "cache")
    cache.files_dir.mkdir(parents=True)
    cache.cache_path_for_source(note).write_text("{not json", encoding="utf-8")

    chunks, warnings = load_corpus(corpus, enrich_metadata=True, enrichment_cache_dir=cache.cache_dir)

    assert warnings == []
    assert chunks[0].metadata["enrichment"]["source_role"] == "project_note"
