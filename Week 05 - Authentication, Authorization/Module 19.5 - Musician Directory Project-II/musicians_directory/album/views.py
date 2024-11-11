from django.shortcuts import render, redirect
from .forms import AlbumForm
from album.models import AlbumsModel
from django.views.generic import CreateView
from django.urls import reverse_lazy



# # Create your views here.
# def add_Album(request):
#     if request.method == 'POST':
#         form = AlbumForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return redirect('add_Album')
#     else:
#         form = AlbumForm()
#     return render(request, 'album/add_Album.html', {'form' : form})



# Add album using class based view
class AddAlbumCreateView(CreateView):
    model = AlbumsModel
    form_class = AlbumForm
    template_name = 'album/add_Album.html'
    success_url = reverse_lazy('add_Album') 

    def form_valid(self, form):
        return super().form_valid(form)
    






def edit_Album(request, id):
    albumData = AlbumsModel.objects.get(pk=id)  
    form = AlbumForm(instance=albumData)
    
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=albumData)
        if(form.is_valid()):
            form.save()
            return redirect('index')

    return render(request, 'album/add_Album.html', {'form' : form}) 