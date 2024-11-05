from django.shortcuts import render, redirect
from .forms import AlbumForm
from album.models import AlbumsModel

# Create your views here.
def add_Album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('add_Album')
    else:
        form = AlbumForm()
    return render(request, 'album/add_Album.html', {'form' : form})


def edit_Album(request, id):
    albumData = AlbumsModel.objects.get(pk=id)  
    form = AlbumForm(instance=albumData)
    
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=albumData)
        if(form.is_valid()):
            form.save()
            return redirect('index')

    return render(request, 'album/add_Album.html', {'form' : form}) 