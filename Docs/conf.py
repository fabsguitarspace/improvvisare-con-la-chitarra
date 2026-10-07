"""Configurazione Sphinx per Improvvisare con la Chitarra."""

import os


project = "Improvvisare con la Chitarra"
author = ""
copyright = "2026"
release = "0.1"

extensions = ["myst_parser"]
source_suffix = {".md": "markdown"}
root_doc = "index"
language = "it"

exclude_patterns = [
    "_build",
    "adr/**",  # Le ADR guidano lo sviluppo e non fanno parte del libro.
    "Thumbs.db",
    ".DS_Store",
]

html_theme = "shibuya"
html_title = project
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")
html_theme_options = {
    "globaltoc_expand_depth": 1,
}

epub_title = project
epub_language = "it"

# XeLaTeX offre un supporto affidabile per gli accenti italiani nel PDF.
latex_engine = "xelatex"
