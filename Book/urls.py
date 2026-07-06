from django.urls import path,include
from Book.views_books import book_views,categori_views,writer_views

urlpatterns = [
    path('categori-get/<slug:slug>/',categori_views.get_categori,name='get_categori'),
    path('categori-all/',categori_views.all_categori,name='book_categori'),
    # path('categori-add/',categori_views.insert_categori,name='book_categori_add'),
    # path('categori-delete/<slug:slug>/',categori_views.delete_categori,name='book_delete'),
    # path('categori-update/<slug:slug>/',categori_views.patch_categori,name='categori_patch'),

    # path('book-add/',book_views.kitap_ekle,name='book_add'),
    # path('book-delete/<slug:slug>/',book_views.kitap_sil,name='book_delete'),
    path('book-get/<slug:slug>/',book_views.get_info_book,name='book_get'),
    # path('book-update/<slug:slug>/',book_views.get_guncelleme,name='guncelleme'),
    path('book-all/',book_views.get_all,name='book_all'),
    path('search/<name>/',book_views.get_search,name='search'),

    path('writer-all/',writer_views.get),
    path('writer/get/<int:id>',writer_views.get_first),
    # path('writer/add/',writer_views.add),
    # path('writer/delete/<int:id>/',writer_views.delete),
    # path('writer/update/<int:id>/',writer_views.update),
    path('writer/search/<name>/',writer_views.search)
]