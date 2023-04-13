# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Menu
from .serializers import MenusSerializer

# Create your viewsets here
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenusSerializer