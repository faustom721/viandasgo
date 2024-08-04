from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .forms import VendorUserRegisterForm, VendorRegisterForm


def user_register(request):
    if request.method == "POST":
        form = VendorUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate the user
            authenticated_user = authenticate(
                username=user.username, password=form.cleaned_data.get("password1")
            )
            if authenticated_user is not None:
                # Log the user in
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse("vendors:vendor_register"))
            else:
                # Handle the case where authentication fails
                return render(
                    request,
                    "vendors/user_register.html",
                    {"form": form, "error": "Autenticación fallida."},
                )
        else:
            # Render the form with errors back to the template
            return render(request, "vendors/user_register.html", {"form": form})
    else:
        form = VendorUserRegisterForm()
    context = {"form": form}
    return render(request, "vendors/user_register.html", context)


def vendor_register(request):
    if request.method == "POST":
        form = VendorRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save()
            # Set the selected_vendor for the user
            request.user.selected_vendor = vendor
            request.user.save()
            return HttpResponseRedirect(reverse("vendors:home"))
        else:
            return render(request, "vendors/vendor_register.html", {"form": form})
    else:
        form = VendorRegisterForm()
    context = {"form": form}
    return render(request, "vendors/vendor_register.html", context)
