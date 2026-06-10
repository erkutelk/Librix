from django.urls import path
from . import views

urlpatterns = [
    path('book-add/',views.kitap_ekle,name='book_add'),
    path('book-delete/<slug:slug>/',views.kitap_sil,name='book_delete'),
    path('book-get/<slug:slug>/',views.get_info_book,name='book_get'),
    path('book-update/<slug:slug>/',views.get_guncelleme,name='guncelleme'),
    path('book-all/',views.get_all,name='book_all'),
    path('search/<name>',views.get_search,name='search'),

]
