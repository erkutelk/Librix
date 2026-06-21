from django.shortcuts import render
from Book.models import Writer
from rest_framework.decorators import api_view
from Book.serializer import WriterBookSerializer_list,WriterUpdateSerializer_create,WriterUpdateSerializer_update
from rest_framework.response import Response
from rest_framework import status
from User.permissions import BasePermission
from rest_framework.decorators import api_view, permission_classes
from User.permissions import IsAdmin 
# Create your views here.
from django.db.models import Q


@api_view(['GET'])
def get(request):
    models=Writer.objects.all()
    serializer=WriterBookSerializer_list(models,many=True)
    return Response({"data":serializer.data})


# @permission_classes([IsAdmin])
@api_view(['POST'])
def add(request):
    serializer=WriterUpdateSerializer_create(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"status":"Başarıyla yeni yazar eklendi",
                         "data":serializer.data},status=201)
    
    return Response({"errors":serializer.errors},status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete(request, id):
    try:
        writer = Writer.objects.get(pk=id)
        writer.delete()
        return Response({"status": "silindi"}, status=200)

    except Writer.DoesNotExist:
        return Response({"error": "bulunamadı"}, status=404)


@api_view(['PATCH'])
def update(request, id):
    try:
        bookWriteUpdate = Writer.objects.get(pk=id)

        serializer = WriterUpdateSerializer_update(
            bookWriteUpdate,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "Güncellendi",
                "data": serializer.data
            }, status=200)

        return Response({"errors": serializer.errors}, status=400)

    except Writer.DoesNotExist:
        return Response({"status": "bulunamadı"}, status=404)

@api_view(['GET'])
def get_first(request,id):
    try:
        models_firs=Writer.objects.get(pk=id)

    except Writer.DoesNotExist:
        return Response({"Error":"yazar bulunamadı"},status=401)
    
    serializer=WriterBookSerializer_list(models_firs)
    return Response({'data':serializer.data})

@api_view(['GET'])
def search(request,name):
    arama=Writer.objects.filter(Q(name__icontains=name) | Q(surname__icontains=name))
    if arama.exists():
        serializer = WriterBookSerializer_list(arama, many=True)
        return Response({'status':'başarıyla bulundu',
                        'data':serializer.data,
                        'Adet':f'{len(serializer.data)} kayıt bulundu',},
                        status=status.HTTP_302_FOUND)
    
    else:
        return Response({'erorr':'Kitap bulunamadı',
                         'data':[]},status=status.HTTP_404_NOT_FOUND)
    