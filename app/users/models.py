
from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .validators import check_phone
class User(AbstractUser):
    username = models.CharField('username', max_length=256, unique=True, null=True)
    phone = models.CharField('phone number', max_length=11, null=True, validators=[check_phone])
    name = models.CharField('full name', default="کاربر مهمان", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    