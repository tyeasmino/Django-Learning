from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import MyModel


class ContactForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
    name = forms.CharField(max_length = 20, initial='Your name') 
    email = forms.EmailField(label="Please enter your email address")
    value = forms.DecimalField(required = False)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))


    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color_choice = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_multiple_choice = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_checkbox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)



    comment = forms.CharField(min_length=10, widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField(initial=True)



class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField() 

    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput())



class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'