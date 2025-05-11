from django.contrib import admin
from .models import User,UserLoginInfo
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserLoginInfo)
class UserLoginInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip','created')
    def user_name(self, obj):
        return obj.user.username

    user_name.short_description = 'User'
