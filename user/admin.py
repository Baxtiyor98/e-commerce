from django.contrib import admin
from user.models import CustomUser


@admin.register(CustomUser)
class Custom(admin.ModelAdmin):
    list_display = ['username', 'id']
