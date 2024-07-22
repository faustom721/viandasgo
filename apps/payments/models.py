from django.db import models


# class Payment(models.Model):
#     order = models.OneToOneField(
#         "Order", on_delete=models.CASCADE, verbose_name="Orden", related_name="payment"
#     )
#     created_at = models.DateTimeField("Fecha de creación")
#     last_modified = models.DateTimeField("Última modificación")
#     amount = models.DecimalField("Monto", max_digits=6, decimal_places=0)
#     payment_method = models.CharField("Método de pago", max_length=100)
#     payment_type = models.CharField("Tipo de pago", max_length=100)
#     payment_status = models.CharField("Estado de pago", max_length=100)
#     payment_id = models.CharField("ID de pago", max_length=100)
#     payment_provider = models.CharField("Proveedor de pago", max_length=100)

#     class Meta:
#         verbose_name = _("Pago")
#         verbose_name_plural = _("Pagos")

#     def save(self, *args, **kwargs):
#         new_payment_status = kwargs.get("payment_status", self.payment_status)

#         if new_payment_status == "approved":
#             send_confirmation_email(self.order)
#         elif new_payment_status == "cancelled" or new_payment_status == "rejected":
#             print("Bad payment")
#         else:
#             print("Pending")
#         super().save(*args, **kwargs)
