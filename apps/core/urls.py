from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("login", views.login, name="login"),
    path("error/", views.error, name="error"),
    path("contact/", views.contact, name="contact"),
    path(
        "contact-confirmation/", views.contact_confirmation, name="contact_confirmation"
    ),
]
