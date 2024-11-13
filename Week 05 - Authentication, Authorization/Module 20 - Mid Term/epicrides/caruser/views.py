from django.shortcuts import render
from django.contrib.auth.models import User
from . import forms, models
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# Create your views here.
class CarUserRegistrationCreateView(CreateView):
    model = User
    form_class = forms.CarUserRegistrationForm
    template_name = "user_registration_login.html"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Provide correct information to sign up")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTitle"] = 'Sign Up'
        return context
    
    
class CarUserLoginCreateView(LoginView):
    template_name = 'user_registration_login.html'    

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Sign in successful!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Sign in information is incorrect!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTitle"] = 'Sign In'
        return context


class CarUserLogoutCreateView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('signin')



@method_decorator(login_required, name='dispatch')
class CarUserProfileCreateView(CreateView):
    model = User
    form_class = forms.CarUserRegistrationForm
    template_name = 'user_profile.html'



@login_required 
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserInfoForm(request.POST, instance = request.user) 
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserInfoForm(instance = request.user) 
    
    return render(request, 'update_profile.html', {'form': profile_form})



@method_decorator(login_required, name='dispatch')
class CarUserEditProfile(UpdateView):
    model = User
    form_class = forms.CarUserRegistrationForm
    template_name = 'user_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset = None):
        return self.request.user 