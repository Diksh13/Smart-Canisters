from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from accounts.models import Register


# from emp.models import employee
# from emp import views
class IndexPage(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'index.html', context=None)

class LoginPage(TemplateView):
    def post(self, request, **kwargs):
        email = request.POST['your_email']
        password = request.POST['password']
        try:
            g = Register.objects.get(r_email=email)
            if g.r_password==password:
                name=g.r_name
                return render(request, 'address.html', {"role":g.r_role,"name": name,"u_email":email})
            else:
                return render(request, 'index.html', {"et":"Invalid ID/Password"})
        except:
            return render(request, 'index.html', {"et": "Invalid ID/Password"})


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
