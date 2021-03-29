from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from IDLS_API.models import Measurement
from IDLS_API.api.serializers import serialMes
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@api_view(['GET', 'POST']) #idls-server.herokuapp.com/idls_api/api/mes/mobile_handler
#@csrf_exempt
def mobile_handler(request):
    if(request.method == 'GET'):
        Measure = Measurement.objects.all()
        serial = serialMes(Measure, many=True)
        return Response(serial.data)
        #return Response(serials.data, status=status.HTTP_201_CREATED)
    elif(request.method == 'POST'):
        serials = serialMes(data=request.data)
        if(serials.is_valid()):
            serials.save()
            return JsonResponse(serials.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serials.errors, status=status.HTTP_400_BAD_REQUEST)



