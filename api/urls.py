from django.conf.urls import include, url
from rest_framework import routers
from api.views import UserViewSet, GarageViewSet, AssetViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'garages', GarageViewSet, base_name='garages')
router.register(r'assets', AssetViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]