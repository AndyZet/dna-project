# Genealogical DNA Analysis Workspace

**Created:** January 10, 2026  
**For:** Andrzej Radzimowski DNA Genealogy Investigation  
**Purpose:** Build production-ready genealogical research workspace with automated DNA analysis

## Quick Start

1. **Install dependencies:**
   ```bash
   bash install_workspace.sh
   ```

2. **Activate virtual environment:**
   ```bash
   source genealogy_env/bin/activate
   ```

3. **Add your data:**
   - Place Y-DNA results in `data/raw/y_dna_results/`
   - Place autosomal DNA in `data/raw/autosomal/`
   - Place GEDCOM files in `data/raw/genealogical/`

4. **Run analysis:**
   ```bash
   python pipeline.py
   ```

5. **Start Jupyter notebooks:**
   ```bash
   jupyter notebook notebooks/
   ```

## Project Structure

- `data/` - Raw and processed data
- `src/` - Python source code modules
- `notebooks/` - Jupyter notebooks for analysis
- `tests/` - Unit tests
- `output/` - Generated reports and visualizations
- `docs/` - Documentation

## Key Features

- Y-DNA haplogroup analysis
- SNP analysis from VCF files
- TMRCA calculations
- Ancient DNA matching (Bodzia, Kievan Rus')
- Genealogical tree parsing and validation
- Migration pattern analysis
- Interactive visualizations

## Documentation

See individual documentation files:
- `SETUP.md` - Detailed setup instructions
- `API_USAGE.md` - API and function documentation
- `HYPOTHESIS_LIST.md` - Research hypotheses
- `RESEARCH_METHODOLOGY.md` - Methodology documentation

## License

This workspace is for personal genealogical research.
