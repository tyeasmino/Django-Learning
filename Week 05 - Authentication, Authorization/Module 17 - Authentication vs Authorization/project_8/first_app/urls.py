from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('profile/', views.profile, name = 'profile'),
    path('pass_change/', views.pass_change, name = 'pass_change'),
    path('pass_change2/', views.pass_change2, name = 'pass_change2'),
    path('logout/', views.user_logout, name = 'logout'),
]
