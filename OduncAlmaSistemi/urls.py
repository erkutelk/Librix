from . import views
from django.urls import path

urlpatterns = [
    path('odunc-all/',views.odunc_alma_get_all),
    path('users/<int:user_id>/books/',views.kullanicilarin_odunc_aldigi_kitaplar),
    path('admins/odunc-get/<int:id>/',views.odunc_first_id),
    path('admins/odunc-update/<int:id>/',views.odunc_alma_guncelleme),
    path('admins/odunc-create/',views.odunc_create),
    path('admins/odunc-list-user/',views.tum_kullanicilar)
]