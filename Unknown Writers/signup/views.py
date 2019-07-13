from django.shortcuts import render
from django.http import HttpResponse
from .models import signupform
# Create your views here.

def signupview(request):

    return render(request,'Createaccount.html')


def newPage(request):

    name=request.POST.get("uname")
    emailid=request.POST.get("Email")
    password=request.POST.get("password")

    data1 =signupform(Name =name ,Email=emailid, Password =password)
    data1.save()
    
    return render(request, 'Login_Page.html')
    