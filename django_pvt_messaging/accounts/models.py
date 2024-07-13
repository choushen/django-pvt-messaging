from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .account_manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None # Set value to None to use email as the username
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # Define unique identifier as email
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email