from django.shortcuts import render, get_object_or_404
from apps.categories.models import Category
from .models import Product

def catalog_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    products = Product.objects.filter(
        category=category,
        is_active=True
    ).select_related("brand")

    return render(request, "pages/catalog.html", {
        "category": category,
        "products": products
    })
