from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from core.comment.viewsets import CommentViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.post.viewsets import PostViewSet

router = DefaultRouter()

"""##############  User  ##############"""
router.register(r'user', UserViewSet, basename='user')

"""##############   Register   ##############"""
router.register(r'auth/register', RegisterViewSet, basename="auth-register")

"""##############   Login   ##############"""
router.register(r'auth/login', LoginViewSet, basename="auth-login")
router.register(r'auth/refresh', RefreshViewSet, basename="auth-refresh")

"""##############   Posts   ##############"""
router.register(r'post', PostViewSet, basename="post")

posts_router = NestedDefaultRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment')

urlpatterns = [
    *router.urls,
    *posts_router.urls,
]
