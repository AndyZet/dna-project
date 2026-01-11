# Setup Guide

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (optional, for cloning repositories)

## Installation Steps

### 1. Install Dependencies

Run the installation script:

```bash
bash install_workspace.sh
```

This will:
- Create a Python virtual environment
- Install all required packages
- Download reference data (ISOGG tree)
- Create the database
- Run initial tests

### 2. Manual Installation (Alternative)

If you prefer manual installation:

```bash
# Create virtual environment
python3 -m venv genealogy_env
source genealogy_env/bin/activate

# Install packages
pip install -r requirements.txt

# Create database
python src/database/migrations.py
```

### 3. Download Reference Data

Reference data should be downloaded automatically, but you can download manually:

- **ISOGG Y-DNA Tree:** https://isogg.org/tree/
- **Bodzia Samples:** (Add your source)
- **Kievan Rus' Data:** (Add your source)

Place downloaded files in `data/reference/`

### 4. Add Your Data

Place your data files in the appropriate directories:

- Y-DNA results → `data/raw/y_dna_results/`
- Autosomal DNA → `data/raw/autosomal/`
- GEDCOM files → `data/raw/genealogical/`
- Parish records → `data/raw/genealogical/parish_records/`

## Configuration

Edit configuration files in `config/`:

- `settings.yaml` - General settings
- `database.ini` - Database credentials (if using PostgreSQL)
- `api_keys.env` - API keys for external services

## Verification

Test the installation:

```bash
# Run tests
pytest tests/

# Run pipeline
python pipeline.py
```

## Troubleshooting

### Common Issues

1. **Import errors:** Make sure virtual environment is activated
2. **Missing data files:** Check that reference data is downloaded
3. **Database errors:** Ensure SQLite is available (usually built-in)

### Getting Help

- Check the main guide: `Genealogy_DNA_Workspace_Guide.md`
- Review API documentation: `docs/API_USAGE.md`
- Check error messages for specific issues
