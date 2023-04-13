# Third party imports
from rest_framework import serializers

# Local imports
from .models import Menu

# Create your serializers here
class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        