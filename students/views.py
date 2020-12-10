from django.http import HttpResponse
from django.shortcuts import render

def home(request,*args, **kwargs):
    #print(request.user)
    return render(request, "home.html" , {})
    #just to add some text to below commented code can be handy
    #return HttpResponse("<h1>Hello world<br>Welcome to my webpage</h1>")
def contact(request,*args, **kwargs):

    return render(request, "contact.html", {})
def about(request,*args, **kwargs):
    return render(request, "about.html", {})
