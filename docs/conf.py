extensions = [
    "myst_parser",          # allow Markdown
    "sphinx_copybutton",
    "sphinx_design",
]
templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Optional: nicer options
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
}
