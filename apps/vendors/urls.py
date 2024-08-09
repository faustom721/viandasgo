from django.urls import path

from . import views

app_name = "vendors"

urlpatterns = [
    path("user_register", views.user_register_view, name="user_register"),
    path("vendor_register", views.vendor_register_view, name="vendor_register"),
    path("dashboard", views.dashboard_view, name="dashboard"),
]
