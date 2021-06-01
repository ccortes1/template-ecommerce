"""Invoices model."""

# Django
from django.db import models

# Utilities
from utils.models import BasicModel

class Invoice(BasicModel):
    """Invoice model"""
    client = models.ForeignKey('users.User', on_delete=models.CASCADE)
    total_invoice_value = models.PositiveIntegerField()

    class Meta(BasicModel.Meta):
        db_table = "invoice"

class items_on_invoice(BasicModel):
    """items on invoice
    this table is used for connecting
    the invoices table with products table
    """
    invoice = models.OneToOneField('Invoice', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    sold_units = models.PositiveIntegerField()
    total_value = models.PositiveIntegerField()

    class Meta(BasicModel.Meta):
        db_table = "items_on_invoice"

