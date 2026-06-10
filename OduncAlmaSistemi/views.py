from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OduncAlmaSistemi
from .serializer import OduncAlmaSistemiSeriazlier
# Create your views here.

@api_view(['GET'])
def odunc_alma_get(request):
    models_odunc=OduncAlmaSistemi.objects.all()
    deger=OduncAlmaSistemiSeriazlier(models_odunc,many=True)
    return Response({'status':'true',
                     'data':deger.data})