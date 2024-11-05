from django.urls import path
from . import views

urlpatterns = [
    path('gfg/', views.gfg),  
    path('earthly/', views.earthly),  
]
