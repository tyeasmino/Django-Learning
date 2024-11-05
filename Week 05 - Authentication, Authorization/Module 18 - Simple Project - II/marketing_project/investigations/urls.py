from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_investigations, name='add_investigations'), 
]