from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from accounts.models import *
from dashboard.models import *
from datetime import datetime
from django.db import connection
from json import dumps


class IndexPage(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'index.html', context=None)
 

class LoginPage(TemplateView):
    def post(self, request, **kwargs):
        if Register.objects.filter(r_email=request.POST['your_email'],r_password=request.POST['password']).exists():
            # if credentials are correct
            user=Register.objects.get(r_email=request.POST['your_email'])
            login_time=datetime.now()
            # saving login details
            login=Login(username=user.r_email,password=user.r_password,login_time=login_time)
            login.save()
            #normal login
            if Login.objects.filter(username=request.POST['your_email']).count()>1:
                if user.r_role=="customer":
                    return render(request, 'dashboard.html', {"user":user,"role":"customer"})
                else:
                    with connection.cursor() as cursor:
                        #for fetching no. of customers
                        vcity=VendorAddress.objects.get(vendor_id=user.r_id)
                        cursor.execute("select r.r_id,r.r_name,r.r_email,c.* from accounts_register r JOIN dashboard_customeraddress c on r.r_id=c.user_id where r.r_role='customer' and c.city=%s",[vcity.city])
                        row=cursor.fetchall()
                        count_of_customers=len(row)

                        #for fetching customer_id in order to fetch canister details of all customers
                        customers_id=[]
                        for i in row:
                            customers_id.append(i[0])
                        
                        #for fetching canister details of all customers
                        canister_details=[]
                        for i in customers_id:
                            cursor.execute("select r.r_name,c.c_name,c.c_actual_amount from accounts_register r JOIN dashboard_canisters c on r.r_id=c.register_id where c.register_id=%s",[i])
                            row=cursor.fetchall()
                            canister_details.append(row)
                            datajson=dumps(canister_details)

                    return render(request, 'dashboard.html', {"user":user,"role":"","row":row,"count_of_customers":count_of_customers,"data":datajson})

            #logging in for the first time
            else:
                if user.r_role=="customer":
                    return render(request, 'address.html', {"role": "customer","u_email":user.r_email,"user":user})
                else:
                    return render(request, 'address.html', {"role":"","u_email":user.r_email,"user":user})


        else:
            return render(request, 'index.html', {"et":"Invalid ID/Password"})


        

class RegisterPage(TemplateView):
    def post(self, request, **kwargs):
        name = request.POST['full_name_1']
        email = request.POST['your_email_1']
        password = request.POST['password_1']
        role = request.POST['your_role']
        l = Register(r_name=name, r_email=email, r_password=password, r_role=role)
        l.save()
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
