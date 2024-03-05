from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email='admin@gmail.com'):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True, null=False)
    photo = models.ImageField(upload_to="images/", null=True)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
