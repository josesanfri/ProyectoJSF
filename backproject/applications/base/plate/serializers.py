# Third party imports
from ast import Name
from attr import validate
from rest_framework import serializers

# Local imports
from .models import Plate

# Create your serializers here
class PlatesSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)     
        try:             
            ret['type_plate'] = [value for key, value in Plate.PLATES_TYPE_CHOICES if key == ret['type_plate']][0]         
        except:
            pass
        return ret
    
    class Meta:
        model = Plate
        fields = '__all__'
        