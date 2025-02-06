from django.shortcuts import redirect, render
from django.http import HttpResponse
from myapp.forms import *
from .models import *

def Users(request):
    myform= RegistrationForms()
    person=Question.objects.all()
    #person=Question.objects.filter(name="geetha")
    #person=Question.objects.exclude(name="geetha")
    #person=Question.objects.order_by(name,-name)
    #person=Question.objects.value(name)
    if request.method=="GET":
        name=request.GET.get('name','guest')
    elif request.method=="POST":
        postform=RegistrationForms(request.Post)
        if postform.is_valid():
            postform.save()
            return redirect("success")
    return render(request,"index.html",{'forms':'myform','person':'person'})
