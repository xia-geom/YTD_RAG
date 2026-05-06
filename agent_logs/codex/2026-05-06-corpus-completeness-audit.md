# Agent Log: Corpus Completeness Audit

Date: 2026-05-06
Agent: Codex
Branch: master
Commit: 345adcf
Related files:
- `corpus/arxiv/*/metadata.yaml`
- `.math_rag_index/index.json`
- `corpus/my_notes/requested_non_arxiv_sources.md`
- `corpus/my_notes/project_paper_index.md`
- `eval/toric_core_gold_questions.yaml`

## Goal

Verify that expected papers are present and correctly ingested before making retrieval-ranking changes.

## Commands Run

```bash
math_rag/.venv/bin/python -m math_rag.cli stats
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/
```

Also ran a local read-only metadata/index consistency script over `corpus/arxiv/*/metadata.yaml` and `.math_rag_index/index.json`.

## Index Status

```text
Index: .math_rag_index/index.json
Sources: 80
Chunks: 13870
Chunk types:
  citation_context: 424
  conjecture: 54
  definition: 518
  example: 96
  lemma: 740
  proof: 1171
  proposition: 510
  question: 7
  remark: 445
  text: 9088
  theorem: 817
```

## Completeness Checks

Checked each `corpus/arxiv/<folder>` for:

- `metadata.yaml` exists;
- `primary_ingestion` exists;
- folder name matches normalized `arxiv_id`;
- `primary_ingestion: tex` has at least one `source/*.tex`;
- `pdf_available: true` has `paper.pdf`;
- at least one indexed chunk exists for the paper.

## Results

```text
ArXiv folders checked: 67
Index chunks checked: 13870
primary_ingestion distribution:
  tex: 66
  pdf: 1
Required-check failures: 0
```

No expected-source absence was found in eval. All expected sources in `eval/toric_gold_questions.yaml` are represented in the current index.

## Noteworthy Cases

- `corpus/arxiv/dg-ga_9711014` has `primary_ingestion: pdf`, so no `.tex` is required by the audit rule.
- `corpus/arxiv/dg-ga_9711014/source/source` exists as an extensionless source file, but indexed chunks come from `paper.pdf`.
- `corpus/my_notes/project_paper_index.md` now covers every `corpus/arxiv/*` folder by local ID.

## Non-ArXiv Pointers

`corpus/my_notes/requested_non_arxiv_sources.md` records:

- Donaldson, "Scalar curvature and stability of toric varieties": bibliographic pointer only.
- Boucksom-Hisamoto-Jonsson EMS correction pointer: arXiv source exists locally at `corpus/arxiv/1603.01026`.
- Cheng-Yau complete Kähler metric paper: bibliographic pointer only.
- Tian-Yau complete Kähler metric papers: bibliographic pointer only; exact papers still need manual selection.

## Important Decision

Corpus completeness is not the current blocker. Retrieval misses are ranking/retrieval-quality failures, not missing-paper failures.

## Known Limitations

This audit checks source-level presence and chunk presence. It does not verify passage-level correctness inside each paper.

## Recommended Next Step

Use the retrieval precision audit to decide the first conservative ranking hygiene patch. Do not expand the corpus as a way to fix the current eval misses.
