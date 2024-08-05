from django import forms

from ..widgets import TailwindEmailInput, TailwindPasswordInput


class LoginForm(forms.Form):
    email = forms.EmailField(widget=TailwindEmailInput())
    password = forms.CharField(widget=TailwindPasswordInput())
