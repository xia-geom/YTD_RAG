# Agent Log: Ranking Hygiene Patch

Date: 2026-05-06
Agent: Codex
Branch: main
Commit: uncommitted
Related files:
- `math_rag/src/math_rag/hybrid_search.py`
- `math_rag/tests/test_hybrid_search.py`
- `eval/toric_core_gold_questions.yaml`

## Goal

Recover top-1 retrieval precision after the enriched index made navigation notes, especially `corpus/my_notes/project_paper_index.md`, too competitive with primary mathematical sources.

## Files Created

- `agent_logs/codex/2026-05-06-ranking-hygiene-patch.md`

## Files Modified

- `math_rag/src/math_rag/hybrid_search.py`
- `math_rag/tests/test_hybrid_search.py`

## Commands Run

```bash
cd /Users/xiaxiao/Desktop/Projects/YTD_RAG/math_rag
.venv/bin/python -m pytest tests/test_hybrid_search.py tests/test_metadata_enrichment.py
.venv/bin/python -m pytest

cd /Users/xiaxiao/Desktop/Projects/YTD_RAG
math_rag/.venv/bin/python -m math_rag.cli ingest corpus/ --enrich-metadata
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
```

## Test Results

- Focused retrieval/enrichment tests: 23 passed.
- Full test suite: 129 passed.

## Eval Results

Baseline after cached metadata enrichment but before ranking hygiene:

- hits@1: 4/39
- hits@3: 23/39
- hits@5: 30/39

After ranking hygiene:

- total chunks: 13,870
- hits@1: 17/39
- hits@3: 28/39
- hits@5: 31/39
- missing expected sources: none

## Important Decisions

- Demote navigation notes for ordinary mathematical queries.
- Keep navigation notes competitive for explicit paper-list/source-list/bibliography queries.
- Demote engineering memory for mathematical retrieval.
- Lightly boost primary papers.
- Boost project notes only when the query explicitly asks for notes, tables, dictionaries, CP1 examples, moment intervals, or notation.
- Add score-gated source diversity: a different source can jump ahead only when it is competitively scored.

## Known Limitations

- Remaining misses are not all ranking hygiene problems. Some require query-specific signals, better note retrieval, or passage-level evaluation.
- Source diversity groups arXiv papers by `corpus/arxiv/<id>`, but other local source families are still grouped by file path.
- The retrieval stack is still deterministic sparse retrieval, not dense semantic embedding.

## Recommended Next Step

Run a second precision audit on the remaining worst failures and classify them before adding more ranking weights. In particular, inspect:

- `abreu_equation`
- `slope_stability`
- `cp1_polytope_one_cusp`
- `cusp_alpha_beta_table`
- `toric_kenergy_dictionary`
- `symplectic_potential_toric_notes`
