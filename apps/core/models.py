from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone = PhoneNumberField("Teléfono", region="UY")


class ContactMsg(models.Model):
    name = models.CharField("Nombre", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Mensaje")
    created_at = models.DateTimeField("Fecha", auto_now_add=True)

    class Meta:
        verbose_name = _("Mensaje de contacto")
        verbose_name_plural = _("Mensajes de contacto")

    def __str__(self):
        return f"{self.name} - {self.email}"
