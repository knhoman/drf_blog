from gjango.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

url_patterns = [
	path("", include(router.urls))
]
