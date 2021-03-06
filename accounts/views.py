from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from accounts.models import *
from dashboard.models import *
from datetime import datetime
from django.db import connection
from json import dumps
# import requests
from django.contrib import messages

class IndexPage(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'index.html', context=None)


# class LoginPage(TemplateView):
#     def post(self,request,**kwargs):
#         if Register.objects.filter(r_email=request.POST['your_email'],r_password=request.POST['password']).exists():
#             # if credentials are correct
#             user=Register.objects.get(r_email=request.POST['your_email'])
#             request.session['user_id']=user.r_id
#             request.session['user_role']=user.r_role
#             login_time=datetime.now()
#             if(user.last_login is None):
#                 user.last_login=login_time
#                 user.save()
#                 if user.r_role=="customer":
#                     messages.success(request, 'Login Successful as Customer. Now You can complete your details to go ahead.')
#                     return render(request, 'address.html', {"role": "customer","u_email":user.r_email,"user":user})
#                 else:
#                     messages.success(request, 'Login Successful as Vendor. Now You can complete your details to go ahead.')
#                     return render(request, 'address.html', {"role":"","u_email":user.r_email,"user":user})
                
#             else:
#                 user.last_login=login_time
#                 user.save()
#                 if user.r_role=="customer":
#                     return render(request, 'dashboard.html', {"user":user,"role":"customer"})
#                 else:
#                     return render(request, 'dashboard.html', {"user":user,"role":""})


#         else:
#             messages.error(request, 'Invalid ID/Password')
#             return redirect(request.META['HTTP_REFERER'])
        
        
            

 

class LoginPage(TemplateView):
    def post(self, request, **kwargs):
        if Register.objects.filter(r_email=request.POST['your_email'],r_password=request.POST['password']).exists():
            # if credentials are correct
            user=Register.objects.get(r_email=request.POST['your_email'])
            login_time=datetime.now()
            # saving login details
            # login=Login(username=user.r_email,password=user.r_password,login_time=login_time)
            # login.save()
            request.session['user_id']=user.r_id
            request.session['user_role']=user.r_role
            
            # if(user.last_login is None):
            #     user.last_login=login_time
            #     user.save()
            #     return render(request,"address.html")
            # else:
            #     user.last_login=login_time
            #     user.save()
            #     return render(request,"dashboard.html")


            # print(request.session['user_id'],request.session['user_role'])
            #normal login
            # if Login.objects.filter(username=request.POST['your_email']).count()>1:
            if(user.last_login is not None):
                user.last_login=login_time
                user.save()
                if user.r_role=="customer":
                    return render(request, 'dashboard.html', {"user":user,"role":"customer"})
                else:
                    with connection.cursor() as cursor:
                        #for fetching no. of customers
                        vcity=VendorAddress.objects.get(vendor_id=user.r_id)
                        cursor.execute("select r.r_id,r.r_name,r.r_email,c.* from accounts_register r JOIN dashboard_customeraddress c on r.r_id=c.user_id where r.r_role='customer' and c.city=%s",[vcity.city])
                        row=cursor.fetchall()
                        count_of_customers=len(row)
                        if count_of_customers > 0:

                        #for fetching customer_id in order to fetch canister details of all customers
                            customers_id=[]
                            for i in row:
                                customers_id.append(i[0])
                        
                        #for fetching canister details of all customers
                            canister_details=[]
                            alerts=[]
                            for i in customers_id:
                                cursor.execute("select r.r_name,c.c_name,c.c_actual_amount from accounts_register r JOIN dashboard_canisters c on r.r_id=c.register_id where c.register_id=%s",[i])
                                row=cursor.fetchall()
                                canister_details.append(row)
                                datajson=dumps(canister_details)
                                cursor.execute("select a.grocery,r.r_name from dashboard_alert a,accounts_register r where a.register=r.r_id and a.register=%s",[i])
                                alert=cursor.fetchall()
                                if alert:
                                    alerts.append(alert)

                            #count_of_alerts
                            count=0
                            for i in alerts:
                                for j in i:
                                    count=count+1

                            #count_of_vendors
                            cursor.execute("select count(*) from accounts_register where r_role='vendor'")
                            count_vendor=cursor.fetchone()
                            

                        
                        #for fetching Alerts & Notifications
                        # cursor.execute("select a.grocery,r.r_name from dashboard_alert a,accounts_register r where a.register=r.r_id")

                            return render(request, 'dashboard.html', {"user":user,"role":"","row":row,"count_of_customers":count_of_customers,"count_of_alerts":count,"count_vendor":count_vendor[0],"data":datajson,"alert":alerts})
                        else:
                            with connection.cursor() as cursor:
                                #count_of_vendors
                                cursor.execute("select count(*) from accounts_register where r_role='vendor'")
                                count_vendor=cursor.fetchone()

                            return render(request, 'dashboard.html', {"user":user,"role":"","row":row,"count_of_customers":count_of_customers,"count_of_alerts":"0","count_vendor":count_vendor[0],"data":"","alert":""})

            #logging in for the first time
            else:
                user.last_login=login_time
                user.save()
                if user.r_role=="customer":
                    messages.success(request, 'Login Successful as Customer. Now You can complete your details to go ahead.')
                    return render(request, 'address.html', {"role": "customer","u_email":user.r_email,"user":user})
                else:
                    messages.success(request, 'Login Successful as Vendor. Now You can complete your details to go ahead.')
                    return render(request, 'address.html', {"role":"","u_email":user.r_email,"user":user})


        else:
            messages.error(request, 'Invalid ID/Password')
            return redirect(request.META['HTTP_REFERER'])
        

        

class RegisterPage(TemplateView):
    def post(self, request, **kwargs):
        name = request.POST['full_name_1']
        email = request.POST['your_email_1']
        contact=request.POST['contact']
        password = request.POST['password_1']
        role = request.POST['your_role']
        l = Register(r_name=name, r_email=email, r_password=password, r_role=role,r_contact=contact)
        l.save()
        messages.success(request, 'Registered Successfully')
        return render(request, 'index.html')





























# class displayempPage(TemplateView):
#     def get(self, request, **kwargs):
#         emp_no = request.GET['empno']
#         e_name = request.GET['empname']
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
