from django.shortcuts import render
from .models import Writer
from rest_framework.decorators import api_view
from .serializer import WriterBookSerializer_list
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def get(request):
    models=Writer.objects.all()
    serializer=WriterBookSerializer_list(models,many=True)
    return Response({"data":serializer.data})


@api_view(['POST'])
def add(request):
    serializer=WriterBookSerializer_list(data=request.data)

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
    """
    {
        "name": "str",
        "surname": "str",
        "isActive": bool,
        "dateAdd": "2026-06-12T00:59:33.754593Z"
    }
    """
    bookWriteUpdate=Writer.objects.get(pk=id)

    serializer=WriterBookSerializer_list(bookWriteUpdate,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({"status":"Güncellendi",
                         "data":serializer.data})
