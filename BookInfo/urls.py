from django.urls import path
from . import views

urlpatterns = [
    path('categori-all/',views.all_categori,name='book_categori'),
    path('categori-add/',views.insert_categori,name='book_categori_add')
]
