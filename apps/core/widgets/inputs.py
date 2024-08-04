from django import forms
from phonenumber_field.widgets import RegionalPhoneNumberWidget


class TailwindTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            }
        )
        super().__init__(*args, **kwargs)


class TailwindEmailInput(forms.EmailInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            }
        )
        super().__init__(*args, **kwargs)


class TailwindPasswordInput(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            }
        )
        super().__init__(*args, **kwargs)


class TailwindPhoneNumberInput(RegionalPhoneNumberWidget):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            }
        )
        super().__init__(*args, **kwargs)
