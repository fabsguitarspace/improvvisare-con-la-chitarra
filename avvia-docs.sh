#!/usr/bin/env sh
set -eu

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
VENV_DIR="$PROJECT_DIR/.venv"

if [ ! -x "$VENV_DIR/bin/python" ]; then
    python3 -m venv "$VENV_DIR"
fi

if [ ! -x "$VENV_DIR/bin/sphinx-autobuild" ]; then
    "$VENV_DIR/bin/python" -m pip install -r "$PROJECT_DIR/requirements-docs.txt"
fi

exec "$VENV_DIR/bin/sphinx-autobuild" \
    --host 127.0.0.1 \
    --open-browser \
    "$PROJECT_DIR/Docs" \
    "$PROJECT_DIR/_build/html"
