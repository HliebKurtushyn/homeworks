from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, default="")
    age = models.PositiveIntegerField(null=True, blank=True, default=None)
    phone = models.CharField(max_length=15, unique=True, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
