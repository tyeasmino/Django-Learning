from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'navigation/about.html')

def contact(request):
    return render(request, 'navigation/contact.html')

def projects(request):
    return render(request, 'navigation/projects.html')