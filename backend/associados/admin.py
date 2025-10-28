from __future__ import annotations

from django.contrib import admin

from .models import Invoice, Member, Plan


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_whatsapp", "email", "is_active", "join_date")
    search_fields = ("full_name", "email", "phone_whatsapp")
    list_filter = ("is_active", "join_date")
    ordering = ("full_name",)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "active")
    list_filter = ("active",)
    ordering = ("name",)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("member", "due_date", "amount", "status", "paid_at", "method")
    list_filter = ("status", "due_date", "method")
    search_fields = ("member__full_name", "external_id", "pix_txid")
    autocomplete_fields = ("member",)
    actions = ("mark_as_paid_cash", "mark_as_canceled")

    @admin.action(description="Marcar selecionadas como PAGAS (Dinheiro)")
    def mark_as_paid_cash(self, request, queryset):
        for invoice in queryset:
            invoice.mark_paid(Invoice.Method.CASH)

    @admin.action(description="Cancelar selecionadas")
    def mark_as_canceled(self, request, queryset):
        queryset.update(status=Invoice.Status.CANCELED)
