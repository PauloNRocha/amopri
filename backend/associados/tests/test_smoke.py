"""Smoke tests for associados app."""
from __future__ import annotations

import pytest
from django.apps import apps

pytestmark = pytest.mark.django_db


def test_associados_app_is_registered() -> None:
    """Ensure the associados app is available in Django registry."""
    config = apps.get_app_config("associados")
    assert config.name == "backend.associados"


def test_invoice_mark_paid_sets_fields() -> None:
    """Invoice.mark_paid atualiza status e pagamento."""
    from datetime import date
    from decimal import Decimal

    from backend.associados.models import Invoice, Member, Plan

    member = Member.objects.create(full_name="Fulano da Silva")
    plan = Plan.objects.create(name="Mensalidade", amount=Decimal("30.00"))
    invoice = Invoice.objects.create(
        member=member,
        due_date=date.today(),
        amount=plan.amount,
    )

    invoice.mark_paid(Invoice.Method.CASH)

    invoice.refresh_from_db()
    assert invoice.status == Invoice.Status.PAID
    assert invoice.method == Invoice.Method.CASH
    assert invoice.paid_at is not None
