from django import forms

from ..models import Vendor
from core.widgets import (
    TailwindEmailInput,
    TailwindTextInput,
    TailwindTextarea,
    TailwindPhoneNumberInput,
    TailwindFileInput,
)
from ..utils import get_vendor_user


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["description"].required = False
        self.fields["email"].required = False
        self.fields["phone"].required = True
        self.fields["address"].required = True
        self.fields["logo"].required = True

    def save(self, commit=True):
        vendor = super().save(commit=False)
        if commit:
            vendor.owner = get_vendor_user(self.request.user)
            vendor.save()
        return vendor
