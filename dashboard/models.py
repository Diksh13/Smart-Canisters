from django.db import models

# Create your models here.
from django.db import models
from accounts.models import Register


class CustomerAddress(models.Model):
    c_house_no = models.CharField(primary_key=True, max_length=10)
    c_apartment= models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    landmark = models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    pincode=models.CharField(max_length=10)
    user=models.ForeignKey(Register, on_delete=models.CASCADE)


class VendorAddress(models.Model):
    v_shop_no = models.CharField(primary_key=True, max_length=10)
    v_shop= models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    landmark = models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    pincode=models.CharField(max_length=10)
    vendor=models.ForeignKey(Register, on_delete=models.CASCADE)


class Grocery(models.Model):
    g_id=models.AutoField(primary_key=True, unique=True)
    g_name=models.CharField(max_length=30)
    g_amount=models.IntegerField()
    g_price=models.IntegerField()

class Canisters(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=30)
    c_max_capacity=models.IntegerField()
    c_actual_amount=models.IntegerField()
    grocery=models.ForeignKey(Grocery, on_delete=models.CASCADE)
    register=models.ForeignKey(Register, on_delete=models.CASCADE)


# # Create your models here.
