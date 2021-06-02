"""Products views"""

# Django

from django.shortcut import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateViews, DetailView, ListView

# Models
from products.models import Product

class CatalogView(ListView):
    """Return all products on DB"""

    template_name = 'products/catalog.html'
    models = Product
    ordering = ('-modified',)
    paginate_by = 30
    context_object_name = 'post'