from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name='homepage'),  
    path('diagnostic_center/', include('diagnostic_center.urls')),
    path('marketing_executive/', include('marketing_executive.urls')),
    path('investigations/', include('investigations.urls')),
    path('locations/', include('locations.urls')),
]
