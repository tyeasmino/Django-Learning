from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name='homepage'), 
    path('profiles/', include('profiles.urls')),
    path('diagnostic_center/', include('diagnostic_center.urls')),
    path('investigations/', include('investigations.urls')),
    path('locations/', include('locations.urls')),
]
