from django.shortcuts import render

# Create your views here.

def about(request):
    # Your view logic here
    return render(request, 'about-us.html')

def index(request):
    return render(request, 'index.html') 
