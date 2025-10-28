"""Smoke tests for associados app."""
from __future__ import annotations

import django
from django.apps import apps


def test_associados_app_is_registered() -> None:
    """Ensure the associados app is available in Django registry."""
    if not django.apps.apps.ready:
        django.setup()
    config = apps.get_app_config("associados")
    assert config.name == "associados"
