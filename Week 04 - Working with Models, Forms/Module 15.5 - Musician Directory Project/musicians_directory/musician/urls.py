from django.urls import path 
from . import views

urlpatterns = [
    path('add/', views.add_Musician, name ='add_Musician'), 
    path('edit/<int:id>', views.edit_Musician, name ='edit_Musician'), 
    path('delete/<int:id>', views.delete_Musician, name ='delete_Musician'), 
]
