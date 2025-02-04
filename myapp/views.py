from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import *
from .models import *

def Users(request):
    myform= RegistrationForms()
    return render(request,"index.html",{'forms':'myform'})
