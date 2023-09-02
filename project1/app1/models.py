from django.db import models

# Create your models here.

class registration(models.Model):
    reg_name = models.CharField(max_length=100)
    reg_place = models.CharField(max_length=100)
    reg_address = models.CharField(max_length=100)
    reg_mobno = models.IntegerField()

class homepage(models.Model):
    hom_login = models.CharField(max_length=50)    
    hom_gallery =models.CharField(max_length=50)

class products(models.Model):
    pro_name =  models.CharField(max_length=50)
    pro_prize = models.CharField(max_length=50)
    pro_image = models.ImageField( upload_to='products')

class login(models.Model):    
    log_username = models.CharField(max_length=50)
    log_password = models.CharField(max_length=50)

class changepassword(models.Model):    
    cha_oldpassword = models.CharField(max_length=50)
    cha_newpassword = models.CharField(max_length=50)    
    cha_verifynewpassword = models.CharField(max_length=50) 

    