from rest_framework import serializers
from .models import BookCategori,BookInfo,Writer, BookImage

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ["resim"]



class KitapInfoSerializer_create(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = BookInfo
        fields = [
            "book_name",
            "barcode",
            "price",
            "writer_book",
            "kategori",
            "stock",
            "images"
        ]

    def create(self, validated_data):
        images = validated_data.pop("images", [])

        book = BookInfo.objects.create(**validated_data)

        for image in images:
            BookImage.objects.create(
                book=book,
                resim=image
            )

        return book



class KitapInfoSerializer_list(serializers.ModelSerializer):
    kategori = serializers.CharField(source="kategori.book_categori")
    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = BookInfo
        fields = ["book_name", "barcode", "kategori", "images"]

from rest_framework import serializers
from .models import Writer
        
class WriterBookSerializer_list(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["id","name","surname","isActive","dateAdd"]
        read_only_fields = ["dateAdd"]

class WriterUpdateSerializer_update(serializers.ModelSerializer):
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("En az 2 karakter")
        return value

    def validate_surname(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(f"En az 2 karakter")
        return value

    class Meta:
        model = Writer
        fields = ["id","name", "surname", "isActive", "dateAdd"]


class WriterUpdateSerializer_create(serializers.ModelSerializer):
    def validate(self, attrs):# iki adet değeri kontrol ettiğim için alan belirtmiyoruz.
        import re

        name = attrs.get("name", "")
        surname = attrs.get("surname", "")

        if Writer.objects.filter(name=name, surname=surname).exists():
            raise serializers.ValidationError("Bu kayıt zaten var")

        if not name.strip() or not surname.strip():
            raise serializers.ValidationError("Bu alan boş bırakılmamalı")

        if len(name.strip()) <= 1 or len(surname.strip()) <= 1:
            raise serializers.ValidationError("Karakter sayısı en az 2 olmalı")

        if not re.search(r"[a-zA-Z0-9çğıöşüÇĞİÖŞÜ]", name) or not re.search(r"[a-zA-Z0-9çğıöşüÇĞİÖŞÜ]", surname):
            raise serializers.ValidationError("Emoji kabul edilmez")

        return attrs

    class Meta:
        model = Writer
        fields = ["id","name", "surname", "isActive", "dateAdd"]


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
        