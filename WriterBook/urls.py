from . import views
from django.urls import path

urlpatterns = [
    path('writer/',views.get),
    path('writer/get/<int:id>',views.get_first),
    path('writer/add/',views.add),
    path('writer/delete/<int:id>/',views.delete),
    path('writer/update/<int:id>/',views.update),
    # path('writer/pathc',views.patch),
]