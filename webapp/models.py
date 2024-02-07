from django.db import models

# Create your models here.
class RegistrationDb(models.Model):
    RegName=models.CharField(max_length=60,null=True,blank=True)
    Rprofileim=models.ImageField(upload_to="profileim",null=True,blank=True)
    REmail=models.EmailField(max_length=100,null=True,blank=True)
    Rpassword=models.CharField(max_length=60,null=True,blank=True)
class CartDb(models.Model):
    UseName=models.CharField(max_length=70,null=True,blank=True)
    ProName=models.CharField(max_length=50,null=True,blank=True)
    ProDis=models.CharField(max_length=150,null=True,blank=True)
    ProQuantity=models.IntegerField(null=True,blank=True)
    ProTotal=models.IntegerField(null=True,blank=True)

class CheckoutDb(models.Model):
    CheckName=models.CharField(max_length=50,null=True,blank=True)
    Checkemail=models.EmailField(max_length=60,null=True,blank=True)
    CheckAddress=models.CharField(max_length=100,null=True,blank=True)
    CheckPhone=models.IntegerField(null=True,blank=True)
    CheckSubject=models.CharField(max_length=100,null=True,blank=True)


