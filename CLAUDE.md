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
python scripts/generate_bodzia_complete_tree.py   # Dynasty tree → output/visualizations/
python scripts/comprehensive_genetic_analysis.py  # Multi-source → output/reports/
python scripts/analyze_yfull_exports.py           # Requires data/raw/y_dna_results/SNP_for_YF*.csv
python scripts/analyze_mta_matches.py             # Requires data/raw/autosomal/MTA/*/matchesMTA.md
python scripts/generate_bodzia_full_tree.py       # Extended tree → output/visualizations/
python scripts/generate_dna_visualizations.py     # General → output/visualizations/
python scripts/generate_dtree_visualization.py    # D-tree JSON → output/web/
python scripts/generate_genealogy_tree.py         # Graphviz → output/visualizations/
```

### BAM to GedMatch Conversion

**Prerequisites:** `bcftools`, `samtools`, `plink` (install via Homebrew or download PLINK 1.9 binary to `~/bin/`)

```bash
# First-time setup: downloads ~19GB reference data (GRCh37 + dbSNP b151)
bash scripts/setup_bam_conversion.sh

# Convert single BAM → 23andMe format for GedMatch upload
bash scripts/convert_bam_to_gedmatch.sh input.bam

# Output: output/gedmatch/{sample}_23andme.txt
```

**Reference data locations (after setup):**
- `data/reference/genomes/human_g1k_v37.fasta` — GRCh37 reference genome (3.1 GB)
- `data/reference/dbsnp/All_20180423.vcf.gz` — dbSNP b151 (15.7 GB, tabix-indexed)

**External BAM files:** Priority Bodzia samples (VK155.final.bam, VK157.final.bam) on `/Volumes/T7 Touch/Downloads/drive.usercontent.google.com/`

**Google Colab alternative** (no local bioinformatics tools needed):
- `notebooks/BAM_to_GedMatch_Colab.ipynb` — Single sample conversion
- `notebooks/BAM_to_GedMatch_Batch.ipynb` — Auto-discover and batch process all Drive BAMs

**Critical workflow note:** The conversion script handles chromosome naming mismatches automatically (`1` → `chr1` for dbSNP annotation, then back to numeric for PLINK). If annotation rates are unexpectedly low (<50%), verify the dbSNP VCF uses `chr`-prefixed chromosomes.

### SuperKit Creation (Modern DNA Merging)

Merge multiple consumer DNA test files into a maximized SNP set:

```bash
python scripts/create_superkit.py
# Output: APR_SuperKit_Combined.txt (~1.17M SNPs from 3 sources)
```

Input file formats supported:
- **23andMe:** `rsid\tchrom\tpos\tgenotype` (tab-separated, # comments)
- **AncestryDNA:** `rsid\tchrom\tpos\tallele1\tallele2` (tab-separated)
- **MyHeritage:** CSV with `RSID,CHROMOSOME,POSITION,RESULT` columns

The merger uses first-seen priority (23andMe → AncestryDNA → MyHeritage) and outputs 23andMe format compatible with GEDmatch, MyTrueAncestry, and DNA.Land.

## Module Import Pattern

When importing from `src/`, scripts use path insertion:
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from y_dna.haplogroup_parser import parse_isogg_tree
```

For interactive REPL or notebooks, run from project root with venv activated.

## Notebook Workflow

The numbered notebooks form a sequential analysis workflow:

1. `01_y_dna_haplogroup_analysis.ipynb` — Y-DNA haplogroup parsing and SNP analysis
2. `02_ancient_dna_matching.ipynb` — Bodzia/Kievan Rus' sample matching
3. `03_migration_analysis.ipynb` — Geographic migration pattern analysis
4. `04_genealogical_tree_validation.ipynb` — GEDCOM parsing and family tree validation
5. `05_visualization_and_reports.ipynb` — Generate visualizations and final reports

**Google Colab Notebooks** (for BAM processing without local tools):
- `BAM_to_GedMatch_Colab.ipynb` — Single-sample BAM→23andMe conversion
- `BAM_to_GedMatch_Batch.ipynb` — Auto-discover and batch process all Drive BAMs

Run local notebooks with: `jupyter notebook notebooks/`

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
| `ancient_dna/` | Bodzia matching (`bodzia_matcher.py`), Kievan Rus' analysis (`kievan_rus_analysis.py`), G25 coordinates (`g25_analyzer.py` — Euclidean distance on 25-dim PCA vectors), PCA (`pca_analyzer.py`), MTA parsing (`mta_parser.py` — parses `matchesMTA.md` files, `mta_analyzer.py`), admixture models (`admixture_estimator.py`) |
| `genealogical/` | GEDCOM parsing (`gedcom_parser.py`), parish records (`parish_records.py`), migration analysis (`migration_analyzer.py`), family tree validation (`family_tree_validator.py`) |
| `visualization/` | Phylogenetic trees (`phylogenetic_trees.py` — graphviz/ete3), family trees (`family_trees.py`), migration maps (`migration_maps.py` — folium/geopandas), report generation (`report_generator.py`) |
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

### Y-STR Distance Calculations

The `y_str_comparison.py` module uses **Manhattan distance** (cityblock) for Y-STR profile comparisons, with **Ward's method** for hierarchical clustering. This matches the standard approach in genetic genealogy where each STR step difference is counted equally.

Key distance thresholds (from YFull data):
- **0-7 STRs:** Close match (same I-Y224059 branch)
- **8-15 STRs:** Related branch (I-Y45113 umbrella)
- **15+ STRs:** Distant or unrelated

### Ancient DNA Quality — Actual Results (January 2026)

Bodzia samples converted locally via `scripts/convert_bam_to_gedmatch.sh`:

| Sample | SNP Count | File Size | GedMatch Usability |
|--------|----------|-----------|-------------------|
| **VK157** (elite male) | ~617K | 15 MB | Full functionality — rivals modern tests |
| **VK155** (female) | ~75K | 1.8 MB | Population analysis, admixture, MTA matches |
| VK158 | ~2K | 62 KB | Too low — haplogroup only |

VK157's exceptional yield (~1M raw variants, 62.9% annotation rate) makes it suitable for GEDmatch one-to-many comparisons and MyTrueAncestry Deep Dive analysis.

**Reference thresholds:**
- **600K+ SNPs:** Modern consumer test quality — full GEDmatch functionality
- **200K+ SNPs:** Good ancient DNA — reliable population matching
- **50K-100K SNPs:** Minimum viable — admixture/Oracle analysis only
- **<50K SNPs:** Below threshold — limited to haplogroup determination

## Research Context

### Y-DNA Files

Located in `data/raw/y_dna_results/`:
- `SNP_for_YF079056_*.csv` — SNP calls from YFull (positive/negative/no-call)
- `STR_for_YF079056_*.csv` — Y-STR marker values (DYS series)
- `SNP_matches_for_YF079056.csv` — YFull matching samples with distances
- `NovelSNP_for_YF079056_*.csv` — Novel (private) SNP discoveries
- `STR_statistic_for_YF079056.csv` — Private mutation flags per branch

**File naming convention:** `{Type}_for_{YFullKit}_{YYYYMMDD}.csv` where YFullKit is `YF######`.

### FamilyTreeDNA Integration

See `docs/FTDNA.md` for centralized kit registry, test statuses, and naming conventions.

**Critical naming difference:** FTDNA and YFull use different prefixes for the same SNPs:
- FTDNA: `I-FTC2520` (FTC = FamilyTreeDNA Commercial)
- YFull: `I-Y224059` (Y = YFull nomenclature)

These refer to the **same terminal SNP** — always cross-reference when comparing data sources.

## Hypothesis Workflow

Research progress is tracked through `docs/HYPOTHESIS_LIST.md` — the central document for all research claims (33+ hypotheses, tiered by confidence).

**Adding/updating hypotheses:**
- Follow existing format: H#.# numbering, Status/Confidence/Priority fields
- Adjust confidence percentages based on new evidence; update "Last Updated" field
- Cross-reference related hypotheses (e.g., RA.1→RA.3) when evidence supports multiple claims

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
| `docs/FTDNA.md` | FamilyTreeDNA kit registry and Z63 project data |
| `docs/MTA.md` | MyTrueAncestry autosomal match results |
| `docs/HYPOTHESIS_SKORY.md` | Doug Skory Big Y-700 persuasion strategy |

## Autosomal DNA Data

### G25 Coordinates
Located in `data/raw/autosomal/MTA/`:
- `VK155/vk155_G25.txt` — Bodzia female G25 coordinates
- `VK157/vk157_G25.txt` — Bodzia elite male G25 coordinates
- `*/matchesMTA.md` — MyTrueAncestry match summaries

G25 coordinates are 25-dimensional PCA vectors used for population affinity comparisons. The `G25Analyzer` class in `src/ancient_dna/g25_analyzer.py` provides:
- `parse_g25_file()` — Load CSV coordinates (format: `sample_id,coord1,...,coord25`)
- `calculate_distance()` — Euclidean distance between samples
- `find_closest_references()` — Match sample against reference populations

Process admixture models with `src/ancient_dna/admixture_estimator.py`.

### MTA Match Parser

The `MTAParser` class in `src/ancient_dna/mta_parser.py` parses `matchesMTA.md` files to extract:
- Top matches with genetic distances and percentiles
- Deep Dive results with shared DNA segments (cM, SNP chains)
- Era categorization (Mesolithic through Post-Medieval)
- Region extraction (Poland, Sweden, Ukraine, etc.)

Use `parser.parse_both_files(vk155_path, vk157_path)` to compare VK155/VK157 results simultaneously.

### Processed Ancient DNA
Located in `data/processed/ancient_dna/`:
- `g25_comparison.json` — G25 distance calculations
- `admixture_comparison.json` — Admixture model results
- `pca_results.json` — PCA projections
- `genetic_profiles.json` — Consolidated genetic profiles

## MCP Integration

A Google Drive MCP server is configured in `.mcp.json` for programmatic access to cloud-stored BAM files and research data. Available tools:
- `gdrive_search` — Search Drive by filename/content
- `gdrive_read_file` — Retrieve file content by ID (binary files base64-encoded)

### Google Drive Organization

DNA research files are organized in `01_Projects/DNA_Genealogy/` with four workflow stages:
```
01-Raw_Data_Imports/     # BAM files, YFull exports, GEDCOM
02-Working_Analysis/     # GedMatch conversions, G25 calculations
03-Documentation_Reports/# Hypothesis evaluations, presentations
04-Historical_Pedigree/  # Genealogical records, parish documents
```

Key BAM files (Bodzia samples) are located in Drive and can be batch-processed via `notebooks/BAM_to_GedMatch_Batch.ipynb` which auto-discovers all `.final.bam` files.

## Code Style

- Python 3.10+ with type hints
- PEP 8 with 4-space indentation
- `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants
- No formatter configured; keep diffs clean
- Tests: pytest with `test_*.py` naming; run `pytest tests/` before sharing changes

## Git Guidelines

No enforced commit conventions; use concise imperative subjects (e.g., "Add haplogroup parser") and one logical change per commit. PRs should include a short summary, testing results, and notes on any new data/reference files.

## Key Individuals Reference

| Code | Name | Haplogroup | YFull Kit | TMRCA | Notes |
|------|------|------------|-----------|-------|-------|
| APR | Andrzej Radzimowski | I-Y224059 | YF079056 | — | Research subject |
| Artur | Artur Garboś | I-Y224059 | YF089989 | ~700 ybp | MDA Józef Garboś b.1710 |
| Aleksei | Aleksei Berezhnoy | I-Y45233 | — | ~1050 ybp | Sister branch under I-Y45113 |
| VK157 | Bodzia Elite Male | I-S2077 (ancestral) | ancient | — | Proposed Sviatopolk I; 617K SNPs converted |
| VK155 | Bodzia Female | — (mtDNA H1c) | ancient | — | VK157's maternal relative; 75K SNPs |
| VK542 | Kievan Rus' Male | N-Y16323 | ancient | — | Proposed Gleb (VK157's ½ brother) |
| Doug | Doug Skory | I-Y45113 (pending) | — | — | Big Y-700 unfunded since Feb 2022 |
| Wladyslaw | Wladyslaw Mazgaj | I-Y45113 (pending) | — | — | Y111 distance 10 from Aleksei |

**GEDmatch-ready files:** `output/gedmatch/VK155_23andme.txt`, `output/gedmatch/VK157_23andme.txt`
