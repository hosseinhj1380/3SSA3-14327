
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
    

class UserLoginInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    ip = models.CharField(max_length=25, verbose_name=_('IP Address'))
    device = models.CharField(max_length=25, verbose_name=_('Device'))
    browser_family = models.CharField(max_length=25, verbose_name=_('Browser Family'))
    browser_version = models.CharField(max_length=25, verbose_name=_('Browser Version'))
    os = models.CharField(max_length=25, verbose_name=_('OS'))
    is_mobile = models.BooleanField(default=False, verbose_name=_('Phone'))
    is_tablet = models.BooleanField(default=False, verbose_name=_('Tablet'))
    is_pc = models.BooleanField(default=False, verbose_name=_('PC'))
    is_bot = models.BooleanField(default=False, verbose_name=_('Bot'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'))
    
    

    def __str__(self):
        return self.ip

    class Meta:
        db_table = "user_login_info"
        ordering = ['-created']
        verbose_name = _('User Login Info')
        verbose_name_plural = _('Users Login Info')