from django.shortcuts import render
from rest_framework.decorators import api_view
from Reservation.serializer import Reservation_List
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
# Create your views here.
from User.permissions import IsAdmin
from rest_framework.decorators import api_view, permission_classes
from Reservation.models import Reservation

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from .serializer import Reservation_List

@api_view(["GET"])
def resarvation_book_list(request):
    reservations = Reservation.objects.all()
    serializer = Reservation_List(reservations, many=True)
    return Response({"data": serializer.data})