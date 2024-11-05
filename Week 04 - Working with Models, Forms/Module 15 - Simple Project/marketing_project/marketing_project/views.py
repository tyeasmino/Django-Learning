from django.shortcuts import render
from profiles.models import Profiles
from investigations.models import Investigation

def home(request):
    profileData = Profiles.objects.all()
    investigationData = Investigation.objects.all()


    return render(request, 'home.html', {'profileData' : profileData, 'investigationData' : investigationData})