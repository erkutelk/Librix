from rest_framework import serializers
from .models import BookCategori,BookInfo
        
class KitapInfoSerializer_create(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ["book_name","barcode","price","writer","kategori","stock"]



class KitapInfoSerializer_list(serializers.ModelSerializer):
    kategori = serializers.CharField(source="kategori.book_categori")

    class Meta:
        model = BookInfo
        fields = ["book_name","barcode","kategori"]

