from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def add_investigations(request):
    if request.method == 'POST':
        investigation_form = forms.InvestigationForm(request.POST)
        if investigation_form.is_valid():
            # investigation_form.cleaned_data['marketing_executive'] = request.user

            investigation_form.instance.marketing_executive = request.user 
            investigation_form.save()
            return redirect('add_investigations')

    else:
        investigation_form = forms.InvestigationForm()
    
    return render(request, 'add_investigations.html', {'form' : investigation_form})
