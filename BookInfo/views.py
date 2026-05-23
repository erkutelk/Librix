from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import KategoriSerializer,KitapInfoSerializer
from rest_framework.response import Response
from .models import BookCategori

# Create your views here.

@api_view(['GET'])
def all_categori(request):
    menu = BookCategori.objects.all()
    serializer = KategoriSerializer(menu, many=True)
    return Response(serializer.data)