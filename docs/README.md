# DTMF Table Python Documentation

This directory contains the Sphinx documentation for the dtmf_table Python library.

## Structure

```
docs/
├── source/
│   ├── conf.py              # Sphinx configuration
│   ├── index.rst            # Main landing page
│   ├── api.rst              # API reference (auto-generated)
│   ├── _static/             # Static files (CSS, images)
│   └── _templates/          # Custom templates
├── build/                   # Generated documentation (gitignored)
├── Makefile                 # Build commands
└── README.md                # This file
```

## Prerequisites

Make sure the virtual environment is activated and dev dependencies are installed:

```bash
source .venv/bin/activate
uv pip install -e ".[dev]"
```

## Building Locally

### Quick build:

```bash
# From project root
uv run python build_docs.py
```

### Clean build:

```bash
uv run python build_docs.py --clean
```

### Manual build:

```bash
# From docs/ directory
make html
```

Then open `build/html/index.html` in your browser:

```bash
# Linux
xdg-open build/html/index.html

# macOS
open build/html/index.html
```

## Auto-Generated Documentation

The documentation uses Sphinx autodoc to automatically generate API reference from the Python type stubs and docstrings. The type stubs in `python/__init__.pyi` provide comprehensive documentation for all classes and methods.

All docstrings are written in the Rust source code and exposed through PyO3, ensuring the Python documentation stays in sync with the implementation.

## Extensions Used

- `sphinx.ext.autodoc`: Automatic API documentation from docstrings
- `sphinx.ext.autosummary`: Generate summary tables
- `sphinx.ext.napoleon`: Support for Google/NumPy style docstrings
- `sphinx.ext.viewcode`: Add links to highlighted source code
- `sphinx.ext.intersphinx`: Link to other project documentation
- `sphinx_copybutton`: Add copy buttons to code blocks
- `myst_parser`: Support for Markdown files

## Theme

The documentation uses the **Read the Docs** theme (`sphinx_rtd_theme`) for a clean, professional look.

## Deployment

The documentation is deployed to GitHub Pages at:
**https://jmg049.github.io/dtmf_table/**

To deploy, use the deployment script:

```bash
./deploy_docs.sh
```

This script builds the documentation and pushes it to the `gh-pages` branch.

