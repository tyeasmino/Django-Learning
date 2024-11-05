from django.shortcuts import render 
from investigations.models import Investigation

def home(request):
    # profileData = Profiles.objects.all()
    investigationData = Investigation.objects.all()


    return render(request, 'home.html', {  'investigationData' : investigationData})