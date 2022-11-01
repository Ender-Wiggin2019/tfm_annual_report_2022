from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.forms import JSONField


class UserAccountManager(BaseUserManager):
    def create_user(self, name, password=None):
        user = self.model(name=name)
        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=250, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name


class UserData(models.Model):
    user_id = models.AutoField("id", primary_key=True)
    user_name = models.CharField("username", max_length=30)
    user_total = models.CharField("userdata", max_length=10000, default="");


class UserCheck(models.Model):
    class UserType(models.TextChoices):
        ADMIN = 'admin'
        USER = 'user'
        CLIENT = 'client'

    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.USER)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)


