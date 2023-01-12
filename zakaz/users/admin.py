from django.contrib import admin
from .models import User


# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(User, UserModelAdmin)
