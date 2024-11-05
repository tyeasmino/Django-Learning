from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def add_location(request):
    if request.method == 'POST':
        location_form = forms.LocationForm(request.POST) 
        if location_form.is_valid():
            location_form.save() 
            return redirect('add_location')
    
    else:
        location_form = forms.LocationForm() 

    return render(request, 'add_location.html', {'form' : location_form})  