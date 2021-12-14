from django.db import models

# Create your models here.

class Register(models.Model):
    firstname=models.CharField(max_length=25)
    surname=models.CharField(max_length=20)
    email_phone=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
