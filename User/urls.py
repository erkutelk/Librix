from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('list/',views.liste,name='kullanicilar'),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    # path('register/', views.register),
    path('deactive/<int:id>/', views.deactive_user),
    path('create/', views.create_user_by_admin),

]


# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MTY2MzU0OCwiaWF0IjoxNzgxNTc3MTQ4LCJqdGkiOiI4YWJmNTM1NzJjZDA0MTZlODQ5MWQ4MTBjNWE4MGU2YSIsInVzZXJfaWQiOiI1In0.RHlQJo4i35llUs4P7oNoGFRi6soQNcwRy0Wbhv_P_U8",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxNTc3NDQ4LCJpYXQiOjE3ODE1NzcxNDgsImp0aSI6IjI3ZDY0YmExOTg4MTQ3YTRiNTE2ZGNmYzFiYmNmZGExIiwidXNlcl9pZCI6IjUifQ.cqqGMu6ONAouGobKk_jpES_5oe0QO0baehorNxvZWpI"
# }