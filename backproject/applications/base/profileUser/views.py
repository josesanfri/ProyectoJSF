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
        response = super().create(request, *args, **kwargs)
        response.data.update(message=_('Profile successfully created'))
        return response

    def get_serializer(self, *args, **kwargs):
        if isinstance(self.request.data, QueryDict):
            data_dict = self.request.data.dict()

            key_list = ['address']

            for key in key_list:
                if key in self.request.data:
                    data_dict[key] = json.loads(self.request.data.get(key))    
                    
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
        instance = self.get_object()
        
        if self.request.method == 'PUT':
            if isinstance(self.request.data, QueryDict):
                data_dict = self.request.data.dict()

                key_list = ['address']

                for key in key_list:
                    if key in self.request.data:
                        data_dict[key] = json.loads(self.request.data.get(key))    
                
                return ViewCustomerProfileSerializer(instance=instance, data=data_dict)
            
            else:   
                return ViewCustomerProfileSerializer(instance=instance, data=self.request.data)
            
        return ViewCustomerProfileSerializer(instance=instance)
    