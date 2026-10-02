"""Model defaults and compatibility with the persisted JSON index schema."""

import json

import pytest

from math_rag.index_store import IndexStore
from math_rag.models import Chunk, DocumentMetadata, SearchResult, metadata_from_dict, model_to_dict


def test_index_roundtrip_preserves_existing_schema(tmp_path):
    record = {
        "chunk_id": "theorem-1",
        "source_path": "corpus/paper.tex",
        "title": "Kähler metrics",
        "chunk_type": "theorem",
        "section_path": ["Estimates", "Main result"],
        "page_number": None,
        "line_start": 12,
        "line_end": 18,
        "content": "The weighted Mabuchi energy is convex.",
        "metadata": {"source_format": "tex", "authors": ["A. Researcher"]},
        "symbols": ["Mabuchi"],
        "topics": ["Kähler"],
    }
    store = IndexStore(tmp_path)
    # Existing indexes may contain extra fields written by another version.
    store.index_path.write_text(
        json.dumps({"schema_version": 1, "chunks": [{**record, "future_field": True}]}),
        encoding="utf-8",
    )

    chunks = store.load_chunks()
    assert len(chunks) == 1
    assert model_to_dict(chunks[0]) == record
    store.save_chunks(chunks)

    assert json.loads(store.index_path.read_text(encoding="utf-8")) == {
        "schema_version": 1,
        "chunks": [record],
    }
    assert store.load_chunks() == chunks


def test_metadata_roundtrip_ignores_extra_yaml_fields():
    record = {
        "source_path": "corpus/note.md",
        "title": "Research notes",
        "authors": ["A. Researcher"],
        "year": 2026,
        "document_type": "note",
        "topics": ["toric"],
        "mathematical_objects": ["polytope"],
        "status": "read",
        "notes": "Check hypotheses.",
    }

    metadata = metadata_from_dict({**record, "personal_label": "working"})

    assert model_to_dict(metadata) == record
    assert metadata_from_dict(json.loads(json.dumps(record))) == metadata


def test_mutable_defaults_are_isolated_between_models():
    first = Chunk(chunk_id="one", source_path="corpus/one.md")
    second = Chunk(chunk_id="two", source_path="corpus/two.md")
    first.section_path.append("Section")
    first.metadata["source_format"] = "md"
    first.symbols.append("x")
    first.topics.append("toric")

    assert second.section_path == []
    assert second.metadata == {}
    assert second.symbols == []
    assert second.topics == []
    assert second.content == ""

    first_metadata = DocumentMetadata(source_path="corpus/one.md")
    second_metadata = DocumentMetadata(source_path="corpus/two.md")
    first_metadata.authors.append("A. Researcher")
    first_metadata.topics.append("toric")
    first_metadata.mathematical_objects.append("polytope")

    assert second_metadata.authors == []
    assert second_metadata.topics == []
    assert second_metadata.mathematical_objects == []


def test_search_result_serialization_is_json_ready_and_detached():
    chunk = Chunk(chunk_id="one", source_path="corpus/note.md", topics=["toric"])
    result = SearchResult(chunk=chunk, score=0.7, keyword_score=0.5, vector_score=0.2, rank=1)

    payload = model_to_dict(result)

    assert json.loads(json.dumps(payload)) == payload
    assert payload["chunk"]["chunk_id"] == "one"
    assert {key: value for key, value in payload.items() if key != "chunk"} == {
        "score": 0.7,
        "keyword_score": 0.5,
        "vector_score": 0.2,
        "rank": 1,
    }
    payload["chunk"]["topics"].append("weighted")
    assert chunk.topics == ["toric"]


def test_model_to_dict_rejects_unsupported_values():
    with pytest.raises(TypeError, match="Cannot serialize"):
        model_to_dict("not a model")
