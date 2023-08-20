from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email", 
            "position",
            "department_type",
            "is_staff",
            "is_superuser"
        )



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "password",
            "email", 
            "position",
            "department_type",
        )


