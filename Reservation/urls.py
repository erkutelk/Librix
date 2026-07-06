from django.urls import path,include
from .views import resarvation_book_list

urlpatterns = [
    path('reservation/',resarvation_book_list),
]