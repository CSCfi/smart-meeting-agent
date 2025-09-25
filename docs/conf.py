from datetime import date
from pathlib import Path
import sys

# Make the repo root importable so autodoc can find your modules
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

project = "Smart Meeting Agent"
author = "CSCfi"
year = date.today().year
copyright = f"{year}, {author}"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
]

autosummary_generate = True
autodoc_typehints = "description"
templates_path = ["_templates"]
exclude_patterns = []

html_theme = "furo"
html_static_path = ["_static"]

# MyST (Markdown) options
myst_enable_extensions = [
    "colon_fence",
    "attrs_block",
    "deflist",
    "linkify",
]

# Link to Python stdlib docs
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
}
