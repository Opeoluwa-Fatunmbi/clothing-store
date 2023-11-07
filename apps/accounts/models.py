from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        default=uuid.uuid4(), primary_key=True, unique=True, editable=False
    )
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    email = models.EmailField(_("Email_address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    terms_agreement = models.BooleanField(_("terms_agreement"), default=False)
    avatar = models.ImageField(upload_to="avatars/", null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
