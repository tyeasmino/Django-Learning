from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('gfg/', views.gfg, name='gfg'),
    path('medium/', views.medium, name='medium'),
]
