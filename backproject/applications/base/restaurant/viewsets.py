# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Restaurant, MediaRestaurant
from .serializers import (RestaurantSerializer,  MediaRestaurantSerializer)

# Create your viewsets here
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MediaRestaurantViewSet(viewsets.ModelViewSet):
    queryset = MediaRestaurant.objects.all()
    serializer_class = MediaRestaurantSerializer
    