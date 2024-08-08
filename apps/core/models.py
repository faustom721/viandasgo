from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone = PhoneNumberField("Teléfono", region="UY")
    vendor_user = models.OneToOneField(
        "vendors.VendorUser",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user",
        primary_key=True,
    )
    customer_user = models.OneToOneField(
        "customers.CustomerUser",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user",
        primary_key=True,
    )

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


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
