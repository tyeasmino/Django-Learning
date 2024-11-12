from django.urls import path 
from . import views

urlpatterns = [
    path('add/', views.AddMusicianCreateView.as_view(), name ='add_Musician'), 
    path('edit/<int:id>', views.UpdateMusicianView.as_view(), name ='edit_Musician'), 
    path('delete/<int:id>', views.DeleteMusicianView.as_view(), name ='delete_Musician'), 
]
