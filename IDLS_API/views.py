# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import os
from IDLS_API.models import Measurement, Production
from IDLS_API.models import Coordination
from django.db import connection, transaction
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

# Create your views here.
@csrf_exempt
def api_handler(request):
    if(request.POST):
        income_data = json.loads(request.body)
        now = datetime.now()
        BSSID_i = income_data['bssid']
        SSID_i = income_data['ssid']
        RSSI_i = float(income_data['rssi'])
        Location_ID_i = income_data['loc_id']
        Time_i = now.strftime("%d/%m/%Y %H:%M:%S")

        Mes = Measurement(BSSID = BSSID_i, SSID = SSID_i, RSSI = RSSI_i, 
        Location_ID = Location_ID_i, Time = Time_i)
        Mes.save()

        #return HttpResponse('OK')
        return HttpResponse(BSSID_i, RSSI_i)
    return HttpResponse('Bạn đã bị nhiễm covid 19')

@csrf_exempt
def api_handler_mobile(request):
    if(request.POST):
        income_data = json.loads(request.body)
        now = datetime.now()
        BSSID_i = income_data['bssid']
        SSID_i = income_data['ssid']
        RSSI_i = float(income_data['rssi'])
        Location_ID_i = income_data['loc_id']
        Time_i = now.strftime("%d/%m/%Y %H:%M:%S")

        prod = Production(BSSID = BSSID_i, SSID = SSID_i, RSSI = RSSI_i, 
        Location_ID = Location_ID_i, Time = Time_i)
        prod.save()

        return HttpResponse('OK')
    return HttpResponse('hehe')