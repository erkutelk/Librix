from rest_framework import serializers
from .models import BookCategori,BookInfo,Writer
        
class KitapInfoSerializer_create(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ["book_name","barcode","price","writer_book","kategori","stock"]



class KitapInfoSerializer_list(serializers.ModelSerializer):
    kategori = serializers.CharField(source="kategori.book_categori")

    class Meta:
        model = BookInfo
        fields = ["book_name","barcode","kategori"]

from rest_framework import serializers
from .models import Writer
        
class WriterBookSerializer_list(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["name","surname","isActive","dateAdd"]
        read_only_fields = ["dateAdd"]


class WriterUpdateSerializer_create(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["name", "surname", "isActive","dateAdd"]


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
        