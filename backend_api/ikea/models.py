from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    location = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.title
#
class Product_category(models.Model):
    title =models.CharField(max_length=200)
    detail  =  models.TextField(null = True, max_length=50)
    
    def __str__(self):
        return self.title
  
class Product(models.Model):
       name = models.CharField(max_length=20)
       detail = models.TextField(null=True)
       price = models. FloatField()
       
       def __str__(self):
          return self.title