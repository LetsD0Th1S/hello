from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello there!! I'm index :)")

def julian(request):
    return HttpResponse("Julian's page")

def all(request, name):
    return HttpResponse(f"{name.capitalize()}'s brand new page!")