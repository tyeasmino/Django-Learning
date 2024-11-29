from django import forms
from .models import BookCategoryModel, BookModel 

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategoryModel
        fields = '__all__'
    

class BookDetailsForm(forms.ModelForm):
    class Meta: 
        model = BookModel
        fields = '__all__' 
    

# class CommentsForm(forms.ModelForm):
#     class Meta: 
#         model = CommentModel
#         fields = ['name', 'email', 'comment'] 