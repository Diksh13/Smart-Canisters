from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from accounts.models import *
from datetime import datetime


# from emp.models import employee
# from emp import views
class IndexPage(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'index.html', context=None)


# if User.objects.filter(username=request.POST['username'], 
#             password=request.POST['password']).exists():
#             global user
#             user = User.objects.get(username=request.POST['username'], 
#             password=request.POST['password'])


#             act = User.objects.get(id=user.id)
#             act.login_time = datetime.now()
#             act.save()
#             return render(request, 'dash.html', {'user': user, })

class LoginPage(TemplateView):
    def post(self, request, **kwargs):
        if Register.objects.filter(r_email=request.POST['your_email'],r_password=request.POST['password']).exists():
            global user
            user=Register.objects.get(r_email=request.POST['your_email'])
            login_time=datetime.now()
            login=Login(username=user.r_email,password=user.r_password,login_time=login_time)
            login.save()
            if Login.objects.filter(username=request.POST['your_email']).count()>1:
                return render(request, 'dashboard.html', {"u_email":user.r_email})
            else:
                if user.r_role=="customer":
                    return render(request, 'address.html', {"role": "customer","u_email":user.r_email})
                else:
                    return render(request, 'address.html', {"role":"","u_email":user.r_email})
        else:
            return render(request, 'index.html', {"et":"Invalid ID/Password"})
        



        # email = request.POST['your_email']
        # password = request.POST['password']
        # g = Register.objects.get(r_email=email)
        # if g.r_password==password:
            
        #     if g.r_role=="customer":
        #         return render(request, 'address.html', {"role": "customer","u_email":email})
        #     else:
        #         return render(request, 'address.html', {"role":"","u_email":email})
        # else:
        #     return render(request, 'index.html', {"et":"Invalid ID/Password"})
        


class RegisterPage(TemplateView):
    def post(self, request, **kwargs):
        name = request.POST['full_name_1']
        email = request.POST['your_email_1']
        password = request.POST['password_1']
        role = request.POST['your_role']
        l = Register(r_name=name, r_email=email, r_password=password, r_role=role)
        l.save()
        return render(request, 'index.html', context=None)





























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
