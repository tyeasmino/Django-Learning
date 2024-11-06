from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
def add_investigations(request):
    if request.method == 'POST':
        investigation_form = forms.InvestigationForm(request.POST)
        if investigation_form.is_valid():
            # investigation_form.cleaned_data['marketing_executive'] = request.user

            investigation_form.instance.marketing_executive = request.user 
            investigation_form.save()
            messages.success(request, 'Investigation Added Successfully!')
            return redirect('profile')

    else:
        investigation_form = forms.InvestigationForm()
    
    return render(request, 'add_investigations.html', {'form' : investigation_form})


@login_required
def edit_investigations(request, id):
    investigation = models.Investigation.objects.get(pk=id)
    investigation_form = forms.InvestigationForm(instance=investigation)

    if request.method == 'POST':
        investigation_form = forms.InvestigationForm(request.POST, instance=investigation)
        if investigation_form.is_valid():
            # investigation_form.cleaned_data['marketing_executive'] = request.user

            investigation_form.instance.marketing_executive = request.user 
            investigation_form.save()
            messages.success(request, 'Investigation Updated Successfully!')
            return redirect('profile')
    
    return render(request, 'edit_investigation.html', {'form' : investigation_form})


@login_required
def delete_investigations(request, id):
    investigation = models.Investigation.objects.get(pk=id).delete()
    return redirect("profile") 
