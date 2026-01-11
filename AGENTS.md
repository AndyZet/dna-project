# Repository Guidelines

## Project Structure & Module Organization
- `src/` holds Python packages for analysis (e.g., `y_dna/`, `ancient_dna/`, `genealogical/`, `visualization/`, `database/`).
- `data/` stores raw inputs and processed outputs (`data/raw/`, `data/processed/`, `data/reference/`). Place personal DNA files under the appropriate `data/raw/*` subfolder.
- `tests/` contains pytest suites (`tests/test_*.py`).
- `notebooks/` contains Jupyter analysis notebooks. `output/` stores generated reports/figures.
- `config/` contains runtime settings (e.g., `config/settings.yaml`).

## Build, Test, and Development Commands
- `bash install_workspace.sh` — sets up the virtualenv, installs dependencies, pulls reference data, and runs initial tests.
- `source genealogy_env/bin/activate` — activates the local virtual environment created by the install script.
- `pip install -r requirements.txt` — manual dependency install (use if you skip the script).
- `python pipeline.py` — runs the end-to-end analysis pipeline.
- `jupyter notebook notebooks/` — launches notebook exploration.
- `pytest tests/` — runs the test suite.

## Coding Style & Naming Conventions
- Python 3.10+ codebase; follow PEP 8 with 4-space indentation.
- Use `snake_case` for functions/variables, `PascalCase` for classes, and `UPPER_SNAKE_CASE` for constants.
- Keep modules small and domain-focused (e.g., Y-DNA logic in `src/y_dna/`).
- No formatter/linter is configured; keep diffs clean and consistent.

## Testing Guidelines
- Tests use `pytest` (see `tests/`). Name files `tests/test_*.py` and tests `test_*`.
- Add focused unit tests for new parsing, matching, or visualization logic.
- Run `pytest tests/` before sharing changes.

## Commit & Pull Request Guidelines
- No git history is present in this workspace; no established commit-message convention exists yet.
- If you add git history, use concise imperative subjects (e.g., "Add haplogroup parser") and one logical change per commit.
- PRs should include: a short summary, testing results, and notes on any new data/reference files. Include screenshots for visualization changes when applicable.

## Configuration & Data Handling
- Update `config/settings.yaml` for local settings; keep secrets out of versioned files.
- Store API keys in a local, untracked file (e.g., `config/api_keys.env`) and avoid committing personal DNA data.
