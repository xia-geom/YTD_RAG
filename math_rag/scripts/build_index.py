"""Build a local index from a corpus folder."""

from __future__ import annotations

import argparse

from math_rag.cli import run_ingest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus_path")
    parser.add_argument("--index-dir", default=".math_rag_index")
    parser.add_argument("--metadata", default=None)
    args = parser.parse_args()
    return run_ingest(args.corpus_path, args.index_dir, args.metadata)


if __name__ == "__main__":
    raise SystemExit(main())

