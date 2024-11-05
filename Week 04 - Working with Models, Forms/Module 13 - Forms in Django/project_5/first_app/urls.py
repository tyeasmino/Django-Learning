from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('about/', views.about, name = 'aboutpage'),
    path('form/', views.form, name = 'formpage'),
    # path('django_form/', views.DjangoForm, name = 'django_form'),
    path('django_form/', views.StudentForm, name = 'django_form'),
    path('password_form/', views.PasswordForm, name = 'password_form'),
]
