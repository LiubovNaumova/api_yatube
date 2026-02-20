from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта:
    - безопасные методы (GET, HEAD, OPTIONS) разрешены (но доступ к API всё равно
      ограничен IsAuthenticated глобально/на вьюсете)
    - изменять/удалять может только автор.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, "author", None) == request.user
