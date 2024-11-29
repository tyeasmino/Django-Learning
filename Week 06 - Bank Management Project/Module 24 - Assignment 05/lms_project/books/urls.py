from django.urls import path
from . import views
urlpatterns = [ 
    path('addBookCategory/', views.addBookCategoryView.as_view(), name='addBookCategory'), 
    path('addBookDetails/', views.addBookDetailsView.as_view(), name='addBookDetails'), 
    # path('bookDetails/<int:id>/', views.carDetailsView.as_view(), name='bookDetails'), 


    # path('placeOrder/<int:id>/', views.placeOrder, name='placeOrder'), 


    # path('edit/<int:id>/', views.updateInvestigationUpdateView.as_view(), name='edit_investigations'),  
    # path('delete/<int:id>/', views.deleteInvestigationDeleteView.as_view(), name='delete_investigations'), 
]