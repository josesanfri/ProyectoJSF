# Third party imports
from rest_framework import serializers

# Local imports
from .models import Department, SubDepartment
from applications.base.restaurant.models import Restaurant

# Create your serializers here
class DepartmentSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(many=False, queryset = Restaurant.objects.all())
    
    class Meta:
        model = Department
        fields = '__all__'

class SubDepartmentSerializer(serializers.ModelSerializer):
    principal_department = serializers.PrimaryKeyRelatedField(many=False, queryset = Department.objects.all())
    secondary_department = serializers.PrimaryKeyRelatedField(many=False, queryset = Department.objects.all())

    class Meta:
        model = SubDepartment
        fields = '__all__'
