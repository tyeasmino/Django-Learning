from django.urls import path 
from . import views

urlpatterns = [
    path('add/', views.add_Album, name ='add_Album'), 
    path('edit/<int:id>', views.edit_Album, name ='edit_Album') 
]
