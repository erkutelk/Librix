from django.db import models

class BookCategori(models.Model):
    book_categori=models.CharField(max_length=100)
    categori_isActive=models.BooleanField(default=True)
    def __str__(self):
        return 'Kategori Name: ',self.book_kategori


class BookInfo(models.Model):
    book_name=models.CharField(max_length=100)
    barcode=models.CharField(max_length=12,unique=True)
    price=models.FloatField()
    writer=models.CharField(max_length=70)
    kategori = models.ForeignKey(BookCategori, on_delete=models.CASCADE)

# Create your models here.
