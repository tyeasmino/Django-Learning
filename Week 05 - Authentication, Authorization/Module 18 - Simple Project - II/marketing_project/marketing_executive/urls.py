from django.urls import path
from . import views
urlpatterns = [
    # path('add/', views.add_marketing_executive, name='add_marketing_executive'), 
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/change_password/', views.change_pass, name='change_password'),
]