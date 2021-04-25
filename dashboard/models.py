from django.db import models

# Create your models here.
from django.db import models
from accounts.models import Register


class CustomerAddress(models.Model):
    c_house_no = models.CharField(primary_key=True, max_length=10)
    c_apartment= models.CharField(max_length=30)
    c_street = models.CharField(max_length=50)
    c_landmark = models.CharField(max_length=30)
    c_city=models.CharField(max_length=20)
    c_state=models.CharField(max_length=20)
    c_country=models.CharField(max_length=20)
    c_pincode=models.CharField(max_length=10)
    user=models.ForeignKey(Register, on_delete=models.CASCADE)


# Create your models here.
