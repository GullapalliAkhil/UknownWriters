from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import signupform, thoughtspost
import logging
from django.contrib import messages
from django.contrib.auth import logout 
import time




# Create your views here.

logger=logging.getLogger("UnknownWriters")

#When user clicks on Create Account Signup form page will be displayed.

def signupview(request):

    return render(request,'Createaccount.html')
    

#User Data will be stored in the database and when clicks on create user will be redirected to the Login page.

def newPage(request):

    name=request.POST.get("uname")

    emailid=request.POST.get("Email")

    password=request.POST.get("password")

    data1 =signupform(Name =name ,Email=emailid, Password =password)

    data1.save()

    time.sleep(4)
    
    return render(request, 'Login_Page.html')

#Login Page will be displayed to the user

def loginview1(request):

    return render(request,'Login_Page.html')  

#To validate the login functinality and navigate to the Home page

def user_login(request):

    username=request.POST.get('username')

    password=request.POST.get('Password')

    all_data=signupform.objects.all()
    
    for i in range (0, all_data.count()):

        if username==all_data[i].Name and password==all_data[i].Password:

               all_content=thoughtspost.objects.all()

               return render(request,'HomePage.html',{'all_data':all_content})

               break
        #else:

          # return render(request, 'Error.html')
    
def userthoughts(request):
    
    comments=request.POST.get('message')
    
    data=thoughtspost(user_thoughts=comments)

    data.save()

    all_content=thoughtspost.objects.all()

    return render(request,'HomePage.html',{'all_data':all_content})
    
#Log out functionality 

def user_logout(request):

   if request.method=="POST":
       request.sessions.
      return render(request, 'logout.html') 
    

    
   


     
       

         