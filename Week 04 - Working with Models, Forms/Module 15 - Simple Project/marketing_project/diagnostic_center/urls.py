from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_diagnostic_center, name='add_diagnostic_center'), 
]