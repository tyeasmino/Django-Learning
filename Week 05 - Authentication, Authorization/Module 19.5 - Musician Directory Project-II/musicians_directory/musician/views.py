from django.shortcuts import render, redirect
from .forms import MusiciansForm, RegistrationForm
from .models import MusiciansModel
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = MusiciansModel
    form_class = MusiciansForm
    template_name = 'musician/add_Musician.html'
    success_url = reverse_lazy('add_Musician')

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UpdateMusicianView(UpdateView):
    model = MusiciansModel
    form_class = MusiciansForm
    template_name = 'musician/add_Musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')


@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = MusiciansModel
    template_name = 'musician/delete_Musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')


@method_decorator(login_required, name='dispatch')
class ProfileView(CreateView):
    model = MusiciansModel
    form_class = MusiciansForm
    template_name = 'musician/profile.html'


class userRegister(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "musician/register.html"
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form): 
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context
    

class UserLoginView(LoginView):
    template_name = 'musician/register.html'
    
    def get_success_url(self):
        return reverse_lazy('user_profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in failed!')
        return super().form_invalid(form) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login' 
        return context
    
        
class UserLogoutView(LogoutView): 
    def get_success_url(self):
        return reverse_lazy('user_login')