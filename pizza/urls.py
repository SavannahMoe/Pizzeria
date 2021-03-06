from django.urls import path

from . import views

app_name = 'pizza'

urlpatterns =[
    path('',views.index, name='index'), 
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    #path('pizzas/<int:pizza_id>/', views.comment, name='comment'),
    path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
]
