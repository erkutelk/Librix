from django.db import models
from django.utils.text import slugify
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from BookCategori.models import BookCategori


class BookInfo(models.Model):
    book_name=models.CharField(max_length=100)
    book_slug=models.SlugField(unique=True,blank=True)
    barcode=models.CharField(max_length=12,unique=True)
    price=models.FloatField(null=True,blank=True)
    writer=models.CharField(max_length=70)
    kategori = models.ForeignKey(BookCategori, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.book_slug = slugify(unidecode(self.book_name))
        super().save(*args, **kwargs)
# Create your models here.
