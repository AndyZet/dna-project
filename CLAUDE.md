# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **genealogical DNA analysis workspace** for investigating the Radzimowski family lineage through Y-DNA, autosomal DNA, and historical records. The project focuses on haplogroup I-Y45113 (specifically I-Y224059) and connections to the Bodzia cemetery elite burials, Kievan Rus' populations, and related Polish/Ukrainian families (Garboś, Mazgaj, Berezhnoy, Skory).

## Essential Commands

```bash
# Setup and activate environment
bash install_workspace.sh              # First-time setup
source genealogy_env/bin/activate      # Activate virtual environment

# Run analysis
python pipeline.py                     # Full analysis pipeline
jupyter notebook notebooks/            # Interactive analysis

# Testing
pytest tests/                          # Run all tests
pytest tests/test_y_dna.py            # Run specific test file

# Standalone scripts (from project root)
python scripts/analyze_yfull_exports.py
python scripts/comprehensive_genetic_analysis.py
python scripts/generate_bodzia_complete_tree.py
```

## Architecture

### Source Modules (`src/`)

| Module | Purpose |
|--------|---------|
| `y_dna/` | Y-DNA analysis: haplogroup parsing (ISOGG tree), SNP analysis (VCF files via pysam), TMRCA calculations, Y-STR comparisons, YFull data exports |
| `ancient_dna/` | Matching against ancient DNA samples (Bodzia cemetery, Kievan Rus' populations) |
| `genealogical/` | GEDCOM parsing, family tree data handling |
| `visualization/` | Phylogenetic trees (graphviz/ete3), migration maps (folium/geopandas), charts |
| `database/` | SQLite/PostgreSQL storage for analysis results |

### Data Flow

1. **Raw data** (`data/raw/`) → Y-DNA results (VCF, CSV from YFull), autosomal DNA, GEDCOM files
2. **Reference data** (`data/reference/`) → ISOGG Y-DNA tree, Bodzia samples, population references
3. **Processing** → `pipeline.py` orchestrates analysis through `src/` modules
4. **Output** (`output/`) → Visualizations, reports, database

### Key Configuration

- `config/settings.yaml` — Analysis parameters including target haplogroup (I-Y45113), mutation rates, visualization settings, dynasty color schemes for Bodzia diagrams
- Database defaults to SQLite at `data/processed/family_tree_normalized.db`

## Research Context

The workspace tracks research hypotheses in `docs/HYPOTHESIS_LIST.md` with confidence ratings and evidence requirements. Key genetic connections being investigated:

- **Andrzej (APR)**: I-Y224059 (YFull sample YF079056)
- **Artur Garboś**: I-Y224059 (YFull sample YF089989) — TMRCA ~700 ybp
- **Aleksei Berezhnoy**: I-Y45233 (sister branch under I-Y45113) — TMRCA ~1050 ybp
- **VK157 (Bodzia)**: Ancient Viking-era burial, haplogroup I-S2077 (ancestral to I-Y45113)

## Working with DNA Data

### Y-DNA Files (in `data/raw/y_dna_results/`)
- `SNP_for_YF079056_*.csv` — SNP calls from YFull
- `STR_for_YF079056_*.csv` — Y-STR marker values
- `SNP_matches_for_YF079056.csv` — YFull matching samples
- VCF files for raw variant data

### Key Analysis Scripts
- `scripts/generate_bodzia_complete_tree.py` — Comprehensive dynasty tree with Bodzia connections
- `scripts/comprehensive_genetic_analysis.py` — Multi-source genetic analysis
- `scripts/analyze_yfull_exports.py` — Process YFull export data

## Python Conventions

- Python 3.10+ with type hints
- Modules use pysam for VCF handling, biopython for sequences, pandas for tabular data
- Visualization via matplotlib/seaborn (static) and plotly/folium (interactive)
- Tests use pytest, located in `tests/test_*.py`

## Documentation

Research documentation lives in `docs/`:
- `HYPOTHESIS_LIST.md` — Tracked research hypotheses with confidence ratings
- `BODZIA_*.md` — Bodzia cemetery analysis and connections
- `YFULL_WORKFLOW.md` — YFull data processing procedures
- `Academic Papers/` — Source materials organization
