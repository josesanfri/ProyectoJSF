# Third party imports
from rest_framework import viewsets

# Local imports
from .models import (CustomerProfile, StaffProfile)
from .serializers import (CustomerProfileSerializer, StaffProfileSerializer)

# Create your viewsets here
class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

class StaffProfileViewSet(viewsets.ModelViewSet):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer