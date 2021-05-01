import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Pizzeria.settings')

import django
django.setup()

from pizza.models import Pizza, Topping, Comments

pizzas = Pizza.objects.all()

pizza = Pizza.objects.get(id=1) 
print(pizza)
toppings = pizza.topping_set.all()
for topping in toppings:
    print(topping)

comments = pizza.comments_set.all()
for comment in comments:
    print(f"CommentID: {comment.pizza} Comment:{comment.comment} ")

'''
for p in pizzas:
    print(f"Pizza ID: {p.id} Pizza: {p}") 

toppings = Topping.objects.all()

for t in toppings:
    print(f"Pizza: {t.pizza}")
    print(f"Toppings: {t.name}")
'''