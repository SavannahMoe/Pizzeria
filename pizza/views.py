from django.shortcuts import render

# Create your views here.

def index(request):
    """The Home Page for Pizzeria"""
    return render(request, 'Pizza/index.html')