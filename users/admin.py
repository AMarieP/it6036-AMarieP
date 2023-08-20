from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form_class = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'first_name', 'last_name', 'position', 'department_type'
        )
    
    fieldsets = (
        (None, {
            'fields': ('username', 'password',)
        }),
        ('Details', {
            'fields': ('first_name', 'last_name')
        }),
        ('Staff Information', {
            'fields': ('position', 'department_type', 'is_staff', 'is_superuser')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username','password1', 'password2')
        }),
        ('Details', {
            'fields': ('first_name', 'last_name')
        }),
        ('Staff Information', {
            'fields': ('position', 'department_type', 'is_staff', 'is_superuser')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)