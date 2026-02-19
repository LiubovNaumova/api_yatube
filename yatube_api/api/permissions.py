from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает доступ на чтение всем,
    изменение - только автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить чтение всем
        if request.method in permissions.SAFE_METHODS:
            return True
            # Разрешить запись только автору объекта
            return obj.author == request.user
