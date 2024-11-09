from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, UpdateView, DeleteView

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



@method_decorator(login_required, name='dispatch')
class addInvestigationCreateView(CreateView):
    model = models.Investigation
    form_class = forms.InvestigationForm
    success_url = reverse_lazy('profile') 
    template_name = 'add_investigations.html'
    def form_valid(self, form):
        form.instance.marketing_executive = self.request.user
        return super().form_valid(form)
    






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


@method_decorator(login_required, name='dispatch')
class updateInvestigationUpdateView(UpdateView):
    model = models.Investigation
    form_class = forms.InvestigationForm
    success_url = reverse_lazy('profile') 
    template_name = 'add_investigations.html'
    pk_url_kwarg = 'id'
        




@login_required
def delete_investigations(request, id):
    investigation = models.Investigation.objects.get(pk=id).delete()
    return redirect("profile") 


@method_decorator(login_required, name='dispatch')
class deleteInvestigationDeleteView(DeleteView):
    model = models.Investigation
    success_url = reverse_lazy('profile')
    template_name = 'delete_investigation.html'
    pk_url_kwarg = 'id' 

