# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import ZoneViewSet, AddressViewSet

# Router register
router = DefaultRouter()
router.register(r'zone', ZoneViewSet)
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('api/suite/location/', include(router.urls))
]

