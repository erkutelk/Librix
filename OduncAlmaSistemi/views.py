from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OduncAlmaSistemi
from .serializer import OduncAlmaSistemiSeriazlier_list
# Create your views here.

@api_view(['GET'])
def odunc_alma_get(request):
    models_odunc=OduncAlmaSistemi.objects.all()
    deger=OduncAlmaSistemiSeriazlier_list(models_odunc,many=True)
    return Response({'status':'true',
                     'data':deger.data})

@api_view(['GET'])
def odunc_first_id(request,id):
    models_odunc=OduncAlmaSistemi.objects.get(pk=id)
    deger=OduncAlmaSistemiSeriazlier_list(models_odunc)
    return Response({'status':"true",'data':deger.data})

@api_view(['PATCH'])
def odunc_alma_guncelleme(request, id):
    obj = OduncAlmaSistemi.objects.get(id=id)

    serializer = OduncAlmaSistemiSeriazlier_list(
        obj,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response({
            "mesaj": "Güncellendi",
            "data": serializer.data
        })

    return Response(serializer.errors)