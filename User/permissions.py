from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied("Bu işlemi yapmak için giriş yapmalısınız.")

        if not request.user.is_staff:
            raise PermissionDenied("Bu işlemi yapmak için admin yetkiniz yok.")
        return (
            request.user.is_authenticated and
            request.user.role == "admin"
        )