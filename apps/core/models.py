import math

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

from PIL import Image
from apps.core.utils import send_confirmation_email
from django_ckeditor_5.fields import CKEditor5Field


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
