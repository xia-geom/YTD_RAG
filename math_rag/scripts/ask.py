"""Ask a retrieval-grounded question."""

from __future__ import annotations

import argparse

from math_rag.cli import run_ask


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--index-dir", default=".math_rag_index")
    parser.add_argument("--mode", default="hybrid", choices=["keyword", "vector", "hybrid"])
    parser.add_argument("--top-k", type=int, default=6)
    args = parser.parse_args()
    return run_ask(args.query, args.index_dir, args.mode, args.top_k)


if __name__ == "__main__":
    raise SystemExit(main())

