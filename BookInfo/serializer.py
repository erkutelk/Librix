from rest_framework import serializers
from .models import BookCategori,BookInfo

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategori
        fields = '__all__'


class KitapInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInfo
        fields=['book_name','barcode','price','writer','kategori']