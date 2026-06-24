from django.shortcuts import render
from rest_framework.decorators import api_view
from Book.serializer import KitapInfoSerializer_create,KitapInfoSerializer_list,BookListSerializer_list,BookDetailSerializer
from rest_framework.response import Response
from Book.models import BookCategori,BookInfo
from rest_framework import status
from django.db.models import Q
# Create your views here.
from User.permissions import IsAdmin
from rest_framework.decorators import api_view, permission_classes



@permission_classes([IsAdmin])
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
    serializer = KitapInfoSerializer_create(data=request.data)

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
@permission_classes([IsAdmin])
def kitap_sil(request, slug):
    try:
        obj = BookInfo.objects.get(book_slug=slug)
        obj.delete()
        return Response(
            {'message': 'Kitap silindi'},
            status=status.HTTP_200_OK
        )
    except BookInfo.DoesNotExist as e:
        return Response(
            {'error': f'Kitap bulunamadı{e}'},
            status=status.HTTP_404_NOT_FOUND
        )



@api_view(['GET'])
def get_info_book(request,slug):
    try:
        kategori = BookInfo.objects.get(book_slug=slug)
        serializer = BookDetailSerializer(kategori)
        return Response({'data':serializer.data})
    except BookInfo.DoesNotExist:
        return Response({"message":"Kategori Bulunamadı"},
                        status=404)
    

@api_view(['PATCH'])
@permission_classes([IsAdmin])
def get_guncelleme(request,slug):
    try:
        instance=BookInfo.objects.get(book_slug=slug)
        serializer=KitapInfoSerializer_create(instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Güncelleme işlemi tamamlandı',
                            'data':serializer.data},
                            status=200)
    
    except BookCategori.DoesNotExist:
        return Response({'error':'Silinmes sırasında bir hata meydana geldi'},status=404)


# @permission_classes([IsAdmin])
@api_view(['GET'])
def get_all(request):
    menu=BookInfo.objects.all()
    try:
        serializer = BookListSerializer_list(menu, many=True)
        return Response({'status':'Tüm kitap bilgileri','data':serializer.data})
    except:
        return Response({'status':'Kitap bilgileri getirilirke hata meydana geldi'},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_search(request, name):
    kitaplar = BookInfo.objects.filter(
        Q(book_name__icontains=name) |
        Q(book_slug__icontains=name)
    )

    if kitaplar.exists():
        serializer = KitapInfoSerializer_list(kitaplar, many=True)
        return Response({'status':'başarıyla bulundu',
                        'data':serializer.data},
                        status=status.HTTP_302_FOUND)
    
    else:
        return Response({'erorr':'Kitap bulunamadı'},status=status.HTTP_404_NOT_FOUND)