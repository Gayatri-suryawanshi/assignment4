from django.db import models

# Create your models here.

class User(models.Model):
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    PhoneNumber=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)