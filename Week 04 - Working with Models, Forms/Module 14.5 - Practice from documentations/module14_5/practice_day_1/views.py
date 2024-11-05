from django.shortcuts import render
from .forms import ContactForm, GeeksForm, MyForm

# Create your views here.
def home(request):
    contactForm = ContactForm()

    return render(request, 'practice_day_1/index.html', {'form' : contactForm} )

def gfg(request):
    contactForm = GeeksForm()

    return render(request, 'practice_day_1/gfg.html', {'form' : contactForm} ) 

def medium(request):
    if request.method == 'POST':
        form = MyForm(request.POST) 
        if form.is_valid(): 
            print(form.cleaned_data) 
             
    else:
        form = MyForm()

    return render(request, 'practice_day_1/medium.html', {'form' : form} ) 