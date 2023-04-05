# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

# Local imports
from applications.base.user import views
from .viewsets import UserViewSet

# Creation of the router and register the viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user-viewset')

# The API URLs are now determined automatically by the router

urlpatterns = [
    # Viewsets
    path('api/suite/user/', include(router.urls), name='user-viewset'),
    
    # Views
    path('api/sign-up/', views.user_register, name='user-sign-up'), 
    path('api/login/', views.user_login, name='login'),
    path('api/logout/', views.user_logout, name='logout'),

]
