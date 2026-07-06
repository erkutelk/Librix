from django.db import models
from User.models import UserInfo
from Book.models import BookInfo

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("waiting", "Bekliyor"),
        ("ready", "Hazır"),
        ("cancelled", "İptal"),
        ("completed", "Tamamlandı"),
    ]
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="waiting")
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_date"]