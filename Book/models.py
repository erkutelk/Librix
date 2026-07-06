from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

class Writer(models.Model):
    name=models.CharField(max_length=20,blank=True)
    surname=models.CharField(max_length=20)
    isActive=models.BooleanField(default=True)
    dateAdd=models.DateTimeField(auto_now_add=True)


class BookCategori(models.Model):
    book_categori = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    categori_isActive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.book_categori))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_categori
    

class BookCategori_details(models.Model):
    book_categori = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    categori_isActive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.book_categori))
        super().save(*args, **kwargs)


class BookLanguage(models.Model):
    language=models.CharField(max_length=25)
    lang=models.CharField(max_length=5,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BookInfo(models.Model):
    book_name=models.CharField(max_length=100)
    book_slug=models.SlugField(unique=True,blank=True)
    barcode=models.CharField(max_length=12,unique=True)
    price=models.FloatField(null=True,blank=True)
    writer_book=models.ForeignKey(Writer,on_delete=models.CASCADE)
    kategori = models.ForeignKey(BookCategori, on_delete=models.CASCADE)
    stock=models.IntegerField(default=1,blank=True)
    isActive=models.BooleanField(default=True)
    description=models.TextField(blank=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language=models.ForeignKey(BookLanguage,on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.book_slug = slugify(unidecode(self.book_name))
        super().save(*args, **kwargs)

class BookImage(models.Model):
    book = models.ForeignKey(
        BookInfo,
        on_delete=models.CASCADE,
        related_name="images"
    )

    resim = models.ImageField(upload_to='Book_image/')
    isActive = models.BooleanField(default=True)


