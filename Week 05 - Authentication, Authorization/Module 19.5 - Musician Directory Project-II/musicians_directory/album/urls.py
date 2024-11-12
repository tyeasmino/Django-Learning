from django.urls import path 
from . import views

urlpatterns = [
    path('add/', views.AddAlbumCreateView.as_view(), name ='add_Album'), 
    path('edit/<int:id>', views.UpdateAlbumView.as_view(), name ='edit_Album') 
]


