from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name='homepage'),  
    path('location/<slug:location_slug>/', views.home, name='location_wise_investigation'),  
    path('diagnostic_center/', include('diagnostic_center.urls')),
    path('marketing_executive/', include('marketing_executive.urls')),
    path('investigations/', include('investigations.urls')),
    path('locations/', include('locations.urls')),
]
