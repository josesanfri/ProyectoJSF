#  Third party imports
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

# Local imports 
from .models import User
from applications.base.profileUser.serializers import (CustomerProfileSerializer, StaffProfileSerializer,)

# Create your serializers here
## GENERIC USER SERIALIZERS
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff']

class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class EmailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
        extra_kwargs = {'email': {'read_only': True}}

## CUSTOMER SERIALIZERS
class CustomerSerializer(ModelSerializer):
    customerprofile = CustomerProfileSerializer(many=False)
    
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff']

## STAFF USER SERIALIZER
class StaffSerializer(ModelSerializer):
    staffprofile = StaffProfileSerializer(many=False)

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff']


## SPECIFIC SERIALIZERS FOR LOGIN & SIGN-UP
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'type_user']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            type_user = validated_data['type_user'],
        )           
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)