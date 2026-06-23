from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied("Giriş yapmalısın.")

        if getattr(request.user, "role", None) != "admin":
            raise PermissionDenied("Admin yetkin yok.")

        return True