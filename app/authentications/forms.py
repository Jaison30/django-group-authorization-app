from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "role",
            "country",
            "nationality",
            "mobile",
            "password1",
            "password2",
        )
