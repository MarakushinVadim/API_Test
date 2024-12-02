from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    phone = models.IntegerField(max_length=10, unique=True, verbose_name='Номер телефона')
    referral_invite = models.CharField(max_length=6, null=True, blank=True, verbose_name='Личный инвайт-код')
    invited_from_user = models.CharField(max_length=6, null=True, blank=True, verbose_name='Приглашен по коду')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
