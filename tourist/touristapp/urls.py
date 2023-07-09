from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChannelViewSet, LocationViewSet, CategoryViewSet, TagViewSet, FlagViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'flags', FlagViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
