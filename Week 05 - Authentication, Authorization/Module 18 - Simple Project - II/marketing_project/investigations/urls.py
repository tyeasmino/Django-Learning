from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_investigations, name='add_investigations'), 
    path('edit/<int:id>', views.edit_investigations, name='edit_investigations'), 
    path('delete/<int:id>', views.delete_investigations, name='delete_investigations'), 
]