from django.core.checks.messages import Error
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from .models import *
from accounts.models import *
from accounts.views import LoginPage
from accounts import views
from django.db import connection
from json import dumps

from django.contrib import messages



class DashboardPage(TemplateView):
    def get(self, request, pk=None):
        return render(request, 'Error.html', context=None)


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
                messages.success(request, 'Address updated successfully')
                return redirect(request.META['HTTP_REFERER'])
                # return render(request, 'dashboard.html', {"user": user,"role":user.r_role,"address":c})
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
                messages.success(request, 'Address updated successfully')
                # return render(request, 'dashboard.html', {"user": user,"role":"","address":v})
                return redirect(request.META['HTTP_REFERER'])
        else:   
            return render(request, 'Error.html')



class EditAddressPage(TemplateView):
    def get(self, request,pk=None):
        if pk:
            user=Register.objects.get(r_id=pk)
            with connection.cursor() as cursor:
                    if user.r_role=="customer":
                        cursor.execute("select * from dashboard_customeraddress where user_id=%s",[pk])
                        row=cursor.fetchone()
                        return render(request, 'EditAddress.html', {"role":"customer","address":row,"user":user})
                    else:
                        cursor.execute("select * from dashboard_vendoraddress where vendor_id=%s",[pk])
                        row=cursor.fetchone()
                        print(row)
                        
                        return render(request, 'EditAddress.html', {"role":"","address":row,"user":user})
        else:   
            return render(request, 'Error.html')


class AssociatedUsers(TemplateView):
    def get(self,request,pk=None):
        if pk:
            user=Register.objects.get(r_id=pk)
            if user.r_role=="vendor":
                vcity=VendorAddress.objects.get(vendor_id=pk)
                with connection.cursor() as cursor:
                    cursor.execute("select r.r_id,r.r_name,r.r_email,r_contact,c.* from accounts_register r JOIN dashboard_customeraddress c on r.r_id=c.user_id where r.r_role='customer' and c.city=%s",[vcity.city])
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
                cursor.execute("select c.c_name,c.c_actual_amount from dashboard_canisters c where c.register_id=%s",[pk])
                row1=cursor.fetchall()
                datajson=dumps(row1)
        
                
            return render(request, 'canister.html',{"row":row,"data":datajson})
        else:
            return render(request,'Error.html')



class Grocery(TemplateView):
    def get(self,request,pk=None):
        with connection.cursor() as cursor:
            cursor.execute("select * from dashboard_grocery")
            grocery=cursor.fetchall()
            # grocery=Grocery.objects.all()
        return render(request, 'grocery.html',{"grocery":grocery})


class Profile(TemplateView):
    def get(self,request,pk=None):
        if pk:
            with connection.cursor() as cursor:
                cursor.execute("select * from accounts_register where r_id=%s",[pk])
                profile=cursor.fetchone()
            return render(request,'profile.html',{"profile":profile})
        else:
            return render(request,'Error.html')

class UpdateProfile(TemplateView):
    def post(self,request,pk=None):
        if pk:
            profile=Register.objects.get(r_id=pk)
            profile.r_name= request.POST['username']
            profile.r_password = request.POST['pwd'] 
            profile.r_contact=request.POST['contact']
            profile.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(request.META['HTTP_REFERER'])
        else:   
            return render(request, 'Error.html')


class VendorProfile(TemplateView):
    def get(self,request,pk=None):
        c=CustomerAddress.objects.get(user_id=pk)
        with connection.cursor() as cursor:
            cursor.execute("select r.r_name,r.r_contact,v.* from accounts_register r,dashboard_vendoraddress v where v.city=%s and v.vendor_id=r.r_id",[c.city])
            row=cursor.fetchone()
            print(row)
        return render(request,'vendor_profile.html',{'vendor':row})
           




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
