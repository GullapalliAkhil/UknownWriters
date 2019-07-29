from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import signupform, thoughtspost
import logging
from django.contrib import messages
from django.contrib.auth import logout 
import time



#When user clicks on Create Account Signup form page will be displayed.

def signupview(request):

    return render(request,'Createaccount.html')
    

#Sending the user data to store in the database .

def newPage(request):

    name=request.POST.get("uname")

    emailid=request.POST.get("Email")

    password=request.POST.get("password")
       
    if signupform.objects.filter(Name=name).exists():
        
       Error="Another user with this username already exists." 

       return render(request, 'Createaccount.html',{'error':Error})
       
    else:

       data1 =signupform(Name =name ,Email=emailid, Password =password)

       data1.save()

       time.sleep(4)
    
       return render(request, 'Login_Page.html')

        
#Login Page will be displayed to the user

def loginview1(request):

    return render(request,'Login_Page.html')  

#To validate the login functinality and navigate to the Home page
#Verify the characters length
#Check if username exists
#Check if given password is equal to the retrieved password.

def user_login(request):

    if request.method == 'POST':
 
       username=request.POST.get('username')

       password=request.POST.get('Password')

       if len(username)==0 and len(password)==0:

         Error="Username or Password fields cannot be empty."

         return render(request, 'Login_Page.html',{'error':Error})

       if len(username)>25 and len(password)>16:

         Error="Username or Password is incorrect."

         return render(request, 'Login_Page.html',{'error':Error})

       if len(username)<5 and len(password)<5:

         Error="Username or Password is incorrect."

         return render(request, 'Login_Page.html',{'error':Error})

       else:
         
         try:
            Data=signupform.objects.get(Name=username)
       
            if Data.Password==password:
         
             all_content=thoughtspost.objects.all()

             request.session['username']=username

             request.session.set_expiry(300)
       
             return render(request,'HomePage.html',{'all_data':all_content,'username':username })
         
            else:
             
             Error="Password is incorrect."

             return render(request,'Login_Page.html',{'error':Error}) 
  
         except:
           
           Error="Username does not exist."

           return render(request,'Login_Page.html',{'error':Error})  
    else:
      
      return render(request,'Login_Page.html')
      
##
# To post the comments data to the database
# ##    
def userthoughts(request):
    
    comments=request.POST.get('message')
    
    data=thoughtspost(user_thoughts=comments)

    data.save()

    all_content=thoughtspost.objects.all()

    return render(request,'HomePage.html',{'all_data':all_content})
    
#Log out functionality 

def user_logout(request):
  
    try:

      del request.session['username']
      
    except KeyError:
       
       pass
    
    return render(request, 'logout.html') 
           