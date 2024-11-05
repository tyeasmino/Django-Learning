from django import forms
from .models import Diagnostic_Center

class Diagnostic_Center_Form(forms.ModelForm):
    class Meta:
        model = Diagnostic_Center
        fields = '__all__'
        