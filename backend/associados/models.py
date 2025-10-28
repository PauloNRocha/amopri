"""Models for associados app."""
from __future__ import annotations

import uuid

from django.db import models
from django.utils import timezone


class Member(models.Model):
    """Representa um associado da AMOPRI."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_whatsapp = models.CharField(max_length=30, blank=True, null=True)
    phone_alt = models.CharField(max_length=30, blank=True, null=True)
    address_street = models.CharField(max_length=255, blank=True, null=True)
    address_number = models.CharField(max_length=30, blank=True, null=True)
    address_complement = models.CharField(max_length=100, blank=True, null=True)
    address_district = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    join_date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)
    fee_override = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ("full_name",)

    def __str__(self) -> str:
        return self.full_name


class Plan(models.Model):
    """Configuração de plano padrão para mensalidade."""

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.name} (R$ {self.amount})"


class Invoice(models.Model):
    """Faturas mensais para os associados."""

    class Status(models.TextChoices):
        OPEN = "OPEN", "Aberta"
        PAID = "PAID", "Paga"
        LATE = "LATE", "Atrasada"
        CANCELED = "CANCELED", "Cancelada"

    class Method(models.TextChoices):
        PIX = "PIX", "PIX"
        CASH = "CASH", "Dinheiro"
        BOLETO = "BOLETO", "Boleto"
        CARD = "CARD", "Cartão"
        OTHER = "OTHER", "Outro"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)
    paid_at = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=10, choices=Method.choices, blank=True, null=True)
    external_id = models.CharField(max_length=100, blank=True, null=True)
    pix_txid = models.CharField(max_length=80, blank=True, null=True)
    pix_qrcode = models.TextField(blank=True, null=True)
    boleto_url = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("-due_date", "member__full_name")
        indexes = [models.Index(fields=("member", "due_date"))]

    def mark_paid(self, method: str, when: timezone.datetime | None = None) -> None:
        """Atualiza fatura como paga usando o método informado."""
        self.status = Invoice.Status.PAID
        self.method = method
        self.paid_at = when or timezone.now()
        self.save(update_fields=["status", "method", "paid_at"])

    def __str__(self) -> str:
        return f"{self.member.full_name} – {self.due_date} – R$ {self.amount} ({self.status})"
