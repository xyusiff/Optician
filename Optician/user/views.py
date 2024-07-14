from django.shortcuts import render

# Create your views here.

def login(request):
    # Your view logic here
    return render(request, 'login.html')

def my_account(request):
    # Your view logic here
    return render(request, 'my-account.html')