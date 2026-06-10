from django.urls import path,include
from BookCategori import views

urlpatterns = [
    path('categori-get/<slug:slug>/',views.get_categori,name='get_categori'),
    path('categori-all/',views.all_categori,name='book_categori'),
    path('categori-add/',views.insert_categori,name='book_categori_add'),
    path('categori-delete/<slug:slug>/',views.delete_categori,name='book_delete'),
    path('categori-update/<slug:slug>/',views.patch_categori,name='categori_patch'),
]