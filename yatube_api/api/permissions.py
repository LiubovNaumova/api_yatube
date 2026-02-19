from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта: только автор может
    редактировать или удалять объект.
    Для остальных — только чтение.
    """
    def has_object_permission(self, request, view, obj):
        # Безопасные методы разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение/удаление только для автора
        return obj.author == request.user
