from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('book-info',include('BookInfo.urls')),
    path('odunc/',include('OduncAlmaSistemi.urls')),
    path('book-categori/',include('BookCategori.urls')),
]
