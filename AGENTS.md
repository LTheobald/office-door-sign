# Repository Guidelines

## Project Structure & Module Organization
Target a conventional Python layout. Place application packages in `src/office_sign/` so imports remain explicit and tooling can resolve modules cleanly. Mirror that structure in `tests/` (for example, `tests/test_display.py` covers `src/office_sign/display.py`). Keep reusable sign assets—SVG templates, fonts, sample schedules—in `assets/`. Temporary notebooks or scratch scripts belong in `sandbox/` and stay out of commits. The `.venv/` directory is intentionally excluded; recreate it locally rather than checking it in.

## Build, Test, and Development Commands
Create or refresh the virtual environment with `python -m venv .venv` and activate it via `source .venv/bin/activate` (PowerShell users can run `.venv\\Scripts\\Activate.ps1`). Install dependencies with `pip install -r requirements.txt` and optional tooling via `pip install -r requirements-dev.txt` when introduced. Run the application entry point with `python -m office_sign.app` (adjust the module path to match the file you are working on). Execute the test suite using `pytest` or `pytest tests -q` for a fast signal.

## Coding Style & Naming Conventions
Adopt Black formatting (see `.idea/Black` configuration) and run `black src tests` before committing. Use four-space indentation, snake_case for functions and modules, and PascalCase for classes. Prefix private helpers with a leading underscore and group related constants inside dedicated modules such as `src/office_sign/constants.py`. Prefer descriptive docstrings, and include type hints for all public functions to simplify static analysis.

## Testing Guidelines
Write unit tests with pytest fixtures, keeping one test module per source module. Name tests using `test_<scenario>_<expected>()` so failures stay readable. When adding new behaviour, add regression tests first; target at least one integration-style test per feature flag or API facade. Run `pytest --cov=src --cov-report=term-missing` before submitting a pull request and ensure no warnings leak into CI output.

## Commit & Pull Request Guidelines
Use present-tense, imperative commit subjects of ~50 characters (e.g., "Add door status polling service"). Group related changes, rebasing if necessary to keep history linear. Pull requests should describe the motivation, list functional changes, call out testing performed, and link any issue tracker references. Include screenshots or terminal snippets whenever the sign output or system behaviour changes so reviewers can verify intent quickly.
