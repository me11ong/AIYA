from django.contrib.auth.models import AbstractUser
from django.db import models
class users(AbstractUser):
    city = models.CharField(max_length=100,null=True)
    gu = models.CharField(max_length=100, null=True)
    dong = models.CharField(max_length=100, null=True)

