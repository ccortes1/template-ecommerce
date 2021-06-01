"""Product admin."""

# Django
from django.contrib import admin

# Model
from products.models import Product, Category, Label

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin"""
    list_display = (
        'name',
        'category',
        'price',
        'brand',
        'unidades_disponibles',
        'description',
        'picture',
        'created',
        'modified'
    )
    
    search_fields = (
        'name',
        'category',
        'label',
        'brand',
        'unidades_disponibles'
        )

    list_filter = (
        'category',
        'label',
        'price',
        'brand',
        'created',
        'modified'
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'modified'
    )
    search_field = ('name',  'created')
    list_filter = ('name',  'created')


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'modified'
    )
    search_field = ('name',  'created')
    list_filter = ('name',  'created')
