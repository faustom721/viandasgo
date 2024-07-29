from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms.register import VendorUserRegisterForm


def vendor_user_register_view(request):
    if request.method == "POST":
        form = VendorUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect("/vendor-registration-confirmation/")
        else:
            return HttpResponseRedirect("/error/")
    else:
        form = VendorUserRegisterForm()
    context = {"form": form}
    return render(request, "vendors/vendor_user_register.html", context)
