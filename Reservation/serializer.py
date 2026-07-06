from .models import Reservation
from rest_framework import serializers
from Book.serializer import BookListSerializer_list

class Reservation_List(serializers.Serializer):
    user = serializers.StringRelatedField()
    book = BookListSerializer_list()

    class Meta:
        model = Reservation
        fields = [
            "id",
            "user",
            "book",
            "status",
            "created_date"
        ]