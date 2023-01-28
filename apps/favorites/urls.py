from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.favorites.views import FavoriteApiViewSet,FavoriteCategoryApiViewSet
from .views import *

router = DefaultRouter()


router.register(prefix='my',viewset=FavoriteApiViewSet),
router.register(prefix='category',viewset=FavoriteCategoryApiViewSet)
urlpatterns = router.urls
