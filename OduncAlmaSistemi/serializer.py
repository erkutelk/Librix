from rest_framework import serializers
from .models import OduncAlmaSistemi
from User.serializer import UserSerializer
from Book.serializer import KitapInfoSerializer_list,BookImageSerializer


class OduncAlmaSistemiSeriazlier_list(serializers.ModelSerializer):
    # user_id = serializers.CharField(source='user.id')
    # username = serializers.CharField(source='user.username')
    images = BookImageSerializer(source='book.images', many=True)
    book_name = serializers.CharField(source='book.book_name')# bu şekilde yapıldığında serializer de yani modelde olan ,stedimiz değeri getirebiliriz
    class Meta:
        model = OduncAlmaSistemi
        fields = ["book_name","status","aldigiTarih","verecegi_tarih",'images']

class OduncAlmaSistemiSeriazlier_details(serializers.ModelSerializer):
    user=UserSerializer()
    book=KitapInfoSerializer_list()
    class Meta:
        model = OduncAlmaSistemi
        fields = ["user", "book","status","verecegi_tarih"]


class OduncAlmaSistemiCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OduncAlmaSistemi
        fields = ["user", "book", "status", "verecegi_tarih"]