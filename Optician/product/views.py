from django.shortcuts import render

from .models import *

# Create your views here.

def product(request):
    # Your view logic here
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def product_detail(request):
    # Your view logic here
    return render(request, 'single-product.html')