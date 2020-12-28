from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Store(AbstractUser):
    """
    Определим поля
    """
    inn = models.TextField(null=True, blank=True) # ИНН юридического лица магазина
    year_open = models.PositiveIntegerField(null=True, blank=True) # Год открытия магазина
