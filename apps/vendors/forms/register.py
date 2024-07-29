from django import forms

from ..models import Vendor


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"
        exclude = ["staff"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }
