# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Reserve
from .serializers import ReserveSerializer

# Create your viewsets here
class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer