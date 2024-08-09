from apps.core.models import CustomUser
from .models import VendorUser


def get_vendor_user(user: CustomUser) -> VendorUser:
    """Given a CustomUser, return the VendorUser that corresponds to it."""

    return VendorUser.objects.filter(username=f"v->{user.email}").first()
