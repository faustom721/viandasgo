from django import forms

from ..models import VendorUser


class VendorUserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = VendorUser
        fields = ["first_name", "last_name", "email", "password"]
