"""Configurazione Sphinx per Improvvisare con la Chitarra."""

import os


project = "Improvvisare con la Chitarra"
author = "Fabrizio's Guitar Space"
copyright = f"2026, {author}"
release = "0.1"

extensions = ["myst_parser"]
myst_enable_extensions = ["attrs_inline"]
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
html_permalinks_icon = "<span>¶</span>"
html_logo = "_static/logo_256.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "globaltoc_expand_depth": 1,
    "youtube_url": "https://youtube.com/@fabsguitarspace",
    "discord_url": "https://discord.gg/DjwCcuS7SA",
    "nav_socials": ["youtube", "discord"],
    "foot_socials": ["youtube", "discord"],
}

epub_title = project
epub_author = author
epub_language = "it"

# XeLaTeX offre un supporto affidabile per gli accenti italiani nel PDF.
latex_engine = "xelatex"
