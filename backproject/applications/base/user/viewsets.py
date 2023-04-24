# Third party imports
from rest_framework import viewsets, filters

# Local imports
from .models import User
from .serializers import UserSerializer, CustomerSerializer, StaffSerializer

# Create your viewsets here
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(type_user=User.CUSTOMER)
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'customerprofile__first_name__unaccent', 'customerprofile__last_name__unaccent', 'customerprofile__phone']

class StaffViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(type_user=User.STAFF)
    serializer_class = StaffSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'staffprofile__first_name__unaccent', 'staffprofile__last_name__unaccent', 'staffprofile__phone']
    