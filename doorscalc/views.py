from django.http import HttpResponse
from django.template import loader
from .models import Door, Discount, Order
from .forms import DoorForm, OrderForm
from django.views import View
from django.http import JsonResponse
from django.core import serializers
import math
import datetime
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import ast
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def email():    
    email = EmailMessage('Subject', 'Body', to=['mateusz.ignatowicz@icloud.com'])
    email.send()
    print('something happened')
# def doors_list(request):
#     doors_objects = Door.objects.all()
#     template = loader.get_template('doorscalc/index.html')
#     context = {
#         'doors_objects': doors_objects,
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    template = loader.get_template('index/index.html')
    date = datetime.datetime.now()
    context = {
        'date': date,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/")
def doors_list(request):

    calc_form = DoorForm()
    ord_form = OrderForm()
    doors_objects = Door.objects.order_by('code')
    user_order = Order.objects.filter(user=request.user).order_by('-data')
    template = loader.get_template('doorscalc/index.html')

    handles = Order.objects.values_list('handle_site')
    context = {
        'doors_objects': doors_objects,
        'calc_form': calc_form,
        'ord_form': ord_form,
        'user_order': user_order,
        'handles': handles,

    }
    return HttpResponse(template.render(context, request))

def ajax(request):

    if request.method == 'POST':
        c = request.POST.get('code', 'None')
        w = request.POST.get('width', 'None')
        h = request.POST.get('height', 'None')
        d = request.POST.get('depth', 'None')

        selected_doors = Door.objects.get(pk=c) 

        formula = eval(selected_doors.formula)
        ob_formula = eval(selected_doors.ob_formula)
        nosna_max_ = eval(str(selected_doors.nosna_max))
        nosna_ = eval(selected_doors.nosna)
        nosna = float(nosna_/1000000)

        m2 = formula/1000000
        netprice = round(m2*float(selected_doors.multiplier))
        discount = float(selected_doors.discount.discount/100)
        discount_price = round(float(netprice-(netprice*discount)))
        ob = ob_formula/1000
        obx = round(ob,1)
        obxp = 0.5 * math.ceil(2.0 * obx)
        obxpp = obxp*5
        checked = selected_doors.gasket

        data = {}

        data['nosna'] = nosna
        data['maxm2'] = selected_doors.nosna_max

        def compare(n,m):
            if n <= m:
                return True
            else:
                return False

        isvalid = compare(nosna, selected_doors.nosna_max)
        data['isvalid'] = isvalid

        if not checked:
            data['gasket'] = 'not included'
            calcall = netprice+obxpp
            data['final_price'] = round(calcall-(calcall*discount))
        else:
            data['gasket'] = 'included'
            data['final_price'] = discount_price

        data['formula'] = selected_doors.formula
        data['m2'] = m2
        data['netprice'] = netprice
        data['discount'] = selected_doors.discount.discount
        data['discount2'] = discount
        data['discount_price'] = discount_price
        data['obx'] = obx
        data['obxp'] = obxp
        data['obxpp'] = obxpp
        return JsonResponse(data)

@csrf_exempt
def ajax_ord(request):
    if request.method == 'POST':

        w = request.POST.get('width', 'None')
        h = request.POST.get('height', 'None')
        d = request.POST.get('depth', 'None')
        t = request.POST.get('code', 'None')

        # konwersja typow danych do nowego slownika
        converted = {}
        payload = {}
        payload2 = {}
        converted2 = {}

        for key, values in request.POST.items():
            converted[key] = values
            payload[key] = values

        for i, v in converted.items():
            try:
                converted2[i] = ast.literal_eval(v)
                payload[i] = ast.literal_eval(v)
            except ValueError:
                pass

        json_payload = json.dumps(converted)
        json_payload2 = json.loads(json_payload)

        payload['payload2'] = payload2
        payload['converted'] = converted2
        payload['json_payload'] = json_payload
        payload['json_payload2'] = json_payload2
        payload['sent'] = 'sent'
        # instancja
        form = OrderForm(request.POST)


        if form.is_valid():
            # stworz obiekt i instancje
            obj = form.save(commit=False) # poczekaj z zapisem
            obj.user = request.user # wrzuć aktualnie zalogowanego usera do pola form.user
            obj.w = converted.get("width", "") # wrzuć reszte do pól
            obj.h = converted.get("height", "")
            obj.data = datetime.date.today

            if d is None:
                payload['error'] = 'd is None'
            elif type(d) is str:
                payload['error'] ='d is string!'
                if d != "None":
                    obj.d = int(d)
            obj.door = Door.objects.get(pk=t) #wybierz dzwi z modelu Door po kodzie id.
            obj.save() # zapisz

            print('SENT!')
        return JsonResponse(payload) # wyślij payload

def delete_order(request):
    responce = {}
    if request.method == 'POST':
        order_id = request.POST.get('id', 'None')
        ord_id = int(order_id)
        query = Order.objects.get(pk=ord_id)    
        query.delete()
        responce['status'] = 'Deleted!'
    else:
        responce['status'] = 'error'
    return JsonResponse(responce)

    # query = Order.objects.get(pk=order_pk)
    # query.delete()
    # return HttpResponse("Deleted!")
def ajax_calc(request):
    payload = {}
    if request.method == 'POST':
        for key, values in request.POST.items():
            payload[key] = values



        c = request.POST.get('door', 'None')
        w = request.POST.get('w', 'None')
        h = request.POST.get('h', 'None')
        d = request.POST.get('d', 'None')

        selected_doors = Door.objects.get(pk=c) 

        formula = eval(selected_doors.formula)
        ob_formula = eval(selected_doors.ob_formula)
        nosna_max_ = eval(str(selected_doors.nosna_max))
        nosna_ = eval(selected_doors.nosna)
        nosna = float(nosna_/1000000)

        m2 = formula/1000000
        netprice = round(m2*float(selected_doors.multiplier))
        discount = float(selected_doors.discount.discount/100)
        discount_price = round(float(netprice-(netprice*discount)))
        ob = ob_formula/1000
        obx = round(ob,1)
        obxp = 0.5 * math.ceil(2.0 * obx)
        obxpp = obxp*5
        checked = selected_doors.gasket

        json = {}

        json['nosna'] = nosna
        json['maxm2'] = selected_doors.nosna_max

        def compare(n,m):
            if n <= m:
                return True
            else:
                return False

        isvalid = compare(nosna, selected_doors.nosna_max)
        json['isvalid'] = isvalid

        if not checked:
            json['gasket'] = 'not included'
            calcall = netprice+obxpp
            json['final_price'] = round(calcall-(calcall*discount))
        else:
            json['gasket'] = 'included'
            json['final_price'] = discount_price

        json['formula'] = selected_doors.formula
        json['m2'] = m2
        json['netprice'] = netprice
        json['discount'] = selected_doors.discount.discount
        json['discount2'] = discount
        json['discount_price'] = discount_price
        json['obx'] = obx
        json['obxp'] = obxp
        json['obxpp'] = obxpp

        return JsonResponse(json)
@csrf_exempt
def ajax_ord2(request):

    d = request.POST.get('depth', 'None')

    payload = {}

    if request.method == 'POST':
        payload['if_post'] = "OK"
        form = OrderForm(request.POST)
        if form:
            payload['if_form'] = "OK"
        if form.is_valid():
            payload['if_valid'] = "OK"
            obj = form.save(commit=False) # poczekaj z zapisem
            obj.user = request.user # wrzuć aktualnie zalogowanego usera do pola form.user
            if d is None:
                payload['error'] = 'd is None'
            elif type(d) is str:
                payload['error'] ='d is string!'
                if d != "None":
                    obj.d = int(d)
            obj.save() # zapisz
        else:
            payload['if_valid'] = "NO"  
    else:
        form = OrderForm()
        payload['saved'] = False
        payload['if_post'] = False

    return JsonResponse(payload) # wyślij payload