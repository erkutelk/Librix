from rest_framework import serializers
from .models import BookCategori,BookInfo

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategori
        fields = '__all__'

    def validate_book_categori(self,value):
        value=value.strip()

        if not value:
            raise serializers.ValidationError("Bu alan boş bırakılmamalı.")
        
        if BookCategori.objects.filter(book_categori=value).exists():
            raise serializers.ValidationError('Aynı kategori adında bir kategori mevcut')

        return value
class KitapInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInfo
        fields=['book_name','barcode','price','writer','kategori']