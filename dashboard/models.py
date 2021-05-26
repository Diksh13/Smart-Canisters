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

class Alert(models.Model):
    a_id=models.AutoField(primary_key=True)
    c_id=models.IntegerField()
    c_name=models.CharField(max_length=30)
    c_max_capacity=models.IntegerField()
    c_actual_amount=models.IntegerField()
    grocery=models.IntegerField()
    register=models.IntegerField()

#after updating empty or low container

# DELIMITER $$
# CREATE TRIGGER after_canister_update
#     AFTER UPDATE 
#     ON dashboard_canisters FOR EACH ROW
# BEGIN
#     IF new.c_actual_amount< 0.1*new.c_max_capacity THEN
#         INSERT INTO dashboard_alert 
#             SET c_id = new.c_id,c_name = new.c_name,c_max_capacity=new.c_max_capacity,c_actual_amount=new.c_actual_amount,grocery = new.grocery_id,register=new.register_id;		
#     END IF;
# END$$    
# DELIMITER ;

#after updating full canister

# DELIMITER $$
# CREATE TRIGGER after_canister_full_update
#     AFTER UPDATE 
#     ON dashboard_canisters FOR EACH ROW
# BEGIN
#     IF new.c_actual_amount>0.1*new.c_max_capacity THEN
#         DELETE FROM dashboard_alert 
#             WHERE c_id = new.c_id AND register=new.register_id;
#     END IF;
# END$$    
# DELIMITER ;


# # Create your models here.
