# Django imports
from django.urls import path, include

# Third party imports 
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import ReserveViewSet
from .views import ListReserveView, CreateReserveView, RestrieveUpdateDestroyReserveView

# Router register
router = DefaultRouter()
router.register(r'', ReserveViewSet)

urlpatterns = [
    # Suite URLS
    path('api/suite/reserve/', include(router.urls), name='reserve'),

    # View URLs
    path('api/reserve/', ListReserveView.as_view(), name='reserve-list'),
    path('api/reserve/create/', CreateReserveView.as_view(), name='reserve-model'),
    path('api/reserve/<int:id>', RestrieveUpdateDestroyReserveView.as_view(), name='reserve-detail' )
]
