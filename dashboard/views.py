from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import CustomerAddress
from accounts.models import Register
class DashboardPage(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html', context=None)


class AddressPage(TemplateView):
    def post(self, request, **kwargs):
        user_email=Register.objects.get(r_email=request.POST['email'])
        house_no = request.POST['house-no']
        apartment = request.POST['apartment']
        street = request.POST['street']
        landmark = request.POST['landmark']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        c = CustomerAddress(c_house_no=house_no, c_apartment=apartment, c_street=street, c_landmark=landmark,
                            c_city=city, c_state=state, c_country=country, c_pincode=pincode,user=user_email)
        c.save()
        return render(request, 'dashboard.html', {"et": user_email})

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
