from django.shortcuts import render
from musician.models import MusiciansModel
from album.models import AlbumsModel

def index(request):
    musicianData = MusiciansModel.objects.all()
    albumData = AlbumsModel.objects.all()


    return render(request, 'index.html', {'musicianData': musicianData, 'albumData':albumData})