from django.contrib.auth.forms import UserCreationForm as ParentUserCreationForm
from django.contrib.auth.forms import UserChangeForm as ParentUserChangeForm

from .models import User


class UserCreationForm(ParentUserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(ParentUserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
