from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import KategoriSerializer,KitapInfoSerializer
from rest_framework.response import Response
from .models import BookCategori,BookInfo
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def all_categori(request):
    menu = BookCategori.objects.all()
    serializer = KategoriSerializer(menu, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_categori(request,slug):
    try:
        kategori = BookCategori.objects.get(slug=slug)
        serializer = KategoriSerializer(kategori)
        return Response(serializer.data)
    except BookCategori.DoesNotExist:
        return Response({"message":"Kategori Bulunamadı"},
                        status=404)

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

@api_view(['DELETE'])
def delete_categori(request, slug):
    try:
        book_categori = BookCategori.objects.get(slug=slug)
    except BookCategori.DoesNotExist:
        raise NotFound({'status':'Kategori bulunamadı'})
    book_categori.delete()

    return Response({'message': 'Kategori silindi'})

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

        serializer = KategoriSerializer(
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
    


@api_view(['POST'])
def kitap_ekle(request):
    """
    {
        "book_name":"str", 
        "barcode":"str", 
        "price":float, 
        "writer":"str", 
        "kategori":int
    }"""
    serializer = KitapInfoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": "Başarıyla yeni kitap eklendi",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        'status': 'hata meydana geldi',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def kitap_sil(requset,slug):
    try:
        book_categori=BookInfo.objects.get(book_slug=slug)
    except BookInfo.DoesNotExist:
        raise NotFound({'status':'Kitap silindi'}) 
    book_categori.delete()

    return Response({'message':'Kitap silinirken hata meydana geldi'})

@api_view(['GET'])
def get_info_book(request,slug):
    try:
        kategori = BookInfo.objects.get(book_slug=slug)
        serializer = KitapInfoSerializer(kategori)
        return Response({'status':'Başarılı bir şekilde eklendi',
                         'data':serializer.data})
    except BookInfo.DoesNotExist:
        return Response({"message":"Kategori Bulunamadı"},
                        status=404)