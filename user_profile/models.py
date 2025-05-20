from enum import IntEnum

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager

from working_space.models import WorkingSpace


class ShopUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self,
            email,
            password=None,
            username=None,
            **extra_fields
    ):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        shop_user = self.model(email=email, **extra_fields)
        if password:
            shop_user.set_password(password)
        shop_user.save(using=self._db)
        return shop_user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CivilLawSubjectChoice(IntEnum):
    company = 1
    person = 2

class MarketUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    password = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    is_staff = models.BooleanField(default=False)
    working_space = models.ForeignKey(
        WorkingSpace,
        on_delete=models.DO_NOTHING
    )
    # civil_law_subject = models.IntegerChoices(CivilLawSubjectChoice)
    date_joined = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = ShopUserManager()


class AddressKind(IntEnum):
    correspondence = 1
    residence_address = 2


class Address(models.Model):
    market_user = models.ForeignKey(
        MarketUser,
        on_delete=models.DO_NOTHING
    )
    kind = models.IntegerChoices(AddressKind)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)