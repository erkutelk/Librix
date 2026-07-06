from django.shortcuts import render
from rest_framework.decorators import api_view
from Book.serializer import KategoriSerializer_list,KategoriSerializer_create,KategoriSerializer_details
from rest_framework.response import Response
from Book.models import BookCategori
from rest_framework import status
from django.db.models import Q
# Create your views here.
from rest_framework.decorators import api_view, permission_classes

from User.permissions import IsAdmin

@api_view(['GET'])
@permission_classes([IsAdmin])
def all_categori(request):
    menu = BookCategori.objects.all()
    serializer = KategoriSerializer_list(menu, many=True)
    return Response(serializer.data)

# @permission_classes([IsAdmin])
@api_view(['GET'])
def get_categori(request,slug):
    try:
        kategori = BookCategori.objects.get(slug=slug)
        serializer = KategoriSerializer_details(kategori)
        return Response(serializer.data)
    except BookCategori.DoesNotExist:
        return Response({"message":"Kategori Bulunamadı"},
                        status=404)
    
# @permission_classes([IsAdmin])
@api_view(['POST'])
def insert_categori(request):
    """
    POST JSON Örneği:\n
    {
        "book_categori":str,
        "categori_isActive":bool
    }
    """
    serializer=KategoriSerializer_create(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status":"Basariyla Eklendi",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        ) 
    return Response(
        {
            'error': serializer.errors,
        },
        status=status.HTTP_400_BAD_REQUEST
    )

from rest_framework.exceptions import NotFound

# @permission_classes([IsAdmin])
@api_view(['DELETE'])
def delete_categori(request, slug):
    try:
        obj = BookCategori.objects.get(slug=slug)
        obj.delete()
        return Response(
            {'message': 'Kategori silindi'},
            status=status.HTTP_200_OK
        )
    except BookCategori.DoesNotExist:
        return Response(
            {'error': 'Kategori bulunamadı'},
            status=status.HTTP_404_NOT_FOUND
        )

# @permission_classes([IsAdmin])
@api_view(['PATCH'])
def patch_categori(request, slug):
    """
    POST JSON Örneği:\n
    {
        "book_categori":str,
        "categori_isActive":bool
    }
    """
    try:
        instance = BookCategori.objects.get(slug=slug)

        serializer = KategoriSerializer_create(
            instance,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Başarılı bir şekilde güncelleme işlemi tamamlandı',
                             'data':serializer.data}, status=200)

        return Response({'status':'Güncelleme sırasında bir hata meydana geldi',
                        'data': serializer.errors},
                        status=400)

    except BookCategori.DoesNotExist:
        return Response({'error': 'Kategori bulunamadı'}, status=404)
    
