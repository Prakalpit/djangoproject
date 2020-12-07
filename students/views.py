from django.http import HttpResponse
from django.shortcuts import render

def home(request,*args, **kwargs):
    #print(request.user)
    return render(request, "home.html" , {})
    #return HttpResponse("<h1>Hello world<br>Welcome to my webpage</h1>")
def contact(request,*args, **kwargs):
    #return HttpResponse("<h1>You can contact me at drparishrameearticles@gmail.com<br>or parishramee@debhiss.com</h1>")
    return render(request, "contact.html", {})
def about(request,*args, **kwargs):
    #return HttpResponse("<h1>You can contact me at drparishrameearticles@gmail.com<br>or parishramee@debhiss.com</h1>")
    return render(request, "about.html", {})
