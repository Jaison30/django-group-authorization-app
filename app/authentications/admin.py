from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "role")

admin.site.register(CustomUser, CustomUserAdmin)