import os
import mercadopago

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import LoginForm, ContactForm


MP_ACCESS_TOKEN = os.environ.get("MP_ACCESS_TOKEN")
SERVER_NAME = os.environ.get("SERVER_NAME")
sdk = mercadopago.SDK(MP_ACCESS_TOKEN)


def landing_page(request):
    return render(request, "core/landing_page.html", {})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get("next", reverse("vendors:dashboard"))
                return HttpResponseRedirect(next_url)
            else:
                form.add_error(None, "Usuario o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, "core/login.html", {"form": form})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            return HttpResponseRedirect(
                f"/contact-confirmation/?contact_msg={contact_msg.id}"
            )
        else:
            return HttpResponseRedirect("/error/")
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "core/contact.html", context)


def contact_confirmation(request):
    contact_msg = request.GET.get("contacordet_msg")
    contact_msg = ContactMsg.objects.filter(id=contact_msg).first()
    if not contact_msg:
        return HttpResponseRedirect("/error/")
    context = {"contact_msg": contact_msg}
    return render(request, "core/contact_confirmation.html", context)


def error(request):
    return render(request, "core/error.html")
