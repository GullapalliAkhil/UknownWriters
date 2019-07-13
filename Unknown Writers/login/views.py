from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginview(request):

    return render(request,'Login_Page.html')