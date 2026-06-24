from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('list/',views.liste),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', views.register),
    path('deactive/<int:id>/', views.deactive_user),
    path('profile/',views.profile),
    path('profile/odunc/',views.kullanicinin_aldigi_kitaplar),
]


