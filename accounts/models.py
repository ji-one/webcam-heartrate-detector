from django.db import models

# Create your models here.
from django.contrib.auth.models import UserManager, AbstractUser, BaseUserManager


class User(AbstractUser):
    objects = UserManager()