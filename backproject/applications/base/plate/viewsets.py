# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Plate
from .serializers import PlatesSerializer

# Create your viewsets here
class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlatesSerializer