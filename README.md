# Genealogical DNA Analysis Workspace

**Created:** January 10, 2026  
**For:** Andrzej Radzimowski DNA Genealogy Investigation  
**Purpose:** Production-ready genealogical research workspace with automated DNA analysis

## Quick Start

1. **Install the workspace:**
   ```bash
   bash install_workspace.sh
   ```

2. **Activate the virtual environment:**
   ```bash
   source genealogy_env/bin/activate
   ```

3. **Add your data:**
   - Place Y-DNA results in `data/raw/y_dna_results/`
   - Place autosomal DNA in `data/raw/autosomal/`
   - Place GEDCOM files in `data/raw/genealogical/`

4. **Run the analysis pipeline:**
   ```bash
   python pipeline.py
   ```

5. **Start Jupyter notebooks:**
   ```bash
   jupyter notebook notebooks/
   ```

## Project Structure

```
genealogy-workspace/
├── data/              # Raw and processed data
│   ├── raw/           # Original data files
│   ├── processed/     # Processed/cleaned data
│   └── reference/     # Reference datasets (ISOGG tree, etc.)
├── src/               # Python source code
│   ├── y_dna/         # Y-DNA analysis modules
│   ├── ancient_dna/   # Ancient DNA matching
│   ├── genealogical/  # Genealogical data handling
│   ├── visualization/ # Visualization tools
│   └── database/      # Database models and queries
├── notebooks/         # Jupyter notebooks for analysis
├── tests/             # Unit tests
├── output/            # Generated reports and visualizations
├── config/            # Configuration files
└── docs/              # Documentation
```

## Key Features

- **Y-DNA Analysis:** Haplogroup assignment, SNP analysis, TMRCA calculations
- **Ancient DNA Matching:** Bodzia cemetery, Kievan Rus' populations
- **Genealogical Tools:** GEDCOM parsing, family tree validation
- **Visualization:** Phylogenetic trees, migration maps, interactive charts
- **Database:** SQLite/PostgreSQL support for storing results

## Documentation

- **[Setup Guide](docs/SETUP.md)** - Detailed installation instructions
- **[API Usage](docs/API_USAGE.md)** - Function and module documentation
- **[Hypothesis List](docs/HYPOTHESIS_LIST.md)** - Research hypotheses tracking
- **[Research Methodology](docs/RESEARCH_METHODOLOGY.md)** - Analysis methodology

## Requirements

- Python 3.10+
- See `requirements.txt` for full dependency list

## Installation

The workspace includes an automated installation script:

```bash
bash install_workspace.sh
```

This will:
- Create a Python virtual environment
- Install all required packages
- Download reference data (ISOGG tree)
- Create the database
- Run initial tests

## Usage Examples

### Y-DNA Haplogroup Analysis

```python
from src.y_dna.haplogroup_parser import parse_isogg_tree, find_haplogroup

tree = parse_isogg_tree('data/reference/isogg_y_tree.csv')
haplogroup = find_haplogroup(tree, 'I-Y45113')
```

### Ancient DNA Matching

```python
from src.ancient_dna.bodzia_matcher import match_bodzia_samples

matches = match_bodzia_samples(
    your_dna='data/raw/autosomal/mytrueancestry_results.json',
    bodzia_samples='data/reference/bodzia_samples.csv'
)
```

### Genealogical Tree Parsing

```python
from src.genealogical.gedcom_parser import parse_family_tree

tree = parse_family_tree('data/raw/genealogical/family_tree.ged')
```

## Next Steps

1. Add your DNA test results to `data/raw/`
2. Download reference data (ISOGG tree, Bodzia samples)
3. Run the analysis pipeline: `python pipeline.py`
4. Explore the Jupyter notebooks in `notebooks/`
5. Review and update hypotheses in `docs/HYPOTHESIS_LIST.md`

## License

This workspace is for personal genealogical research.

## Support

For questions or issues, refer to:
- Main guide: `Genealogy_DNA_Workspace_Guide.md`
- API documentation: `docs/API_USAGE.md`
- Setup guide: `docs/SETUP.md`
