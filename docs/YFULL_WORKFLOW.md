# YFull data workflow (local/private)

This project can ingest **YFull exports** (CSV/PDF) to keep your modern Y-DNA context alongside the Bodzia (VK155/VK157) research.

## Input location

Place YFull export files in:

- `data/raw/y_dna_results/`

This folder is ignored by git (contains genetic data).

## Parse and summarize

Run:

```bash
python scripts/analyze_yfull_exports.py
```

Outputs:

- `data/processed/y_dna/yfull_exports_summary.json` (machine-readable summary)
- `output/private_reports/yfull_exports_summary.md` (human-readable summary)

Both output locations are ignored by git to reduce the risk of accidentally committing personal genetic results.

