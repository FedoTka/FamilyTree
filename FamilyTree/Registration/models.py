from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .services import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30, null=True)
    second_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=255, unique=True)

    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = ["email"]


    def __str__(self):
        return self.nickname

