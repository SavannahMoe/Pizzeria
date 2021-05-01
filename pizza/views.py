from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import CommentForm


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
    #comments = pizza.comment_set.all()
    
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizza/pizza.html', context)


def comments(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
   
    new_comment = None
   
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()

            return redirect('pizza:pizza',pizza_id=pizza.id)

    context = {'form':form, 'pizza':pizza, 'new_comment':new_comment}
    return render(request, 'pizza/comments.html', context)

    


