from django.urls import path

from . import views

app_name = "vendors"

urlpatterns = [
    path("user_register", views.user_register, name="user_register"),
    path("vendor_register", views.vendor_register, name="vendor_register"),
    path("login", views.vendor_register, name="login"),
]
