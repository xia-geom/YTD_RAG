# Corpus

Put private research documents here, or pass another folder to:

```bash
python -m math_rag.cli ingest /path/to/corpus
```

Supported first-version formats:

- `.tex`
- `.md`, `.markdown`
- `.txt`
- `.bib`
- `.pdf` when `pypdf` is installed

The default index is written locally to `.math_rag_index/`.

`research_profile.md` is a local vocabulary and discovery seed. It should not be treated as evidence for mathematical claims.
