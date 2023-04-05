# Third party imports
from rest_framework import serializers

# Local imports
from .models import Restaurant, MediaRestaurant, User
from applications.base.location.models import Address
from applications.base.user.models import User
from applications.base.location.serializers import SimpleAddressSerializer, AddressSerializer, ExtendedAddressSerializer

# Python imports
from datetime import datetime

# Create your serializers here
## RESTAURANT SERIALIZERS ##
class RestaurantSerializer(serializers.ModelSerializer):
    """Serielizer used in Viewset
    """
    class Meta:
        model = Restaurant
        fields = '__all__'

    def to_representation(self, instance):         
        ret = super().to_representation(instance)    
        return ret

class ListRestaurantSerializer(serializers.ModelSerializer):
    """
    Restaurant serializer used in List View 
    """
    address = SimpleAddressSerializer()
    media_restaurant =  serializers.SerializerMethodField()
    
    class Meta:
        model = Restaurant
        fields = ['id', 'slug_restaurant', 'media_restaurant', 'address']

    def get_media_restaurant(self,instance):
        media_restaurant_instances = instance.media_restaurant.filter(is_cover = True)
        return ImageUrlSerializer(media_restaurant_instances, many=True).data
    
    def to_representation(self, instance):         
        ret = super().to_representation(instance)
        return ret

class RetrieveRestaurantSerializer(serializers.ModelSerializer):
    """
    Restaurant serializer used for a single restaurant retrieve view in the website.
    """
    address = ExtendedAddressSerializer(many=False)
    media_restaurant =  serializers.SerializerMethodField()
    
    class Meta:
        model = Restaurant
        exclude = ['is_multireserve', 'is_managed', 'created_by', 'updated_by']

    def to_representation(self, instance):         
        ret = super().to_representation(instance)
        return ret

    def get_media_restaurant(self,instance):
        media_restaurant_instances = instance.media_restaurant.all()
        return ImageUrlSerializer(media_restaurant_instances, many=True).data

class RestaurantModelSerializer(serializers.ModelSerializer):
    """Restaurant serializer used for create & update the model"""
    address = AddressSerializer()
    
    class Meta:
        model = Restaurant
        exclude = ['id']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        restaurant = Restaurant(address=address, **validated_data)
        restaurant.save()
        
        return restaurant

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        Address.objects.filter(id=instance.address.id).update(**address_data)
        
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
  

## MEDIA RESTAURANT SERIALIZERS ##
class MediaRestaurantSerializer(serializers.ModelSerializer):
    """
    Restaurant serializer used for a media fields from restaurant
    """
    restaurant = serializers.PrimaryKeyRelatedField(many = False, queryset = Restaurant.objects.all(), required=False)
    
    class Meta:
        model = MediaRestaurant
        fields = '__all__'
        extra_kwargs = {'type_image' : {'required': False}} 

    def to_representation(self, instance):     
        ret = super().to_representation(instance)
        try:                  
            ret['type_image'] = [value for key, value in MediaRestaurant.IMAGE_TYPE_CHOICES if key == ret['type_image']][0]        
            return ret
        except:
            return ret     

class ImageUrlSerializer(serializers.ModelSerializer):
    """
    MediaRestaurant nested serializer to show cover image on ListRestaurantSerializer
    """
    class Meta:
        model = MediaRestaurant
        fields = ["image"]