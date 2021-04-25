from django.db import models


class Register(models.Model):
    r_name = models.CharField(max_length=30)
    r_email = models.EmailField(primary_key=True)
    r_password = models.CharField(max_length=30)
    r_role = models.CharField(max_length=10)

# Create your models here.
