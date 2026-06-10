from django.db import models
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
# Create your models here.

class BookCategori(models.Model):
    book_categori = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    categori_isActive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.book_categori))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_categori
