"""Pytest configuration helpers."""
from __future__ import annotations

import sys
from pathlib import Path

try:  # pytest-django pode não estar instalado em ambientes mínimos
    import pytest_django  # type: ignore  # noqa: F401
except ImportError:
    pytest_plugins = []
else:
    pytest_plugins = ["pytest_django"]

# Garante que o pacote Django esteja disponível para importação nos testes.
PROJECT_ROOT = Path(__file__).resolve().parent
BACKEND_PATH = PROJECT_ROOT / "backend"

for path in (PROJECT_ROOT, BACKEND_PATH):
    if path.exists():
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)
