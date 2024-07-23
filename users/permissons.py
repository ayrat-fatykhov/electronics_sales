from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """
    Проверяет пользователя на активность.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True
