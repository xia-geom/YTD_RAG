# Agent Log: Evidence Gold Promotion and Gold Audit

Date: 2026-05-09
Agent: Codex
Branch: master
Commit: Not committed
Related files:
- eval/candidate_evidence_questions.yaml
- eval/toric_evidence_gold_questions.yaml
- eval/gold_audit.yaml
- math_rag/src/math_rag/evidence_eval.py
- math_rag/tests/test_evidence_eval.py

## Status Before

- Candidate evidence set existed with 140 entries.
- Evidence gold file existed with 4 promoted entries.
- Core gold file existed with 42 entries but had not been audited in this evidence-review workflow.

## Goal of This Task

Continue candidate triage for the selected mixed-topic batch, promote clean candidates into evidence gold, and create a first-pass audit artifact for core and evidence gold without changing retrieval, ranking, chunking, MCP, or the core gold file.

## Changes Made

### Files Created

- `eval/gold_audit.yaml`
- `agent_logs/codex/2026-05-09-evidence-gold-promotion-and-audit.md`

### Files Modified

- `eval/candidate_evidence_questions.yaml`
  - Reviewed 20 selected candidate entries.
  - Marked 10 as `promote_candidate` and 10 as `needs_correction`.
- `eval/toric_evidence_gold_questions.yaml`
  - Added 10 promoted entries: 8 positive evidence questions and 2 negative sanity questions.
- `math_rag/src/math_rag/evidence_eval.py`
  - Allowed `needs_corpus_expansion` as a valid candidate review status.
- `math_rag/tests/test_evidence_eval.py`
  - Added coverage for `needs_corpus_expansion`.

### Files Removed / Renamed

- None.

## Commands Run

- `math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_evidence_gold_questions.yaml`
- `math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml`
- YAML parse validation for candidate, evidence gold, and audit files.
- `load_gold_questions` validation for core and evidence gold files.
- `math_rag/.venv/bin/python -m pytest math_rag/tests/test_eval.py math_rag/tests/test_evidence_eval.py`
- `math_rag/.venv/bin/python -m pytest math_rag/tests`

## Test Results

- Focused eval tests: 18 passed.
- Full package tests: 174 passed.

## Eval Results

- Evidence gold:
  - Total questions: 14
  - Positive questions: 12
  - Negative questions: 2
  - hits@1: 7/12 = 0.583
  - hits@3: 10/12 = 0.833
  - hits@5: 12/12 = 1.000
  - Missing expected sources: none
- Core gold:
  - Total questions: 42
  - Positive questions: 39
  - Negative questions: 3
  - hits@1: 17/39 = 0.436
  - hits@3: 28/39 = 0.718
  - hits@5: 31/39 = 0.795
  - Missing expected sources: none

Not run / Reason:
- No corpus ingestion was run because this task did not change corpus contents or retrieval code.

## Current Status After Task

- Implemented: selected-batch triage, evidence gold promotion, first-pass gold audit.
- Tested: YAML parsing, gold loading, focused eval tests, full package test suite.
- Working: evidence gold passes hits@5 for all positive entries.
- Not implemented: no retrieval/ranking/chunking/MCP changes.
- Blocked: none.
- Risk / caveat: `eval/gold_audit.yaml` is a first-pass audit; online identity is marked `yes` only for sources checked during this pass.

## Known Limitations / Open Issues

- Core gold has 8 weak-retrieval entries to review.
- Evidence gold intentionally overlaps with core gold; audit currently flags exact cross-file duplicate questions for later deduplication or merge decisions.
- Some candidate questions marked `needs_correction` are mathematically useful but too broad or mismatched to current expected sources.

## Recommended Next Step

Review the 8 weak-retrieval core gold entries in `eval/gold_audit.yaml` before expanding evidence gold further.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem evidence.
