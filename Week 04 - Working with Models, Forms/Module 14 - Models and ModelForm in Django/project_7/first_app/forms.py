from django import forms
# from . import models
from .models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel 
        fields = '__all__' 
        # fields = ['name', 'roll']
        # exclude = ['roll'] 

        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }

        # widgets = {
        #     'roll' : forms.TextInput(attrs={'class': 'form-control my-2'}),
        #     'name' : forms.TextInput(attrs={'class': 'form-control my-2'}),
        #     'father_name' : forms.TextInput(attrs={'class': 'form-control my-2'}),
        #     'address' : forms.TextInput(attrs={'class': 'form-control my-2'}),
        # }

        # help_texts = {
        #     'name' : 'Write your full name'
        # }
        