from django.db import models
from User.models import UserInfo
from Book.models import BookInfo,BookCategori
# Create your models here.

class OduncAlmaSistemi(models.Model):
    STATUS_CHOICES = [
        ("pending", "Bekliyor"),
        ("borrowed", "Kullanıcıda"),
        ("returned", "İade Edildi"),
        ("cancelled", "İptal Edildi"),
    ]
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    aldigiTarih=models.DateField(auto_now_add=True)
    verecegi_tarih=models.DateField()
    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default="pending"
        )
    def __str__(self):
        return f'{self.user} | {self.book}'
