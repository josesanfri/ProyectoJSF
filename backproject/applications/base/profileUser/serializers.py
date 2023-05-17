# Django imports
from collections import OrderedDict
import re
from django.utils.translation import gettext as _
from pkg_resources import require

# Third party imports
from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

# Local imports
from .models import StaffProfile, CustomerProfile
from applications.base.user.models import User
from applications.base.location.models import Address
from applications.base.location.serializers import AddressSerializer


# Create your serializers here
## CUSTOMER PROFILE SERIALIZERS
class CustomerProfileSerializer(ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = CustomerProfile
        fields = '__all__'

class ConfirmedReserveCustomerProfileSerializer(ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['first_name', 'last_name', 'age', 'prefix_phone', 'phone']

class CreateCustomerProfileSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(many = False, queryset = User.objects.filter(type_user = User.CUSTOMER))
    address = AddressSerializer()

    class Meta:
        model = CustomerProfile
        fields = '__all__'
    
    def to_representation(self, instance):         
        ret = super().to_representation(instance) 
        try:                 
            ret['gender'] = [value for key, value in CustomerProfile.GENDER_CHOICES if key == ret['gender']][0]  
        except:
            pass      
        return ret
        
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        
        try:           
            customer_profile = CustomerProfile.objects.create(address=address, **validated_data)
        except Exception as e:
            print(e)
            address.delete()
            raise serializers.ValidationError((e))

        return customer_profile

## STAFF PROFILE SERIALIZERS
class StaffProfileSerializer(ModelSerializer):    
    user = PrimaryKeyRelatedField(many = False, queryset = User.objects.filter(type_user = User.STAFF))
    address = AddressSerializer()
    
    class Meta:
        model = StaffProfile
        fields = '__all__'

# Views Serializers
class ViewCustomerProfileSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(many = False, read_only=True)
    address = AddressSerializer()

    class Meta:
        model = CustomerProfile
        fields = '__all__'
    
    def to_representation(self, instance):         
        ret = super().to_representation(instance) 
        try:                 
            ret['gender'] = [value for key, value in CustomerProfile.GENDER_CHOICES if key == ret['gender']][0]  
        except:
            pass      
        return ret
        
    def update(self, instance, validated_data):
        if 'address' in validated_data:
            address_data = validated_data.pop('address')
            Address.objects.filter(id=instance.address.id).update(**address_data)
        
        if 'user' in validated_data:
            user = validated_data.pop('user')
        
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
