from django.shortcuts import render

# Create your views here.

def shopping(request):
    # Your view logic here
    return render(request, 'shopping-cart.html')

def checkout(request):
    # Your view logic here
    return render(request, 'checkout.html')

def wishlist(request):
    # Your view logic here
    return render(request, 'wishlist.html')