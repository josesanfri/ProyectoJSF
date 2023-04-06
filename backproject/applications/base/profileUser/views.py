# Python imports
import json

# Django imports
from django.http import QueryDict
from django.utils.translation import gettext as _

# Third party imports
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


# Local imports
from .serializers import ViewCustomerProfileSerializer, CreateCustomerProfileSerializer
from applications.base.profileUser.models import CustomerProfile
from applications.utils.permissions import IsCustomerOrAdminUser, IsObjAuthorOrStaff

# Create your views here.
class CreateCustomerProfileView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsCustomerOrAdminUser]
    queryset = CustomerProfile.objects.all()


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        """Overwritted method to include a success message, we call super method and later update\ de data dictionary
            with the message        
        Returns:
            Response: response with the models data and a success message 
        """
        response = super().create(request, *args, **kwargs)
        response.data.update(message=_('Profile successfully created'))
        return response

    def get_serializer(self, *args, **kwargs):
        """We need to parse self.request.data in case it is a dict or a querydict

        Returns:
            ModelSerializer: serializer for Customer Profile
        """
        if isinstance(self.request.data, QueryDict):
            data_dict = self.request.data.dict()
                    
            return CreateCustomerProfileSerializer(data=data_dict)
        
        else:   
            return CreateCustomerProfileSerializer(data=self.request.data)
    

class RetrieveUpdateDestroyCustomerProfileView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsCustomerOrAdminUser, IsObjAuthorOrStaff]
    queryset = CustomerProfile.objects.all()
    lookup_field = 'user'

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data.update(message=_('Profile successfully edited'))
        return response

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        data = {}
        data['message']=_('Profile successfully deleted')
        return Response(data=data, status=status.HTTP_200_OK)

    def get_serializer(self, *args, **kwargs):
        """We need to parse self.request.data in case it is a dict or a querydict

        Returns:
            ModelSerializer: serializer for Customer Profile
        """
        instance = self.get_object()
        
        if self.request.method == 'PUT':
            if isinstance(self.request.data, QueryDict):
                data_dict = self.request.data.dict()
                
                return ViewCustomerProfileSerializer(instance=instance, data=data_dict)
            
            else:   
                return ViewCustomerProfileSerializer(instance=instance, data=self.request.data)
            
        return ViewCustomerProfileSerializer(instance=instance)
    

              

