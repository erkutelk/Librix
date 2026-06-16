from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('odunc/',include('OduncAlmaSistemi.urls')),
    path('',include('Book.urls')),

]