from django.db import models

# Create your models here.(Data base structure or Database table to store the user info)

class signupform(models.Model):

    Name=models.CharField(max_length=16)

    Email=models.CharField(max_length=40)

    Password=models.CharField(max_length=14)


class thoughtspost(models.Model):

    user_thoughts=models.CharField(max_length=4000)

    posted_at=models.DateTimeField(auto_now_add=True)

