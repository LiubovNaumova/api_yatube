from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("groups", GroupViewSet, basename="groups")

urlpatterns = [
    # Токен
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),

    # /posts/ и /groups/ (и detail)
    path("", include(router.urls)),

    # Вложенные комментарии:
    # /posts/{post_id}/comments/
    path(
        "posts/<int:post_id>/comments/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="comments-list",
    ),
    # /posts/{post_id}/comments/{comment_id}/
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        CommentViewSet.as_view(
            {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
        name="comments-detail",
    ),
]
