# Django imports
from django.urls import path, include

# Third party imports 
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import MenuViewSet
from .views import ListMenuView, CreateMenuView, RestrieveUpdateDestroyMenuView

# Router register
router = DefaultRouter()
router.register(r'', MenuViewSet)

urlpatterns = [
    # Suite URLS
    path('api/suite/menu/', include(router.urls), name='menu'),

    # View URLs
    path('api/menu/', ListMenuView.as_view(), name='menu-list'),
    path('api/menu/create/', CreateMenuView.as_view(), name='menu-model'),
    path('api/menu/<int:id>', RestrieveUpdateDestroyMenuView.as_view(), name='menu-detail' )
]