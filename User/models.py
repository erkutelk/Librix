from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class UserInfo(AbstractUser):
    phone = PhoneNumberField(unique=True)
    relative_id_number = models.CharField(max_length=11, unique=True)
    ROLE_CHOICES =[
        ("admin","Admin"),
        ("user","user"),
    ]
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default="user")

    def __str__(self):
        return self.username