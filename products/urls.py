"""Post URLs."""

# Django
from django.urls import path

# Views
from products import views

urlpatterns = [
    path(
        route='',
        view=views.CatalogView.as_view(),
        name='catalog'
    )
]