from tkinter import N
from django.urls import path
from .views import list_vete, create_vete, delete_vete

urlpatterns = [
    path('', list_vete),
    path('new/', create_vete, name='create_vete'),
    path('delete_vete/<int:vete_id>/', delete_vete, name='delete_vete')
]
