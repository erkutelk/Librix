from rest_framework import serializers
from .models import UserInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'phone',
            'relative_id_number',
            'role',
            'is_active'
        ]