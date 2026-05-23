from django.db import models
from django.utils.text import slugify




from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class BookCategori(models.Model):
    book_categori = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    categori_isActive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            text = unidecode(self.book_categori)   # Türkçe → ASCII çevir
            self.slug = slugify(text)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_categori


class BookInfo(models.Model):
    book_name=models.CharField(max_length=100)
    barcode=models.CharField(max_length=12,unique=True)
    price=models.FloatField()
    writer=models.CharField(max_length=70)
    kategori = models.ForeignKey(BookCategori, on_delete=models.CASCADE)

# Create your models here.
