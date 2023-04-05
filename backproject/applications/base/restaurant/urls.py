# Django imports
from django.urls import path, include

# Third party imports 
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import (RestaurantViewSet, MediaRestaurantViewSet)
from .views import ( CreateRestaurantView, RetrieveUpdateDestroyRestaurantView , ListRestaurantView , 
                    CreateRestaurantImageView , RetrieveUpdateDeleteImageView )

# Router register
router = DefaultRouter()
router.register(r'rent', RestaurantViewSet)
router.register(r'media', MediaRestaurantViewSet)

urlpatterns = [
    # Viewset urls
    path('api/suite/restaurant/', include(router.urls), name='restaurant'),

    # Services urls
    path('api/restaurant/', ListRestaurantView.as_view(), name='restaurant-list'),
    path('api/restaurant/register/', CreateRestaurantView.as_view(), name='restaurant-create'),
    path('api/restaurant/<int:id>', RetrieveUpdateDestroyRestaurantView.as_view(), name='restaurant-detail-short'),
    path('api/restaurant/<slug:slug_restaurant>', RetrieveUpdateDestroyRestaurantView.as_view(), name='restaurant-detail-complete'),
    path('api/restaurant/<int:restaurant>/media/', CreateRestaurantImageView.as_view(), name='image-create'),
    path('api/restaurant/<int:restaurant>/media/<int:id>', RetrieveUpdateDeleteImageView.as_view(), name='image-detail'),
]

