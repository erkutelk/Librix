from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = PhoneNumberField(unique=True) 
    date_added = models.DateTimeField(auto_now_add=True)
    relative_id_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
