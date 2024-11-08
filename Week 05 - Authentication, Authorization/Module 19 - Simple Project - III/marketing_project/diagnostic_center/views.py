from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def add_diagnostic_center(request):
    if request.method == 'POST':
        dc_form = forms.Diagnostic_Center_Form(request.POST) 
        if dc_form.is_valid():
            dc_form.save() 
            return redirect('add_diagnostic_center')
    
    else:
        dc_form = forms.Diagnostic_Center_Form() 

    return render(request, 'add_dc.html', {'form' : dc_form})  
 