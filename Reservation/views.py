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
from Book.models import BookInfo
from OduncAlmaSistemi.models import OduncAlmaSistemi
@api_view(["GET"])
def resarvation_book_list(request):
    user = request.user
    reservations = Reservation.objects.filter(user_id=user.id)
    serializer = Reservation_List(reservations, many=True)
    return Response({"data": serializer.data})


@api_view(["POST"])
def rezarvasyon_olustur(request,id_):
    user=request.user
    book=BookInfo.objects.get(id=id_)
    daha_once_aldi_mi=Reservation.objects.filter(user_id=user,book_id=book,status="waiting").exists()

    if daha_once_aldi_mi:
        return Response({"Message":"Bu kitabı daha önceden aldın, iade etmeden tekrar alamazsın"})


    if book.stock>0:
        OduncAlmaSistemi.objects.create(verecegi_tarih="2026-10-05",book_id=book.id,user_id=user.id)
        book.stock-=1
        book.save()
        return Response({'Message':'Kitap ödünç verildi'})

    else:
        Reservation.objects.create(user=user,book=book,status="waiting")
        return Response({"Message":"Stok yok, rezarvasyon alındı"})


@api_view(['POST'])
def kitabi_teslim_et_admin(request, user_id, book_id):

    borrow = OduncAlmaSistemi.objects.filter(
        user_id=user_id,
        book_id=book_id,
        teslim_edildi=False
    )

    if not borrow.exists():
        return Response({"message": "Zaten teslim edilmiş"}, status=400)

    borrow.update(teslim_edildi=True)

    book = BookInfo.objects.get(id=book_id)
    book.stock += 1
    book.save()

    return Response({"message": "Kitap teslim edildi"})