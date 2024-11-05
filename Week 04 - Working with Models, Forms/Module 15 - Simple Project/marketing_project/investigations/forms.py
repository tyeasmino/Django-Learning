from django import forms
from .models import Investigation

class InvestigationForm(forms.ModelForm):
    
    class Meta:
        model = Investigation
        fields = '__all__'
