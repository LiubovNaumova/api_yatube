from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("groups", GroupViewSet, basename="groups")


comment_list = CommentViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

comment_detail = CommentViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path(
        "api-token-auth/",
        obtain_auth_token,
        name="api-token-auth",
    ),
    path("", include(router.urls)),
    path(
        "posts/<int:post_id>/comments/",
        comment_list,
        name="comments-list",
    ),
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        comment_detail,
        name="comments-detail",
    ),
]
