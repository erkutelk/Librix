from . import views
from django.urls import path

urlpatterns = [
    # path('admin/odunc-all/',views.odunc_alma_get_all),
    path('admin/<int:user_id>/books/',views.kullanicilarin_odunc_aldigi_kitaplar),
    path('admin/odunc-get/<int:id>/',views.odunc_first_id),
    path('admin/odunc-update/<int:id>/',views.odunc_alma_guncelleme),
    path('admin/odunc-create/',views.odunc_create),
    path('admin/odunc-list-user/',views.tum_kullanicilar)
]