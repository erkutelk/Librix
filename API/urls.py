from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('',include('OduncAlmaSistemi.urls')),
    path('',include('Book.urls')),
    path('',include('Reservation.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)