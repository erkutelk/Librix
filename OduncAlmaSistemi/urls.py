from . import views
from django.urls import path

urlpatterns = [
    path('odunc-all/',views.odunc_alma_get),
    path('admins/odunc-get/<int:id>/',views.odunc_first_id),
    path('admins/odunc-update/<int:id>/',views.odunc_alma_guncelleme),
    path('admins/odunc-create/',views.odunc_create)
]