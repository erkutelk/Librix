from rest_framework import serializers
from .models import BookCategori,BookInfo

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategori
        fields = '__all__'

    def validate_book_categori(self,value):
        if not value.strip():
            raise serializers.ValidationError("Bu alan boş bırakılmamalı.")
        
        if BookCategori.objects.filter(book_categori=value):
            raise serializers.ValidationError('Aynı kategori adında bir kategori mevcut')
        
        if BookCategori.objects.filter(book_categori=value).exists():
            raise serializers.ValidationError('Böyle bir kategori me')

        return value
class KitapInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInfo
        fields=['book_name','barcode','price','writer','kategori']