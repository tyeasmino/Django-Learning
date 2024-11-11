from django.shortcuts import render, redirect
from .forms import MusiciansForm
from .models import MusiciansModel

# Create your views here.
def add_Musician(request):
    if request.method == 'POST':
        form = MusiciansForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('add_Musician')
    else:
        form = MusiciansForm()
    return render(request, 'musician/add_Musician.html', {'form' : form})


def edit_Musician(request, id):
    musicianData = MusiciansModel.objects.get(pk=id) 
    form = MusiciansForm(instance=musicianData)

    if request.method == 'POST':
        form = MusiciansForm(request.POST, instance=musicianData)
        if(form.is_valid()):
            form.save()
            return redirect('index')
     
    return render(request, 'musician/add_Musician.html', {'form' : form})


def delete_Musician(request, id):
    musicianData = MusiciansModel.objects.get(pk=id).delete() 
    
    return redirect('index')