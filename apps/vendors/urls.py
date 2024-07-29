from django.urls import path

from . import views

app_name = "vendors"

urlpatterns = [
    path("register", views.vendor_user_register_view, name="register"),
]
