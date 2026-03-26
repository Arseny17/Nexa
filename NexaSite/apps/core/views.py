from django.shortcuts import render
from apps.categories.models import Category

def index(request):
    return render(request, 'pages/index.html')

def categories(request):
    categories = Category.objects.all()

    return render(request, "pages/categories.html", {
        "categories": categories
    })

def about(request):
    return render(request, 'pages/about.html')
