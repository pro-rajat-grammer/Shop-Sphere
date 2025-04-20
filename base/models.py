from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class products(models.Model):
    category=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    image=models.ImageField(default='default.png')
    trend=models.BooleanField(default=False)




class Contactmodel(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    message=models.CharField(max_length=400)



class Cart(models.Model):
    category=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=1)
    totalprice=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

