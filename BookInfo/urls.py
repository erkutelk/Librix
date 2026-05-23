from django.urls import path
from . import views

urlpatterns = [
    path('categori-all/',views.all_categori,name='book_categori'),
    path('categori-add/',views.insert_categori,name='book_categori_add'),
    path('categori-delete/<slug:slug>/',views.delete_categori,name='book_delete'),
    path('categori-update/<slug:slug>/',views.patch_categori,name='categori_patch')
]
