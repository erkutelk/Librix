from django.shortcuts import render
from .models import UserInfo
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from User.permissions import IsAdmin
from .serializer import RegisterSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])#Giriş yapan kullanıcı görsün diyoruz
def profile(request):
    user = request.user
    return Response({
        "username": user.username,
        "last_name": user.last_name,
        "phone":str(user.phone),
        "role":user.role
    })

User = get_user_model()
@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Kullanıcı oluşturuldu"})

    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAdmin])
def liste(request):
    users = User.objects.all()
    
    data = []
    for user in users:
        data.append({
            "id": user.id,
            "username": user.username,
            "last_name":user.last_name,
            "role":user.role
        })
    print(data)
    return Response(data)



@api_view(['PATCH'])
@permission_classes([IsAdmin])
def deactive_user(request,id):
    user=UserInfo.objects.get(pk=id)
    user.is_active=False
    user.save()
    return Response({'status':'Kullanıcı pasif hale getirildi'})

