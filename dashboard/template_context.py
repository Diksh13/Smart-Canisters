import serial
from accounts.models import *
from dashboard.models import *
from django.db import connection
from json import dumps
from serial import Serial
import re

data={}
def get_filters(request):
    try:
        user_id=request.session['user_id']
    except:
        user_id=1
    user=Register.objects.get(r_id=user_id)
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

def strtooint(myData):
    st=str(myData)
    x = str(re.search("[A]\d*[B]\d*[C]\d*", st).group())
    a=str(re.search("[A]\d*", x).group())
    b=str(re.search("[B]\d*", x).group())
    c=str(re.search("[C]\d*", x).group())
    d=[]
    for character in a:
        if character.isdigit():
            d.append(character)
    e=''.join(d)
    valdict={'A':e}
    d.clear()
    for character in b:
        if character.isdigit():
            d.append(character)
    e=''.join(d)
    valdict.update({'B':e})
    d.clear()
    for character in c:
        if character.isdigit():
            d.append(character)
    e=''.join(d)
    valdict.update({'C':e})
    d.clear()
    print(valdict)
    return valdict     

def abc(request):
    while True:
        arduinoSerialData=serial.Serial('/dev/ttyACM0',9600)
        while(1==1):
            if(arduinoSerialData.inWaiting()>0):
                myData = arduinoSerialData.readline()
                print(myData)
                dataint={}
                dataint=strtooint(myData)
                max=12
                if int(dataint.get('A')) >=3 and int(dataint.get('A')) <=12:
                    canister_val=((12-int(dataint.get('A')))/max)*(max*10)
                    print(canister_val)
                    with connection.cursor() as cursor:
                        cursor.execute("update dashboard_canisters set c_actual_amount=%s where register_id=1 and grocery_id=1",[canister_val])
                if int(dataint.get('B')) >=3 and int(dataint.get('B')) <=12:
                    canister_val=((12-int(dataint.get('B')))/max)*(max*10)
                    print(canister_val)
                    with connection.cursor() as cursor:
                        cursor.execute("update dashboard_canisters set c_actual_amount=%s where register_id=1 and grocery_id=2",[canister_val])
                if int(dataint.get('C')) >=3 and int(dataint.get('C')) <=12:
                    canister_val=((12-int(dataint.get('C')))/max)*(max*10)
                    print(canister_val)
                    with connection.cursor() as cursor:
                        cursor.execute("update dashboard_canisters set c_actual_amount=%s where register_id=1 and grocery_id=3",[canister_val])
                
                data = {'x':'abx'}
                return data

