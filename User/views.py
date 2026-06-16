from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import UserInfo
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from User.permissions import IsAdmin
@api_view(['GET'])
def profile(request):
    user = request.user

    return Response({
        "username": user.username,
        "phone": user.phone,
        "id": user.id
    })

User = get_user_model()
# Create your views here.
@api_view(['POST'])
def register(request):
    data = request.data

    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        phone=data.get('phone'),
        relative_id_number=data.get('relative_id_number')
    )

    return Response({"message": "Kullanıcı oluşturuldu"})


@api_view(['GET'])
@permission_classes([IsAdmin])
def liste(request):
    users = User.objects.all()

    data = []
    for user in users:
        data.append({
            "id": user.id,
            "username": user.username,
            "phone": user.phone
        })

    return Response(data)

@api_view(['GET'])
@permission_classes([IsAdmin])
def liste(request):
    menu = UserInfo.objects.all()
    serializer = UserSerializer(menu, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAdmin])
def deactive_user(request,id):
    user=UserInfo.objects.get(pk=id)
    user.is_active=False
    user.save()
    return Response({'status':'Kullanıcı pasif hale getirildi'})