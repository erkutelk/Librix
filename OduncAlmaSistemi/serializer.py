from rest_framework import serializers
from .models import OduncAlmaSistemi
from User.serializer import UserSerializer
from Book.serializer import KitapInfoSerializer_list


class OduncAlmaSistemiSeriazlier_list(serializers.ModelSerializer):
    user=UserSerializer()
    book=KitapInfoSerializer_list()
    class Meta:
        model = OduncAlmaSistemi
        fields = ["user", "book","teslim_edildi","verecegi_tarih"]

class OduncAlmaSistemiCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OduncAlmaSistemi
        fields = ["user", "book", "teslim_edildi", "verecegi_tarih"]