from django.db import models

from phonenumber_field.formfields import PhoneNumberField

from apps.core.models import CustomUser


class VendorUser(CustomUser):
    """Vendor users are the staff of a vendor, could be the owner, a cashier, etc."""

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"


class Vendor(models.Model):
    """Vendors are food stores, businesses"""

    logo = models.ImageField("Logo", upload_to="vendors/logos")
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción")
    phone = PhoneNumberField(region="UY")
    email = models.EmailField("Email")
    address = models.CharField("Dirección", max_length=255, null=True, blank=True)
    staff = models.ManyToManyField(VendorUser, verbose_name="Personal")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    max_orders = models.PositiveIntegerField(
        "Máximo de pedidos", default=10, null=True, blank=True
    )

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"


class Menu(models.Model):
    """Menus are the food options that a vendor offers"""

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Local")
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción")
    price = models.DecimalField("Precio", max_digits=6, decimal_places=2)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    photo = models.ImageField("Foto", upload_to="menus/photos")

    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menús"


class WorkingHours(models.Model):
    opening_time = models.TimeField("Hora de apertura")
    closing_time = models.TimeField("Hora de cierre")
    max_orders = models.PositiveIntegerField("Máximo de pedidos", default=10)
    order_limit_time = models.TimeField("Hora límite para pedidos")
    delivery_start_time = models.TimeField("Hora de inicio de entregas")

    class Meta:
        abstract = True


class WeekWorkingHours(WorkingHours):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Local")

    class Meta:
        verbose_name = "Horario de trabajo semanal"
        verbose_name_plural = "Horarios de trabajo semanales"


class WeekendWorkingHours(WorkingHours):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Local")
    saturday = models.BooleanField("Sábado", default=True)
    sunday = models.BooleanField("Domingo", default=False)

    class Meta:
        verbose_name = "Horario de trabajo fin de semana"
        verbose_name_plural = "Horarios de trabajo fin de semana"


class ExceptionalClosingDay(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Local")
    date = models.DateField("Fecha")
    reason = models.CharField("Motivo", max_length=255)

    class Meta:
        verbose_name = "Día de cierre excepcional"
        verbose_name_plural = "Días de cierre excepcionales"
