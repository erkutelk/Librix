from rest_framework import serializers
from .models import Writer
        
class WriterBookSerializer_list(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ["name","surname","isActive","dateAdd"]
        read_only_fields = ["dateAdd"]


