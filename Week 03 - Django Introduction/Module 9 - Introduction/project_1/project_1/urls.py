from django.contrib import admin
from django.urls import path, include

# way 1 
# from .views import contact
# path('contact/', contact) 


# way 2 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('first_app/', include("first_app.urls")),
    path('contact/', views.contact)
]
