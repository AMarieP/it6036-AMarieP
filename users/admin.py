from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.contrib.admin.widgets import FilteredSelectMultiple    


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

class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    users = forms.ModelMultipleChoiceField(
         queryset=CustomUser.objects.all(), 
         required=False,
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance

# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ['permissions']

admin.site.register(Group, GroupAdmin)