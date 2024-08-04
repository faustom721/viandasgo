from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms.user_register import VendorUserRegisterForm


def user_register(request):
    if request.method == "POST":
        form = VendorUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse("vendoruser-registration-confirmation"))
        else:
            # Render the form with errors back to the template
            return render(request, "vendors/user_register.html", {"form": form})
    else:
        form = VendorUserRegisterForm()
    context = {"form": form}
    return render(request, "vendors/user_register.html", context)
