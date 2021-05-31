"""Products model."""

# Django
from django.db import models

# Utilities
from utils.models import BasicModel


class Product(models.Model, BasicModel):
    """Product model."""
    name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    label = models.ManyToManyField('Label', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=100, blank=False)
    unidades_disponibles = models.PositiveIntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='products/picture', blank=False)


class Category(models.Model):
    """Category models."""
    name = models.CharField(max_length=50, blank=False)

class Label(models.Model):
    """Label model."""
    name = models.CharField(max_length=50, blank=False)
