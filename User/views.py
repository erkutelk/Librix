from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import UserInfo
from .serializer import UserSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def liste(request):
    menu = UserInfo.objects.all()
    serializer = UserSerializer(menu, many=True)
    return Response(serializer.data)


