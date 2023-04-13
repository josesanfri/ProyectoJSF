# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Address, Zone
from .serializers import AddressSerializer, ZoneSerializer

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    