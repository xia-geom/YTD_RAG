# Candidate Evidence Evaluation Set

`candidate_evidence_questions.yaml` is a draft evidence-level evaluation set.
It is not a validated benchmark and should not be used for regression metrics
until each entry has been reviewed by a human.

The file is intentionally larger and more redundant than a final gold set. Its
purpose is to collect candidate questions, expected source hints, and evidence
rubric metadata for later pruning, correction, and promotion into a stable eval.

## Fields

- `id`: Stable candidate identifier.
- `topic`: Broad mathematical area for grouping and review.
- `question`: Retrieval question to ask the corpus.
- `expected_sources`: Candidate source hints expected to contain relevant
  evidence. These are not yet validated as exhaustive or uniquely correct.
- `expected_chunk_types`: Preferred evidence chunk types, such as `theorem`,
  `proposition`, `definition`, `proof`, `example`, or `text`.
- `expected_terms`: Terms that should appear in strong retrieved evidence.
- `preferred_sections`: Optional section-title hints when known. Empty means
  no section-level expectation has been validated yet.
- `negative`: Present and `true` for non-established claims where strong
  supporting evidence should not be expected.
- `review_status`: Human triage state. Valid values are `unreviewed`,
  `promote_candidate`, `needs_correction`, `drop`, and `exploratory_only`.
- `review_notes`: Short human review note.
- `correction_needed`: Short description of the expected correction, or empty.
- `relevance_rubric`: Evidence scoring guide:
  - `3`: Exact theorem/proposition/definition/proof/example.
  - `2`: Relevant discussion.
  - `1`: Bibliography only.
  - `0`: Irrelevant.

## Review Workflow

1. Run retrieval against this candidate file only for exploratory analysis.
2. Inspect top chunks manually, including source location and chunk type.
3. Update `review_status`, `review_notes`, and `correction_needed`.
4. Correct expected sources, terms, and section hints after review.
5. Remove ambiguous, duplicate, or over-broad questions.
6. Promote only reviewed entries into a stable gold file.

Do not compare metrics from this candidate set to the stable gold eval. The
candidate set is expected to change during review.

## Inspection Command

Generate a Markdown inspection report from the current local index:

```bash
math_rag/.venv/bin/python -m math_rag.cli inspect-evidence-eval \
  eval/candidate_evidence_questions.yaml \
  --top-k 10 \
  --out eval/candidate_evidence_inspection.md
```

The report lists each candidate question, expected evidence hints, top retrieved
chunks, source/type/term diagnostic matches, and manual review placeholders.

The diagnostic counts in this report are not regression metrics. They are only
triage signals for deciding which candidates need correction, pruning, or
promotion.

For a simpler human review file with paper titles and only the top three ranked
chunks per question, use:

```bash
math_rag/.venv/bin/python -m math_rag.cli inspect-evidence-eval \
  eval/candidate_evidence_questions.yaml \
  --top-k 10 \
  --triage-out eval/candidate_evidence_triage.md
```

Use the triage report first. It explains that rank is the retrieval order, not
mathematical importance, and leaves one editable field per candidate:
`Best evidence rank:`.

Suggested shorthand:

- Blank means the question looks fine and rank 1 is the best evidence.
- `1` means only rank 1 is relevant.
- `1,2` means ranks 1 and 2 are relevant; rank 3 is irrelevant.
- `3` means only rank 3 is relevant.
- `drop` means the candidate is bad or misleading.
- `fix: <short note>` means the candidate is useful but needs correction.

## Triage Statuses

- `unreviewed`: Default state; no human decision has been made.
- `promote_candidate`: Candidate looks suitable for later promotion after final
  source/wording checks.
- `needs_correction`: The candidate is useful, but sources, terms, chunk types,
  or wording need edits.
- `drop`: The candidate is too vague, misleading, duplicated, or mathematically
  unsuitable.
- `exploratory_only`: Useful for ad hoc research but not appropriate for a
  benchmark.

## Promoting Entries

Promote an entry into a stable gold eval only after manual review confirms:

- the question is clear and not duplicative;
- at least one expected source is truly relevant;
- the preferred evidence type and terms are reasonable;
- negative questions are genuinely not established by retrieved evidence;
- the stable eval file's simpler schema is sufficient for the promoted entry.

When promoting, copy only the reviewed fields required by the stable eval
schema, usually `id`, `question`, `expected_sources`, and optionally
`negative: true`.

## Scope

This file does not require any retrieval-code changes. It is data for future
evidence-level evaluation work. Existing ranking, MCP behavior, chunking, and
stable eval files should remain unchanged when editing candidate questions.
