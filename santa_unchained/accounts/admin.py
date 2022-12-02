from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group

from .forms import GroupAdminForm
from .models import CustomUser

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    form = GroupAdminForm
