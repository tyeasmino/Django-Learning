from django.urls import path 
from . import views 

urlpatterns = [ 
    path('register/', views.userRegister.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name ='user_login'), 
    path('logout/', views.UserLogoutView.as_view(), name ='user_logout'), 
    path('profile/', views.ProfileView.as_view(), name ='user_profile'), 
    path('add/', views.AddMusicianCreateView.as_view(), name ='add_Musician'), 
    path('edit/<int:id>', views.UpdateMusicianView.as_view(), name ='edit_Musician'), 
    path('delete/<int:id>', views.DeleteMusicianView.as_view(), name ='delete_Musician'), 
]
