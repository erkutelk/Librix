from django.db import models
from User.models import UserInfo
from Book.models import BookInfo,BookCategori
# Create your models here.

class OduncAlmaSistemi(models.Model):
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    kategori=models.ForeignKey(BookCategori,on_delete=models.CASCADE)

    aldigiTarih=models.DateField(auto_now_add=True)
    verecegi_tarih=models.DateField()
    teslim_edildi=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} | {self.book}'
