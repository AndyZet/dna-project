# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **genealogical DNA analysis workspace** for investigating the Radzimowski family lineage through Y-DNA, autosomal DNA, and historical records. The project focuses on haplogroup I-Y45113 (specifically I-Y224059) and connections to the Bodzia cemetery elite burials, Kievan Rus' populations, and related Polish/Ukrainian families (Garboś, Mazgaj, Berezhnoy, Skory).

**Research Subject:** Andrzej Radzimowski (APR) — Y-DNA haplogroup I-Y224059, YFull sample YF079056.

## Essential Commands

```bash
# Setup and activate environment
bash install_workspace.sh              # First-time setup
source genealogy_env/bin/activate      # Activate virtual environment

# Run analysis
python pipeline.py                     # Full 6-stage analysis pipeline

# Testing
pytest tests/                          # Run all tests
pytest tests/test_y_dna.py -v         # Single test file with verbose output
pytest tests/ -k "haplogroup"          # Run tests matching pattern

# Key standalone scripts
python scripts/generate_bodzia_complete_tree.py   # Dynasty tree with Bodzia connections
python scripts/comprehensive_genetic_analysis.py  # Multi-source genetic analysis
python scripts/analyze_yfull_exports.py           # Process YFull CSV exports
python scripts/analyze_mta_matches.py             # MyTrueAncestry match analysis
```

## Notebook Workflow

The numbered notebooks form a sequential analysis workflow:

1. `01_y_dna_haplogroup_analysis.ipynb` — Y-DNA haplogroup parsing and SNP analysis
2. `02_ancient_dna_matching.ipynb` — Bodzia/Kievan Rus' sample matching
3. `03_migration_analysis.ipynb` — Geographic migration pattern analysis
4. `04_genealogical_tree_validation.ipynb` — GEDCOM parsing and family tree validation
5. `05_visualization_and_reports.ipynb` — Generate visualizations and final reports

Run with: `jupyter notebook notebooks/`

## Architecture

### Pipeline Stages (`pipeline.py`)

The main pipeline orchestrates six sequential stages:
1. Parse ISOGG Y-DNA tree from `data/reference/isogg_y_tree.csv`
2. Analyze SNPs from VCF files via pysam
3. Calculate TMRCA between family branches
4. Parse genealogical GEDCOM records
5. Generate phylogenetic visualizations
6. Store results to SQLite database

### Source Modules (`src/`)

| Module | Purpose |
|--------|---------|
| `y_dna/` | Haplogroup parsing (`haplogroup_parser.py`), SNP analysis via pysam (`snp_analyzer.py`), TMRCA calculations (`tmrca_calculator.py`), Y-STR comparisons (`y_str_comparison.py`) |
| `ancient_dna/` | Bodzia cemetery matching (`bodzia_matcher.py`), Kievan Rus' analysis, admixture estimation |
| `genealogical/` | GEDCOM parsing, parish records, migration analysis, family tree validation |
| `visualization/` | Phylogenetic trees (graphviz/ete3), migration maps (folium/geopandas), report generation |
| `database/` | SQLite/PostgreSQL models, migrations, query helpers |

### Data Flow

```
data/raw/           → Raw DNA files (VCF, YFull CSV, GEDCOM)
data/reference/     → ISOGG tree, Bodzia samples, population refs
      ↓
pipeline.py + src/  → Analysis modules
      ↓
output/             → Visualizations, reports
data/processed/     → SQLite DB (family_tree_normalized.db)
```

### Configuration

`config/settings.yaml` contains:
- Target haplogroup: `I-Y45113`
- TMRCA mutation rate: `0.00069` per generation (25 years)
- Dynasty color schemes for Bodzia diagrams (Rurikid, Piast, Premyslid, etc.)
- Visualization settings (graphviz engine, output formats)

## Research Context

### Hypothesis Tracking

Research hypotheses are tracked in `docs/HYPOTHESIS_LIST.md` with:
- Confidence ratings (percentage)
- Evidence requirements
- Testable predictions
- Last review dates

### Key Genetic Connections

| Person | Haplogroup | YFull Sample | TMRCA |
|--------|------------|--------------|-------|
| Andrzej (APR) | I-Y224059 | YF079056 | — |
| Artur Garboś | I-Y224059 | YF089989 | ~700 ybp |
| Aleksei Berezhnoy | I-Y45233 | — | ~1050 ybp |
| VK157 (Bodzia) | I-S2077 | ancient | ancestral |

### Y-DNA Files

Located in `data/raw/y_dna_results/`:
- `SNP_for_YF079056_*.csv` — SNP calls from YFull
- `STR_for_YF079056_*.csv` — Y-STR marker values
- `SNP_matches_for_YF079056.csv` — YFull matching samples

## Hypothesis Workflow

Research progress is tracked through `docs/HYPOTHESIS_LIST.md` — the central document for all research claims. When working with hypotheses:

1. **Adding new hypotheses**: Follow the existing format (H#.# numbering, Status/Confidence/Priority fields, Evidence Required, Verification Steps)
2. **Updating confidence**: Adjust percentage based on new evidence; document the change in "Last Updated" field
3. **Cross-referencing**: Link related hypotheses (e.g., RA.1→RA.3) when evidence supports multiple claims

### Data Quality Tiers

When citing genetic evidence, use the three-tier quality system:

| Tier | Source Type | Usage |
|------|-------------|-------|
| **Published** ✅ | Peer-reviewed papers, YFull haplogroups | Phylogenetic claims, kinship analysis |
| **Exploratory** ⚠️ | Facebook G25, community datasets | Affinity comparisons, hypothesis generation |
| **Provisional** ⚠️ | MyTrueAncestry cM, preliminary analysis | Hypothesis generation only |

### Key Documentation Files

| File | Purpose |
|------|---------|
| `docs/HYPOTHESIS_LIST.md` | Master hypothesis tracker (33+ hypotheses, tiered by confidence) |
| `docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md` | Comprehensive Bodzia cemetery analysis (v2.3) |
| `docs/BODZIA_HYPOTHESIS_FOR_PRESENTATION.md` | NotebookLM presentation version (v1.1) |
| `docs/VK155_VK157_BURIAL_HYPOTHESIS.md` | Burial structure and untested female analysis |

## Code Style

- Python 3.10+ with type hints
- PEP 8 with 4-space indentation
- `snake_case` for functions/variables, `PascalCase` for classes
- No formatter configured; keep diffs clean
- Tests: pytest with `test_*.py` naming

## Key Individuals Reference

| Code | Name | Haplogroup | YFull Kit | Notes |
|------|------|------------|-----------|-------|
| APR | Andrzej Radzimowski | I-Y224059 | YF079056 | Research subject |
| VK157 | Bodzia Elite Male | I-S2077 (ancestral I-Y45113) | ancient | Proposed Sviatopolk I |
| VK155 | Bodzia Female | — (mtDNA H1c) | ancient | VK157's maternal relative |
| Artur | Artur Garboś | I-Y224059 | YF089989 | MDA Józef Garboś b.1710 |
| Aleksei | Aleksei Berezhnoy | I-Y45233 | — | Sister branch under I-Y45113 |
