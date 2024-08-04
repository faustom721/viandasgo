from django import forms

from ..models import VendorUser
from core.widgets import (
    TailwindTextInput,
    TailwindEmailInput,
    TailwindPasswordInput,
    TailwindPhoneNumberInput,
)


class VendorUserRegisterForm(forms.ModelForm):
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
