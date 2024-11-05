from django.shortcuts import render, redirect 

# for signup
from .forms import RegisterForm 
from django.contrib import messages 

# for signin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 

# for password change 
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash 


# for update info 
from .forms import ChangeUserInfoForm

# Create your views here.
def home(request):
    return render(request, 'first_app/home.html') 

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully') 
                form.save()

        else:
            form = RegisterForm()

        return render(request, 'first_app/signup.html', {'form' : form}) 

    else:
        return redirect('profile')


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successfully') 
                    return redirect('profile')
        
        else: 
            form = AuthenticationForm()
        
        return render(request, 'first_app/signin.html', {'form' : form}) 
    
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserInfoForm(request.POST, instance=request.user) 
            if form.is_valid():
                messages.success(request, 'Account updated successfully') 
                form.save()

        else:
            form = ChangeUserInfoForm(instance=request.user)

        return render(request, 'first_app/profile.html', {'form' : form}) 

    else:
        return redirect('signup') 

def user_logout(request):
    logout(request)
    return redirect('signin') 


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
            
        else:
            form = PasswordChangeForm(user=request.user)
        
        return render(request, 'first_app/passchange.html', {'form' : form}) 
    else:
        return redirect('signin')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
            
        else:
            form = SetPasswordForm(user=request.user)
        
        return render(request, 'first_app/passchange.html', {'form' : form}) 
    else:
        return redirect('signin')


def change_user_info(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserInfoForm(request.POST, instance=request.user) 
            if form.is_valid():
                messages.success(request, 'Account updated successfully') 
                form.save()

        else:
            form = ChangeUserInfoForm(instance=request.user)

        return render(request, 'first_app/profile.html', {'form' : form}) 

    else:
        return redirect('signup') 