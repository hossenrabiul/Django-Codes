from django.contrib import admin
from .models import Transaction
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'transaction_type', 'loan_approve']

    def save_Model(self, request, obj, form, change):
        if obj.loan_approve == True:
            obj.account.balance += obj.amount
            obj.balance_after_transactions = obj.account.balance

            obj.account.save()
        super().save_model(request, obj, form, change)