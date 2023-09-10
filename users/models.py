from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra):
        user = self.model(
            username=username,
            **extra
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)

        if extra.get("is_staff") is not True:
            raise ValueError("You must set is_staff")
        if extra.get("is_superuser") is not True:
            raise ValueError("You must set is_superuser")

        return self.create_user(username=username, password=password, **extra)


class UserModel(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
