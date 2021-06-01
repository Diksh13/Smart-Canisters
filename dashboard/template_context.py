from accounts.models import *
from dashboard.models import *
from django.db import connection
from json import dumps


def get_filters(request):
    user_id=request.session['user_id']
    user=Register.objects.get(r_id=request.session['user_id'])
    if user.r_role == "customer":
        role="customer"
    else:
        role=""
    
    with connection.cursor() as cursor:
        cursor.execute("select * from dashboard_canisters where register_id=%s",[user.r_id])
        canister=cursor.fetchall()
    canister_count=len(canister)
    canister_datajson=dumps(canister)
    # with connection.cursor() as cursor:
    #     #for fetching no. of customers
    #     vcity=VendorAddress.objects.get(vendor_id=user_id)
    #     cursor.execute("select r.r_id,r.r_name,r.r_email,c.* from accounts_register r JOIN dashboard_customeraddress c on r.r_id=c.user_id where r.r_role='customer' and c.city=%s",[vcity.city])
    #     row=cursor.fetchall()
    #     count_of_customers=len(row)

    #     #for fetching customer_id in order to fetch canister details of all customers
    #     customers_id=[]
    #     for i in row:
    #         customers_id.append(i[0])
                        
    #     #for fetching canister details of all customers
    #     canister_details=[]
    #     alerts=[]
    #     for i in customers_id:
    #         cursor.execute("select r.r_name,c.c_name,c.c_actual_amount from accounts_register r JOIN dashboard_canisters c on r.r_id=c.register_id where c.register_id=%s",[i])
    #         row=cursor.fetchall()
    #         canister_details.append(row)
    #         datajson=dumps(canister_details)
    #         cursor.execute("select a.grocery,r.r_name from dashboard_alert a,accounts_register r where a.register=r.r_id and a.register=%s",[i])
    #         alert=cursor.fetchall()
    #         if alert:
    #             alerts.append(alert)

    # data={"user_id":user_id,
    # "row":row,"count_of_customers":count_of_customers,"data":datajson,"alert":alerts
    # }
    data={'mes':'hello','user_id':user_id,'user':user,'role':role,'canister':canister,'canister_count':canister_count,'canister_datajson':canister_datajson}
    return data
    # return True