from . import views
from django.urls import path

urlpatterns = [
    path('odunc-all/',views.odunc_alma_get),
    path('odunc-get/<int:id>/',views.odunc_first_id),
]