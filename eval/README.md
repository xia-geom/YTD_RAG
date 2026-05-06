# Evaluation Files

Use `toric_core_gold_questions.yaml` as the stable regression eval for ranking and retrieval changes.

`toric_gold_questions.yaml` is the original eval filename kept for backward compatibility with older commands, notes, and scripts. It currently contains the same questions as the core eval, but new experiments should not treat both files as independent benchmarks.

Recommended command:

```bash
math_rag/.venv/bin/python -m math_rag.cli eval eval/toric_core_gold_questions.yaml
```

Metrics from different eval files should not be compared blindly. Compare hits@k only when the question set is intentionally stable.
