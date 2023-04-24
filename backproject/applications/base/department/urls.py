# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import DepartmentViewSet, SubDepartmenteViewSet

# Router register
router = DefaultRouter()
router.register(r'dep', DepartmentViewSet, basename='department-viewset')
router.register(r'sub-department', SubDepartmenteViewSet)

urlpatterns = [
    path('api/suite/department/', include(router.urls), name='department'),
]
