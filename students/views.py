from django.http import HttpResponse
from django.shortcuts import render

def home(*args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")

# Create your views here.
