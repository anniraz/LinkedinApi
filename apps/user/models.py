from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from utils.PhoneNumberValidation import phone_validator


class User(AbstractUser):
    
    username = None
    email=models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number=models.CharField(max_length=13,validators=[phone_validator])
    image = models.ImageField(upload_to='avatars/',blank=True, null=True)
    is_premium=models.BooleanField(default=False)

    REQUIRED_FIELDS=[]
    USERNAME_FIELD = "email"

    
    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ("id",)