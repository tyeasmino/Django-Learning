from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profile_form = forms.ProfilesForm(request.POST) 
        if profile_form.is_valid():
            profile_form.save() 
            return redirect('add_profile')
    
    else:
        profile_form = forms.ProfilesForm() 

    return render(request, 'add_profile.html', {'form' : profile_form})  


def edit_profile(request, id): 

    profile = models.Profiles.objects.get(pk=id) 
    profile_form = forms.ProfilesForm(instance=profile)  


    if request.method == 'POST':
        profile_form = forms.ProfilesForm(request.POST, instance=profile) 
        if profile_form.is_valid():
            profile_form.save() 
            return redirect('homepage')

    return render(request, 'add_profile.html', {'form' : profile_form})  


def delete_profile(request, id):
    
    profile = models.Profiles.objects.get(pk=id) 
    profile.delete() 
    
    return redirect('homepage')
