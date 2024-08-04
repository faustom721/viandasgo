from django import forms

from ..models import Vendor
from core.widgets import (
    TailwindEmailInput,
    TailwindTextInput,
    TailwindTextarea,
    TailwindPhoneNumberInput,
    TailwindFileInput,
)


class VendorRegisterForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["name", "description", "email", "phone", "address", "logo"]
        widgets = {
            "name": TailwindTextInput(),
            "description": TailwindTextarea(),
            "email": TailwindEmailInput(),
            "phone": TailwindPhoneNumberInput(),
            "address": TailwindTextInput(),
            "logo": TailwindFileInput(),
        }
