from django.db import models

# Create your models here.
class signupform(models.Model):

    Name=models.CharField(max_length=16)
    Email=models.CharField(max_length=40)
    Password=models.CharField(max_length=14)

