from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'first_name', 'last_name', 'position'
        )
    
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Position', {
            'fields': ('first_name', 'last_name')
        }),
        ('Position', {
            'fields': ('position',)
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Position', {
            'fields': ('first_name', 'last_name')
        }),
        ('Position', {
            'fields': ('position',)
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)