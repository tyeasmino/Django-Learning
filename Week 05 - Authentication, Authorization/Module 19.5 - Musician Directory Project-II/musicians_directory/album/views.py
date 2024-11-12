from django.shortcuts import render, redirect
from .forms import AlbumForm
from album.models import AlbumsModel
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required 


# # Create your views here.
@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = AlbumsModel
    form_class = AlbumForm
    template_name = 'album/add_Album.html'
    success_url = reverse_lazy('add_Album') 

    def form_valid(self, form):
        return super().form_valid(form)
    



@method_decorator(login_required, name='dispatch')
class UpdateAlbumView(UpdateView):
    model = AlbumsModel
    form_class = AlbumForm
    template_name = 'album/add_Album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')

