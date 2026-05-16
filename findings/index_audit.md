# Public-Safe Index Audit

Date: 2026-05-16

## Status

GO_INDEX_PUBLIC_SAFE=true

The candidate index at `.math_rag_index/index.json` exists, loads as JSON, and
was accepted for this public-safe sprint after the user explicitly reclassified
relative `corpus/my_notes` provenance as public knowledge.

## Evidence

- `index.json` size: 57,457,360 bytes
- Top-level keys: `chunks`, `schema_version`
- Chunk count: 18,544
- Distinct source paths: 104
- Source path prefix counts:
  - `corpus/arxiv`: 18,274 chunks
  - `corpus/my_notes`: 270 chunks, accepted by user as public-safe

Hard forbidden marker scan after reclassification:

- No `/Users/`
- No `/home/`
- No `/mnt/data/`
- No `/private/tmp/`
- No `file://`
- No API key, Azure credential, storage key, connection string, `.env`, or
  `private_notes` marker

Review markers:

- `unpublished`: appears in public citation/prose contexts such as
  `Tian-unpublished`; treated as public bibliographic text, not private source
  classification.
- `sk-`: appears inside TeX/math tokens such as `fsk`; treated as a false
  positive, not an API key prefix.

## Decision

The index is acceptable for the low-cost public-safe connector lane. It remains
unsuitable for a private-secret-index claim because the architecture still has a
public backend and no OAuth/JWT user gate.
