# Third party imports
from ast import Name
from attr import validate
from rest_framework import serializers

from .models import Menu
from applications.base.plate.models import Plate
from applications.base.plate.serializers import PlatesSerializer

# Create your serializers here

### SERIALIZERS FOR LIST VIEWS ###
class MenusSerializer(serializers.ModelSerializer):
    starter = PlatesSerializer(many=True, required=False)
    main = PlatesSerializer(many=True, required=False)
    dessert = PlatesSerializer(many=True, required=False)

    class Meta:
        model = Menu
        fields = '__all__'