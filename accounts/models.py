from django.db import models
# from django.utils import timezone

class Register(models.Model):
    r_id = models.AutoField(primary_key=True,unique=True)
    r_name = models.CharField(max_length=30)
    r_email = models.EmailField(max_length=30)
    r_password = models.CharField(max_length=30)
    r_role = models.CharField(max_length=10)

class Login(models.Model):
    sid = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    login_time = models.DateTimeField(null=True)
    logout_time = models.DateTimeField(null=True)

# Create your models here.
