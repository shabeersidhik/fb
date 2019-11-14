from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class Register(models.Model):
    firstnam=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    birthday=models.DateField()
    gender=models.CharField(max_length=15)
    fk_login=models.ForeignKey(Login,on_delete=models.CASCADE)