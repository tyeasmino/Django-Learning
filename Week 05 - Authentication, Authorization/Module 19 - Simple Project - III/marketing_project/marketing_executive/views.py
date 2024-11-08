from django.shortcuts import render, redirect 
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from investigations.models import Investigation


# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()
    
    return render(request, 'register.html', {'form': register_form, 'type' : 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password = user_pass)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully!')
                return redirect('profile')
            else:
                messages.warning(request, 'Login informations are incorrect!')
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login' })


@login_required 
def profile(request):
    investigationData = Investigation.objects.filter(marketing_executive = request.user) 
    return render(request, 'profile.html', {'investigationData': investigationData})

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


@login_required 
def change_pass(request):
    if request.method == 'POST':
        change_pass_form = PasswordChangeForm(request.user, data=request.POST) 
        if change_pass_form.is_valid():
            change_pass_form.save()
            messages.success(request, 'Password Updated Successfully!')
            update_session_auth_hash(request, change_pass_form.user) 
            return redirect('profile')
    
    else:
        change_pass_form = PasswordChangeForm(request.user) 
    
    return render(request, 'password_change.html', {'form': change_pass_form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Logout Successfully!')
    return redirect('user_login')
