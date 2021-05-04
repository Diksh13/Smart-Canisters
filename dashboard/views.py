from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *
from accounts.models import *
from accounts.views import LoginPage
from accounts import views
from django.db import connection
class DashboardPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html', context=None)


class AddressPage(TemplateView):
    def post(self, request, pk=None):
        user_id=Register.objects.get(r_id=pk)
        street = request.POST['street']
        landmark = request.POST['landmark']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        user_role=request.POST['role']
        if user_role:
            house_no = request.POST['house-no']
            apartment = request.POST['apartment']
            c = CustomerAddress(c_house_no=house_no, c_apartment=apartment, street=street, landmark=landmark,city=city, state=state, country=country, pincode=pincode,user=user_id)
            c.save()
            return render(request, 'dashboard.html', {"user": user_id,"role":"customer"})
        else:
            shop_no=request.POST['shop-no']
            shop = request.POST['shop']
            c = VendorAddress(v_shop_no=shop_no, v_shop=shop, street=street, landmark=landmark,city=city, state=state, country=country, pincode=pincode,vendor=user_id)
            c.save()
            return render(request, 'dashboard.html', {"user": user_id,"role":""})

class UpdateAddress(TemplateView):
    def post(self,request,pk=None):
        if pk:
            user=Register.objects.get(r_id=pk)
            if user.r_role=="customer":
            # house_no = request.POST['house-no']
                c=CustomerAddress.objects.get(user_id=pk)
                c.c_apartment = request.POST['apartment']
                c.street = request.POST['street']
                c.landmark = request.POST['landmark']
                c.city = request.POST['city']
                c.state = request.POST['state']
                c.country = request.POST['country']
                c.pincode = request.POST['pincode']   
                c.save()
                return render(request, 'dashboard.html', {"user": user,"role":user.r_role,"address":c})
            else:
                v=VendorAddress.objects.get(vendor_id=pk)
                v.v_shop = request.POST['shop']
                v.street = request.POST['street']
                v.landmark = request.POST['landmark']
                v.city = request.POST['city']
                v.state = request.POST['state']
                v.country = request.POST['country']
                v.pincode = request.POST['pincode']   
                v.save()
                return render(request, 'dashboard.html', {"user": user,"role":"","address":v})
        else:   
            return render(request, 'Error.html')



class EditAddressPage(TemplateView):
    def get(self, request,pk=None):
        if pk:
            user=Register.objects.get(r_id=pk)
            if user.r_role=="customer":
                caddress=CustomerAddress.objects.get(user_id=pk)
                return render(request, 'EditAddress.html', {"role":"customer","address":caddress,"user":user})
            else:
                vaddress=VendorAddress.objects.get(vendor_id=pk)
                return render(request, 'EditAddress.html', {"role":"","address":vaddress,"user":user})
        else:   
            return render(request, 'Error.html')


class AssociatedUsers(TemplateView):
    def get(self,request,pk=None):
        if pk:
            user=Register.objects.get(r_id=pk)
            if user.r_role=="vendor":
                vcity=VendorAddress.objects.get(vendor_id=pk)
                with connection.cursor() as cursor:
                    cursor.execute("select r.r_id,r.r_name,r.r_email,c.* from accounts_register r JOIN dashboard_customeraddress c on r.r_id=c.user_id where r.r_role='customer' and c.city=%s",[vcity.city])
                    row=cursor.fetchall()
                return render(request, 'customer.html',{"row":row})

            else:
                return render(request,'Error.html',{"cars":"!!"})

class AssociatedCanisters(TemplateView):
    def get(self,request,pk=None):
        if pk:
            with connection.cursor() as cursor:
                cursor.execute("select c.* from dashboard_canisters c where c.register_id=%s",[pk])
                row=cursor.fetchall()
            return render(request, 'canister.html',{"row":row})
        else:
            return render(request,'Error.html')



# class displayempPage(TemplateView):
#     def get(self, request, **kwargs):
#         emp_no = request.GET['empno']
#         e_name = request.GET['empname'],
#         e_address = request.GET['empaddress']
#         emp_phone = request.GET['empphone']
#         e = employee(emp_id=emp_no, emp_name=e_name, emp_add=e_address, emp_ph=emp_phone)
#         e.save()
#         # et=m.employee.objects.all()
#         # g=m.employee.objects.get(empid=1234)
#
#         et = employee.objects.order_by('emp_id')
#         # objects.order_by('empid')
#         return render(request, 'display.html', {"et": et})
# Create your views here.
