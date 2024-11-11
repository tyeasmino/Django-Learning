from django import forms
from .models import MusiciansModel

class MusiciansForm(forms.ModelForm):
    
    class Meta:
        model = MusiciansModel
        fields = '__all__'
