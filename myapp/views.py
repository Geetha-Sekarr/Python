from django.shortcuts import render
from django.http import HttpResponse

def Users(request):
    return render(request,"index.html")
