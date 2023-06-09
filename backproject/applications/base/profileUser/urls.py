# Django imports
from django.urls import path, include, re_path

# Third party imports 
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import (CustomerProfileViewSet, StaffProfileViewSet)
from .views import CreateCustomerProfileView, RetrieveUpdateDestroyCustomerProfileView

# Router registe
router = DefaultRouter()
router.register(r'customer', CustomerProfileViewSet)
router.register(r'staff', StaffProfileViewSet)

urlpatterns = [
    # Viewset urls
    path('api/suite/profile/', include(router.urls), name='profile'),

    # Views urls
    path('api/profile/customer/', CreateCustomerProfileView.as_view(), name='customer-profile-create'),
    path('api/profile/customer/<int:user>/', RetrieveUpdateDestroyCustomerProfileView.as_view(), name='customer-profile-detail'),
]
