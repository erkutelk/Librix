from rest_framework import serializers
from .models import BookCategori

class KategoriSerializer_list(serializers.ModelSerializer):
    
    class Meta:
        model = BookCategori
        fields = ['book_categori']

    def get_kategori(self, obj):
        return obj.kategori.book_categori
    
    def validate_book_categori(self,value):
        import re
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Bu alan boş bırakılmamalı.")
        
        if BookCategori.objects.filter(book_categori=value).exists():
            raise serializers.ValidationError('Aynı kategori adında bir kategori mevcut')

        if not re.search(r'[a-zA-Z0-9çğıöşüÇĞİÖŞÜ]', value):
            raise serializers.ValidationError("Kategori emojilerden oluşamaz") 
        
        return value
        

class KategoriSerializer_create(serializers.ModelSerializer):
    class Meta:
        model = BookCategori
        fields = ['book_categori','categori_isActive']

    def get_kategori(self, obj):
        return obj.kategori.book_categori
    
    def validate_book_categori(self,value):
        import re
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Bu alan boş bırakılmamalı.")
        
        if BookCategori.objects.filter(book_categori=value).exists():
            raise serializers.ValidationError('Aynı kategori adında bir kategori mevcut')

        if not re.search(r'[a-zA-Z0-9çğıöşüÇĞİÖŞÜ]', value):
            raise serializers.ValidationError("Kategori emojilerden oluşamaz") 
        
        return value
        