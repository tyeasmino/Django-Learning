from django.shortcuts import render, redirect
from .forms import MusiciansForm
from .models import MusiciansModel
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView 

class AddMusicianCreateView(CreateView):
    model = MusiciansModel
    form_class = MusiciansForm
    template_name = 'musician/add_Musician.html'
    success_url = reverse_lazy('add_Musician')

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateMusicianView(UpdateView):
    model = MusiciansModel
    form_class = MusiciansForm
    template_name = 'musician/add_Musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')


class DeleteMusicianView(DeleteView):
    model = MusiciansModel
    template_name = 'musician/delete_Musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')


# class UserLoginView(LoginView):
#     template_name = 'musician/registration.html'

#     def form_valid(self, form):
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         return super().form_invalid(form) 

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["type"] = 'Login' 
#         return context
    
        
    
