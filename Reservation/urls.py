from django.urls import path,include
from .views import resarvation_book_list,rezarvasyon_olustur,kitabi_teslim_et_admin

urlpatterns = [
    path('reservation/',resarvation_book_list),
    path('take-book/<int:id_>/',rezarvasyon_olustur),
    #Teslim almayı sadece admin yapabilsin
    path('return/user/<int:user_id>/book/<int:book_id>/', kitabi_teslim_et_admin)
]