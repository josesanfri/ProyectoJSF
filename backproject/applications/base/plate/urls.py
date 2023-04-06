# Django imports
from django.urls import path, include

# Third party imports 
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import PlateViewSet
from .views import ListPlateView, CreatePlateView, RestrieveUpdateDestroyPlateView

# Router register
router = DefaultRouter()
router.register(r'', PlateViewSet)

urlpatterns = [
    # Suite URLS
    path('api/suite/plate/', include(router.urls), name='plate'),

    # View URLs
    path('api/plate/', ListPlateView.as_view(), name='plate-list'),
    path('api/plate/create/', CreatePlateView.as_view(), name='plate-model'),
    path('api/plate/<int:id>', RestrieveUpdateDestroyPlateView.as_view(), name='plate-detail' )
]