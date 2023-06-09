# Third party imports
from ast import Name
from attr import validate
from rest_framework import serializers

# Local imports
from .models import Reserve
from applications.base.user.models import User
from applications.base.user.serializers import EmailUserSerializer
from applications.base.restaurant.models import Restaurant
from applications.base.restaurant.serializers import ReserveListRestaurantSerializer


# Create your serializers here
### SERIALIZERS FOR LIST VIEWS
class ReserveSerializer(serializers.ModelSerializer):
    restaurant = ReserveListRestaurantSerializer(many=False)
    customer = EmailUserSerializer(many=False, required=False)

    def to_representation(self, instance):
        ret = super().to_representation(instance)     
        try:             
            ret['status'] = [value for key, value in Reserve.RESERVE_STATUS_CHOICES if key == ret['status']][0]
            ret['type_reserve'] = [value for key, value in Reserve.RESERVE_TYPE_CHOICES if key == ret['type_reserve']][0]         
        except:
            pass
        return ret

    class Meta:
        model = Reserve
        fields = '__all__'

class CustomerReserveSerializer(serializers.ModelSerializer):
    restaurant = ReserveListRestaurantSerializer(many=False)
    customer = EmailUserSerializer(many=False, required=False)

    def to_representation(self, instance):         
        ret = super().to_representation(instance)   
        try:               
            ret['status'] = [value for key, value in Reserve.RESERVE_STATUS_CHOICES if key == ret['status']][0]       
        except:
            pass
        return ret

    class Meta:
        model = Reserve
        exclude = ['intern_note', 'type_reserve']

### SERIALIZERS FOR CREATE VIEWS
class CreateReserveSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(many=False, queryset = Restaurant.objects.all())
    customer = serializers.PrimaryKeyRelatedField(many=False, queryset = User.objects.filter(type_user=User.CUSTOMER), required=False)

    class Meta:
        model = Reserve
        fields = ['id', 'restaurant', 'customer', 'num_customers', 'confirmed_date', 'confirmed_time']

class StaffCreateReserveSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(many=False, queryset = Restaurant.objects.all())
    customer = serializers.PrimaryKeyRelatedField(many=False, queryset = User.objects.filter(type_user=User.CUSTOMER), required=False)

    class Meta:
        model = Reserve
        fields = ['id', 'restaurant', 'customer', 'num_customers', 'confirmed_date', 'confirmed_time']

    def to_representation(self, instance):         
        ret = super().to_representation(instance)   
        try:               
            ret['status'] = [value for key, value in Reserve.RESERVE_STATUS_CHOICES if key == ret['status']][0]
            ret['type_reserve'] = [value for key, value in Reserve.RESERVE_TYPE_CHOICES if key == ret['type_reserve']][0]       
        except:
            pass
        return ret

### SERIALIZERS FOR RETRIEVE UPDATE AND DESTROY VIEWS
class AbstractReserveModelSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    customer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Reserve
        fields = '__all__'

    def to_representation(self, instance):         
        ret = super().to_representation(instance)     
        try:             
            ret['status'] = [value for key, value in Reserve.RESERVE_STATUS_CHOICES if key == ret['status']][0]       
        except:
            pass
        return ret

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class StaffReserveModelSerializer(AbstractReserveModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'

class UserReserveModelSerializer(AbstractReserveModelSerializer):
    class Meta:
        model = Reserve
        exclude = ['created', 'created_by', 'updated', 'updated_by', 'intern_note', 'type_reserve']
        