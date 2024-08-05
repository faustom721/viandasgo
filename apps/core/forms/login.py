from django import forms

from ..widgets import TailwindEmailInput, TailwindPasswordInput


class LoginForm(forms.Form):
    email = forms.EmailField(widget=TailwindEmailInput(), label="Email")
    password = forms.CharField(widget=TailwindPasswordInput(), label="Contraseña")
