"""Products views"""

# Django

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Models
from products.models import Product, Category

class CatalogView(ListView):
    """Return all products on DB"""

    template_name = 'products/catalog.html'
    model = Product
    ordering = ('-modified',)
    paginate_by = 30
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        #context['products'] = self.request.product
        return context
