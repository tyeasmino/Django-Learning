from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('add/', views.add_marketing_executive, name='add_marketing_executive'), 
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),


    # path('logout/', views.user_logout, name='user_logout'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),


    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/change_password/', views.change_pass, name='change_password'),
]