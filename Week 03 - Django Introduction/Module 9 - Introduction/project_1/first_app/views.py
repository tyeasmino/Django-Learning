from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app(request):
    return HttpResponse("This is first app -> home page.")
    
def courses(request):
    return HttpResponse("This is first app -> courses page.")

def about(request):
    return HttpResponse("This is first app -> about page.")
