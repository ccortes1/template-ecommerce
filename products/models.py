"""Products model."""

# Django
from django.db import models

# Utilities
from utils.models import BasicModel


class Product(BasicModel):
    """Product model."""
    name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    label = models.ManyToManyField('Label', db_table='product_label')
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=100, blank=False)
    unidades_disponibles = models.PositiveIntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='products/picture', blank=False)

    class Meta(BasicModel.Meta):
        db_table = "product"


class Category(BasicModel):
    """Category models."""
    name = models.CharField(max_length=50, blank=False)

    class Meta(BasicModel.Meta):
        db_table = "category"

    def __str__(self):
        """Return category name"""
        return self.name


class Label(BasicModel):
    """Label model."""
    name = models.CharField(max_length=50, blank=False)

    class Meta(BasicModel.Meta):
        db_table = 'label'
    
    def __str__(self):
        """Return label name"""
        return self.name
