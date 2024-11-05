from django import forms
from .models import AlbumsModel

class AlbumForm(forms.ModelForm):

    class Meta:
        model = AlbumsModel
        fields = '__all__' 
    
