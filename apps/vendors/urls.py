from django.urls import path

from . import views

app_name = "vendors"

urlpatterns = [
    path("register", views.user_register, name="register"),
]
