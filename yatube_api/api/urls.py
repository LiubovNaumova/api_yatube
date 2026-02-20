from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'groups', views.GroupViewSet, basename='group')

urlpatterns = [
    # Все маршруты от router (посты, группы, детали постов)
    path('', include(router.urls)),

    # Маршруты для комментариев (вручную)
    # GET/POST /posts/{post_id}/comments/
    path('posts/<int:post_id>/comments/',
         views.CommentViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }), name='post-comments'),

    # GET/PUT/PATCH/DELETE /posts/{post_id}/comments/{pk}/
    path('posts/<int:post_id>/comments/<int:pk>/',
         views.CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }), name='post-comment-detail'),

    # Эндпоинт для получения токена
    path(
        'api-token-auth/',
        auth_views.obtain_auth_token,
        name='api_token_auth'),
]
