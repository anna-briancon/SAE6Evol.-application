from django.urls import include, path
from rest_framework import routers

from .views import ArtistViewSet

router = routers.DefaultRouter()
router.register(r'artist', ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
