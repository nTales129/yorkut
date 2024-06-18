from django.urls import path 
from galeria.views import index, cadastro 

urlpatterns = [
    path('', index),
    path('card/', cadastro, name='card')
]