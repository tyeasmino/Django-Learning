from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_profile, name='add_profile'), 
    path('edit/<int:id>', views.edit_profile, name='edit_profile'), 
    path('delete/<int:id>', views.delete_profile, name='delete_profile'), 
]