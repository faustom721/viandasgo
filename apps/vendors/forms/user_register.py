from django import forms
from django.contrib.auth.hashers import make_password

from ..models import VendorUser
from core.widgets import (
    TailwindTextInput,
    TailwindEmailInput,
    TailwindPasswordInput,
    TailwindPhoneNumberInput,
)


class VendorUserRegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(
        label="Repetí la contraseña",
        widget=TailwindPasswordInput(),
        required=True,
    )

    class Meta:
        model = VendorUser
        fields = ["first_name", "last_name", "email", "phone", "password"]
        widgets = {
            "first_name": TailwindTextInput(),
            "last_name": TailwindTextInput(),
            "email": TailwindEmailInput(),
            "phone": TailwindPhoneNumberInput(),
            "password": TailwindPasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        self.fields["phone"].required = True
        self.fields["password"].required = True
        self.fields["password_repeat"].required = True

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        email = cleaned_data.get("email")

        if password and password_repeat and password != password_repeat:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        if VendorUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con este email.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
