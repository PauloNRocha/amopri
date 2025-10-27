"""Pytest configuration helpers."""
from __future__ import annotations

import sys
from pathlib import Path

# Garante que o pacote Django (`amopri`) dentro de backend esteja no PYTHONPATH.
PROJECT_ROOT = Path(__file__).resolve().parent
BACKEND_PATH = PROJECT_ROOT / "backend"
sys.path.insert(0, str(BACKEND_PATH))
