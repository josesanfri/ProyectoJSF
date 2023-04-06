# Third party imports
from rest_framework import serializers

# Local imports
from .models import Zone, Address

# Create your serializers here
class AddressSerializer(serializers.ModelSerializer):
    zone =  serializers.PrimaryKeyRelatedField(many=False, allow_null = True, queryset = Zone.objects.all(), required=False)

    class Meta:
        model = Address
        fields = '__all__'

class SimpleAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['street', 'number', 'city', 'latitude', 'longitude']

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

class ExtendedAddressSerializer(serializers.ModelSerializer):
    zone =  serializers.PrimaryKeyRelatedField(many=False, allow_null = True, queryset = Zone.objects.all(), required=False)
    class Meta:
        model = Address
        exclude = ['created', 'updated', 'created_by', 'updated_by']