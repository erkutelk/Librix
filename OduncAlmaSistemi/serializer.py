from rest_framework import serializers
from .models import OduncAlmaSistemi
from User.serializer import UserSerializer
from Book.serializer import KitapInfoSerializer_list


class OduncAlmaSistemiSeriazlier_list(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id')
    username = serializers.CharField(source='user.username')
    book_name = serializers.CharField(source='book.book_name')# bu şekilde yapıldığında serializer de yani modelde olan ,stedimiz değeri getirebiliriz
    class Meta:
        model = OduncAlmaSistemi
        fields = ["user_id","username", "book_name","teslim_edildi","verecegi_tarih"]

class OduncAlmaSistemiSeriazlier_details(serializers.ModelSerializer):
    user=UserSerializer()
    book=KitapInfoSerializer_list()
    class Meta:
        model = OduncAlmaSistemi
        fields = ["user", "book","teslim_edildi","verecegi_tarih"]


class OduncAlmaSistemiCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OduncAlmaSistemi
        fields = ["user", "book", "teslim_edildi", "verecegi_tarih"]