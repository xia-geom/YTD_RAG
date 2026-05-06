# Agent Log: Retrieval Precision Audit

Date: 2026-05-06
Agent: Codex
Branch: master
Commit: 345adcf
Related files:
- `eval/toric_gold_questions.yaml`
- `eval/toric_core_gold_questions.yaml`
- `.math_rag_index/index.json`
- `corpus/my_notes/project_paper_index.md`
- `math_rag/src/math_rag/eval.py`
- `math_rag/src/math_rag/hybrid_search.py`
- `math_rag/src/math_rag/keyword_search.py`

## Goal

Classify retrieval failures before changing ranking. The target is to recover hits@1 without losing hits@3/hits@5.

## Commands Run

```bash
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_gold_questions.yaml
```

Also ran focused diagnostics over the worst failures using `IndexStore`, `search_chunks`, and eval source-matching helpers.

## Eval Baseline

Current source-level eval after adding and ingesting `corpus/my_notes/project_paper_index.md`:

```text
Total questions: 42
Evaluated positive questions: 39
Negative questions: 3
hits@1: 4/39 = 0.103
hits@3: 23/39 = 0.590
hits@5: 30/39 = 0.769
Missing expected sources:
- none
```

This is not directly comparable to older metrics because the new paper index is now in the corpus and often ranks first.

## Failure Classification

### Right Source Missing Entirely

None. Corpus/index completeness is not the blocker.

### Right Source Present But Below Top 5

- `weighted_ytd`: expected `2509.15016`; official eval rank 9.
- `toric_kahler_extremal_abreu`: expected `dg-ga_9711014` or `0805.0128`; official eval rank 7.
- `slope_stability`: expected `math_0412518`; official eval rank 11.
- `symplectic_potential_toric_notes`: expected `2208.12493` or `one_conic_point.tex`; official eval rank 8.

Focused diagnostics sometimes found the expected source earlier when retrieving a larger raw pool. This indicates that duplicate chunks from high-scoring sources can crowd the retrieval pool before source-level deduplication.

### Right Source Indexed But Not Retrieved In Eval Pool

- `poincare_metric_space`: expected `1205.0056`; focused run found it at unique-source rank 12.
- `abreu_equation`: expected `dg-ga_9711014`, `math_0407486`, or `0805.0128`; focused run found `0805.0128` at unique-source rank 14.
- `cp1_polytope_one_cusp`: expected `one_cusp_point.tex`; not found in focused top 20.
- `cusp_alpha_beta_table`: expected `notation_table.tex`; focused run found it at unique-source rank 10.
- `toric_kenergy_dictionary`: expected `kenergy_table.tex`; not found in focused top 20.

### Bibliography/Citation Chunks Outranking Content

Not currently the visible failure mode. A diagnostic top-5 pass found no `citation_context` chunks in the failed top-5 source lists.

### Same Source Dominates Top Results

This is a major issue.

Examples from raw top-20 results:

```text
weighted_ytd:
  project_paper_index.md: 9/20 raw chunks

toric_kahler_extremal_abreu:
  project_paper_index.md: 12/20 raw chunks

symplectic_potential_toric_notes:
  project_paper_index.md: 9/20 raw chunks

poincare_metric_space:
  project_paper_index.md: 6/20 raw chunks
  weighted_twisted.tex: 4/20 raw chunks
```

The eval deduplicates by source after search, but search only retrieves a finite raw pool. If one source contributes many high-scoring chunks, expected sources can be pushed out of that raw pool before source-level ranking is computed.

### Metadata Noise

The dominant noise is not structural LaTeX commands or citation chunks. It is broad metadata/search-surface usefulness from `project_paper_index.md`.

The paper index is doing what it was designed to do for navigation, but it is hurting source-level regression eval because it is not itself usually an expected source.

Broad `concept_tags` also appear on many plausible-but-not-expected sources, especially:

- `abreu_toric`
- `poincare_cusp`
- `csck`
- `weighted_extremal`
- `mabuchi_k_energy`

These tags are useful, but should remain weaker than direct title/content/source matches.

### Query Wording Mismatch

Likely for my-notes/table questions:

- `cp1_polytope_one_cusp`
- `cusp_alpha_beta_table`
- `toric_kenergy_dictionary`

The expected files are short notes/tables, while query terms are broad and match major arXiv papers or the paper index more strongly.

## Most Important Findings

1. The corpus is complete for the current eval expectations.
2. The new `project_paper_index.md` is now a strong top-result source and depresses hits@1.
3. Duplicate high-scoring chunks from the same source crowd the raw retrieval pool.
4. `citation_context` is already demoted and is not a top-5 problem in this run.
5. Some eval questions may need clearer expected source policy: project/navigation notes are useful, but core source-level regression should probably prefer original papers and dedicated notes over the global paper index.

## Recommended Ranking Patch

First conservative patch, in this order:

1. Add source diversity before final top-k selection, so one source cannot occupy too much of the raw retrieval pool.
2. Downweight global navigation notes such as `corpus/my_notes/project_paper_index.md` for source-level search/eval unless the query asks for papers, bibliography, reading map, or source list.
3. Keep the existing `citation_context` demotion; do not change it first.
4. Keep concept tags lower weight than content/title/source-path signals.

## Success Criteria

After the patch:

```text
hits@1 improves from 4/39
hits@3 remains >= 23/39
hits@5 remains >= 30/39
Missing expected sources remains none
```

## Known Limitations

This audit is source-level. It does not check whether the retrieved chunk contains the exact passage that answers the question.
