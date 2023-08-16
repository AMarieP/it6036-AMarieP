from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

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
        )
        def save(self, commit=True):
            instance = super(CustomUserCreationForm, self).save(commit=False)
            instance.username = "%s.%s" %(self.cleaned_data['first_name'], self.cleaned_data['last_name'])
            if commit:
                instance.save()
            return instance


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "password",
            "email", 
            "position",
        )
        def save(self, commit=True):
            instance = super(CustomUserCreationForm, self).save(commit=False)
            instance.username = "%s.%s" %(self.cleaned_data['first_name'], self.cleaned_data['last_name'])
            if commit:
                instance.save()
            return instance

