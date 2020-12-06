from django.http import HttpResponse
from django.shortcuts import render

def home(*args, **kwargs):
    return HttpResponse("<h1>Hello world<br>"
                        "Welcome to my webpage"
                        "</h1>")
def contact(*args, **kwargs):
    return HttpResponse("<h1>You can contact me at drparishrameearticles@gmail.com<<br>"
                        "or parishramee@debhiss.com/h1>")
# Create your views here.
