from django.shortcuts import render
from .models import UserInfo
from OduncAlmaSistemi.models import OduncAlmaSistemi
from OduncAlmaSistemi.serializer import OduncAlmaSistemiSeriazlier_list
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from User.permissions import IsAdmin
from .serializer import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])#Giriş yapan kullanıcı görsün diyoruz
def profile(request):
    user = request.user
    return Response({
        "username": user.username,
        "last_name": user.last_name,
        "phone":str(user.phone),
        "mail":user.email,
        "role":user.role
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])#Giriş yapan kullanıcı görsün diyoruz
def kullanicinin_aldigi_kitaplar(request):
    user=request.user
    models_odunc = OduncAlmaSistemi.objects.filter(user=user.id)
    if not models_odunc.exists():
        return Response(
            {"message": "Henüz ödünç aldığınız kitap bulunmuyor."},
            status=status.HTTP_200_OK
        )
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(models_odunc, request)
    serializer=OduncAlmaSistemiSeriazlier_list(result_page,many=True)
    return paginator.get_paginated_response(serializer.data)


User = get_user_model()
@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Kullanıcı oluşturuldu"})

    return Response(serializer.errors, status=400)

# @permission_classes([IsAdmin])
@api_view(['GET'])
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
    return Response(data)



# @permission_classes([IsAdmin])
@api_view(['PATCH'])
def deactive_user(request,id):
    user=UserInfo.objects.get(pk=id)
    user.is_active=False
    user.save()
    return Response({'status':'Kullanıcı pasif hale getirildi'})

