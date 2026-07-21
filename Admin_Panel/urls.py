from . import views
from django.urls import path

from Book.views_books import writer_views
from Book.views_books import book_views
from Book.views_books import categori_views
from OduncAlmaSistemi import views as odunc_al
from User import views

urlpatterns = [
    path('odunc-all/',odunc_al.odunc_alma_get_all),
    path('<int:user_id>/books/',odunc_al.kullanicilarin_odunc_aldigi_kitaplar),
    path('odunc-get/<int:id>/',odunc_al.odunc_first_id),
    path('odunc-update/<int:id>/',odunc_al.odunc_alma_guncelleme),
    path('odunc-create/',odunc_al.odunc_create),
    path('odunc-list-user/',odunc_al.tum_kullanicilar),

    #Yazar işlemleri
    path('writer/add/',writer_views.add),
    path('writer/delete/<int:id>/',writer_views.delete),
    path('writer/update/<int:id>/',writer_views.update),
    path('writer-all/',writer_views.get),

    #Kitap işlemleri
    path('book-add/',book_views.kitap_ekle,name='book_add'),
    path('book-delete/<slug:slug>/',book_views.kitap_sil,name='book_delete'),
    path('book-update/<slug:slug>/',book_views.get_guncelleme,name='guncelleme'),
    path('book-all/',book_views.get_all,name='book_all'),

    #Kullanıcı işlemelri
    path('user-list/',views.liste),
    path('user-deactive/<int:id>/', views.deactive_user),

    #Kategori işlemleri
    path('categori-add/',categori_views.insert_categori,name='book_categori_add'),
    path('categori-delete/<slug:slug>/',categori_views.delete_categori,name='book_delete'),
    path('categori-update/<slug:slug>/',categori_views.patch_categori,name='categori_patch'),
    path('categori-get/<slug:slug>/',categori_views.get_categori,name='get_categori'),

    # Kullanıcı kendi bilgileriyle girdiğinde görecekleri
    # Tüm kitaplar
    # kitap arama 
    # Profil bilgileri
    # Aldığı kitaplar
    # Ödünç vereceği kitaplar
    # Rezarvayon ettiği kitaplar
    # Tüm kitap bilgileri(Adminden farklı olucak faklrı bir serializer yazılacak)
]