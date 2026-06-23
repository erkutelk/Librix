from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OduncAlmaSistemi
from .serializer import OduncAlmaSistemiSeriazlier_list,OduncAlmaSistemiCreateSerializer
from User.permissions import IsAdmin
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([IsAdmin])
def odunc_alma_get(request):
    models_odunc=OduncAlmaSistemi.objects.all()
    deger=OduncAlmaSistemiSeriazlier_list(models_odunc,many=True)
    return Response({'status':'Tüm veriler getirildi.',
                     'data':deger.data})

@api_view(['GET'])
@permission_classes([IsAdmin])
def odunc_first_id(request,id):
    models_odunc=OduncAlmaSistemi.objects.get(pk=id)
    deger=OduncAlmaSistemiSeriazlier_list(models_odunc)
    return Response({'status':"Değeri getirildi.",'data':deger.data})

@api_view(['PATCH'])
@permission_classes([IsAdmin])
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

@api_view(['POST'])
@permission_classes([IsAdmin])
def odunc_create(request):
    """
    {
        "user": id,
        "book": id,
        "teslim_edildi": boolen,
        "verecegi_tarih": "date"
    }
    """
    serializer=OduncAlmaSistemiCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'Kitap ödünç verilmiştir',"data":serializer.data})
    
    return Response({'erorr':'Hata meydana geldi'})