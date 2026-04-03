from django.shortcuts import render, get_object_or_404
from apps.categories.models import Category
from apps.catalog.models import Product

def catalog_view(request, slug=None):
    categories = Category.objects.all()

    if slug:
        current_category = get_object_or_404(Category, slug=slug)

        products = Product.objects.filter(
            category=current_category,
            is_active=True
        ).prefetch_related("images")

        for product in products:
            product.main_image = next(
                (img for img in product.images.all() if img.is_main),
                product.images.first()
            )

    else:
        current_category = None
        products = []

    return render(request, "pages/catalog.html", {
        "categories": categories,
        "products": products,
        "current_category": current_category,
    })

def product_view(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("category").prefetch_related("images"),
        slug=slug
    )

    context = {
        "product": product
    }

    return render(request, "pages/product.html", context)
