import json
import requests
import os
import mercadopago


from bs4 import BeautifulSoup
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, Http404, HttpResponseRedirect

from .forms.contact_form import ContactForm


MP_ACCESS_TOKEN = os.environ.get("MP_ACCESS_TOKEN")
SERVER_NAME = os.environ.get("SERVER_NAME")
sdk = mercadopago.SDK(MP_ACCESS_TOKEN)


def landing_page(request):
    return render(request, "core/landing_page.html", {})


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
