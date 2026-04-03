from django.urls import path
from .views import catalog_view, product_view

urlpatterns = [
    path("", catalog_view, name="catalog"),
    path("product/<slug:slug>/", product_view, name="product"),
    path("<slug:slug>/", catalog_view, name="catalog_by_category"),
]
