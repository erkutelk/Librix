from rest_framework import serializers
from .models import BookCategori,BookInfo
        
class KitapInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"
