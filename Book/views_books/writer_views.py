from django.shortcuts import render
from Book.models import Writer
from rest_framework.decorators import api_view
from Book.serializer import WriterBookSerializer_list,WriterUpdateSerializer_create
from rest_framework.response import Response
from rest_framework import status
from User.permissions import BasePermission
from rest_framework.decorators import api_view, permission_classes
from User.permissions import IsAdmin 
# Create your views here.

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
    
    return Response({"status":"hata meydana geldi",
                     "errors":serializer.errors},status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete(request,id):
    bookWriterDelete=Writer.objects.get(pk=id)
    bookWriterDelete.delete()
    return Response({"data":"başarılı bir şekilde silindi",
                     "da":bookWriterDelete.name})


@api_view(['PATCH'])
def update(request,id):
    bookWriteUpdate=Writer.objects.get(pk=id)
    """
    {
        "name": "str",
        "surname": "str",
        "isActive": bool,
    }
    """
    try:
        serializer=WriterBookSerializer_list(bookWriteUpdate,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Güncellendi",
                            "data":serializer.data})
    except Writer.DoesNotExist:
        return Response({"status":"Hata meydana geldi",
                     "erorr":serializer.error_messages})

@api_view(['GET'])
def get_first(request,id):
    try:
        models_firs=Writer.objects.get(pk=id)

    except Writer.DoesNotExist:
        return Response({"Error":"Kategori bulunamadı"},status=401)
    
    serializer=WriterBookSerializer_list(models_firs)
    return Response({'data':serializer.data})