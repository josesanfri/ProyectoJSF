# Third party imports
from ast import Name
from attr import validate
from rest_framework import serializers

from .models import Menu

# Create your serializers here

### SERIALIZERS FOR LIST VIEWS ###
class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'