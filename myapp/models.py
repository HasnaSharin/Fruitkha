from django.db import models

# Create your models here.
class categoryDb(models.Model):
    Name=models.CharField(max_length=60,null=True,blank=True)
    Image=models.ImageField(upload_to="propic",null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
class productDb(models.Model):
    Category=models.CharField(max_length=60,null=True,blank=True)
    PrdctName=models.CharField(max_length=60,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Brand=models.CharField(max_length=50,null=True,blank=True)
    Productimage=models.ImageField(upload_to="Dp",null=True,blank=True)
class ContactDb(models.Model):
    ConName=models.CharField(max_length=60,null=True,blank=True)
    ConEmail=models.EmailField(max_length=60,null=True,blank=True)
    ConPhone=models.IntegerField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)