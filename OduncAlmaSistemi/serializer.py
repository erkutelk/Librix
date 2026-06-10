from rest_framework import serializers
from .models import OduncAlmaSistemi
from User.serializer import UserSerializer
from BookInfo.serializer import KitapInfoSerializer


class OduncAlmaSistemiSeriazlier(serializers.ModelSerializer):
    user=UserSerializer()
    book=KitapInfoSerializer()
    class Meta:
        model = OduncAlmaSistemi
        fields = ["id", "user", "book", "aldigiTarih", "verecegi_tarih", "teslim_edildi"]