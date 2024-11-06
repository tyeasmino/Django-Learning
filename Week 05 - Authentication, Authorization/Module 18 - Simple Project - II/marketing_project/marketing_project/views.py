from django.shortcuts import render 
from investigations.models import Investigation
from locations.models import Location

def home(request, location_slug = None):
    # profileData = Profiles.objects.all()
    investigationData = Investigation.objects.all()
    locationData = Location.objects.all()

    if location_slug is not None:
        location = Location.objects.get(slug = location_slug) 
        investigationData = Investigation.objects.filter(location= location)
 

    return render(request, 'home.html', {  'investigationData' : investigationData, 'locationData' : locationData})