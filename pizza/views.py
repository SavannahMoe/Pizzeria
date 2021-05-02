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
    comments = pizza.comments_set.all()
    
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}
    return render(request, 'pizza/pizza.html', context)


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            form.save()

            return redirect('pizza:pizza',pizza_id=pizza.id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizza/new_comment.html', context)


def edit_comment(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    pizza = comment.topic

    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza:pizza', pizza_id=pizza.id)
    
    context = {'comment':comment, 'form':form, 'pizza':pizza}
    return render(request, 'pizza/edit_comment.html', context)


    


