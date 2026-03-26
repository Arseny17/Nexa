from django.urls import path
from .views import catalog_by_category

urlpatterns = [
    path("<slug:slug>/", catalog_by_category, name="catalog_by_category"),
]
