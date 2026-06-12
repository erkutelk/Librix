from django.db import models


class Writer(models.Model):
    name=models.CharField(max_length=20,blank=True)
    surname=models.CharField(max_length=20)
    isActive=models.BooleanField(default=True)
    dateAdd=models.DateTimeField(auto_now_add=True)
# Create your models here.
