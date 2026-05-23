from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import KategoriSerializer,KitapInfoSerializer
from rest_framework.response import Response
from .models import BookCategori
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def all_categori(request):
    menu = BookCategori.objects.all()
    serializer = KategoriSerializer(menu, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def insert_categori(request):
    """
    POST JSON Örneği:\n
    {
        "book_categori":str,
        "categori_isActive":bool
    }
    """
    serializer=KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({'hata':f'Masa eklenirken hata meydana geldi{serializer.data}'},status=status.HTTP_400_BAD_REQUEST)