#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from __future__ import annotations

import os
import sys
from pathlib import Path


def main() -> None:
    """Run administrative tasks."""
    backend_dir = Path(__file__).resolve().parent
    project_root = backend_dir.parent

    for path in (project_root, backend_dir):
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.amopri.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
