from django.shortcuts import render

# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    response.set_cookie('name', 'karim')

    return response 