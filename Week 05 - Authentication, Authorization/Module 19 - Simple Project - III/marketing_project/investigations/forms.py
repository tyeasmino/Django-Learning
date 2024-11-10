from django import forms
from .models import Investigation, Comment

class InvestigationForm(forms.ModelForm):
    
    class Meta:
        model = Investigation
        # fields = '__all__'
        exclude = ['marketing_executive']



class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body'] 
        
