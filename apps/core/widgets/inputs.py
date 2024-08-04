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


class TailwindTextarea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            }
        )
        super().__init__(*args, **kwargs)


class TailwindSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-select mt-1 block w-full py-2 px-3 rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            }
        )
        super().__init__(*args, **kwargs)


class TailwindCheckboxInput(forms.CheckboxInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-checkbox h-4 w-4 text-indigo-600 transition duration-150 ease-in-out"
            }
        )
        super().__init__(*args, **kwargs)


class TailwindFileInput(forms.FileInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {}).update(
            {
                "class": "form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            }
        )
        super().__init__(*args, **kwargs)
