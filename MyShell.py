import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Pizzeria.settings')

import django
django.setup()

from pizza.models import Pizza, Topping

pizzas = Pizza.objects.all()

p = Pizza.objects.get(id=1) 
print(p)
toppings = p.topping_set.all()
for topping in toppings:
    print(topping)

'''
for p in pizzas:
    print(f"Pizza ID: {p.id} Pizza: {p}") 

toppings = Topping.objects.all()

for t in toppings:
    print(f"Pizza: {t.pizza}")
    print(f"Toppings: {t.name}")
'''