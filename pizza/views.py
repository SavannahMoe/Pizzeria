from django.shortcuts import render
from .models import Pizza, Topping


# Create your views here.

def index(request):
    """The Home Page for Pizzeria"""
    return render(request, 'Pizza/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas': pizzas}
    return render(request, 'pizza/pizzas.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizza/pizza.html', context)