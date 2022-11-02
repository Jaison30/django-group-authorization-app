from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


ROLES = ((1, "student"), (2, "staff"), (3, "admin"), (4, "editor"))


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLES, default=3)
    country = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=100, null=True)
    mobile = PhoneNumberField(null=False, blank=False, unique=True)
    USERNAME_FIELD = "username"

    
    def __str__(self):
        return "{}".format(self.username)
