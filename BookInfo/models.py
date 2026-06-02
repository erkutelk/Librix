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
        self.slug = slugify(unidecode(self.book_categori))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_categori


class BookInfo(models.Model):
    book_name=models.CharField(max_length=100)
    book_slug=models.SlugField(unique=True,blank=True)
    barcode=models.CharField(max_length=12,unique=True)
    price=models.FloatField()
    writer=models.CharField(max_length=70)
    kategori = models.ForeignKey(BookCategori, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.book_slug = slugify(unidecode(self.book_name))
        super().save(*args, **kwargs)
# Create your models here.
