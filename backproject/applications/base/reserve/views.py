# Python imports
import json

#  Django imports
from django.db.models import Q
from django.http import QueryDict
from django.utils.translation import gettext as _

# Third party imports
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

# local imports
from .models import Reserve
from .serializers import (ReserveSerializer, CustomerReserveSerializer,
                        CreateReserveSerializer, StaffCreateReserveSerializer,
                        UserReserveModelSerializer, StaffReserveModelSerializer)
from .filters import ReserveFilter
from applications.base.user.models import User
from applications.utils.permissions import IsObjAuthorOrStaff, IsCustomerOrAdminUser


# Create your views here.
class ListReserveView(ListAPIView):
    permission_classes = [IsAuthenticated]
    filterset_class = ReserveFilter
                
    def get_queryset(self):
        if self.request.user.type_user == User.CUSTOMER:
            return Reserve.objects.filter(Q(customer=self.request.user)).distinct()

        return Reserve.objects.all()

    def get_serializer_class(self):
        if self.request.user.type_user == User.CUSTOMER:
            return CustomerReserveSerializer
        else:
            return ReserveSerializer

class CreateReserveView(CreateAPIView):
    permission_classes = [IsCustomerOrAdminUser]
    queryset = Reserve.objects.all()
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StaffCreateReserveSerializer
        return CreateReserveSerializer

    def perform_create(self, serializer):
        # First we check if the user has his/her customer profile. We not allow to complete the reserve without that condition
        if not self.request.user.is_staff and not self.request.user.customerprofile:
            raise serializers.ValidationError(_('Please, complete your profile before attempting to make a reservation'))

        if serializer.__class__ == StaffCreateReserveSerializer:
            serializer.save(customer=self.request.user, created_by=self.request.user, status=Reserve.CONFIRMED)
        else:
            serializer.save(customer=self.request.user, created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        """Overwritted method to include a success message, we call super method and later update de data dictionary
            with the message        
        Returns:
            Response: response with the models data and a success message 
        """
        response = super().create(request, *args, **kwargs)
        response.data.update(message=_('Reserve successfully created'))
        return response


class RestrieveUpdateDestroyReserveView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsObjAuthorOrStaff]
    queryset = Reserve.objects.all()
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.user.type_user == User.CUSTOMER:
            return UserReserveModelSerializer
        return StaffReserveModelSerializer

    def get_serializer(self, *args, **kwargs):
        """We need to parse self.request.data in case it is a dict or a querydict

        Returns:
            ModelSerializer: serializer for Customer Profile
        """
        instance = self.get_object()
        serializer = self.get_serializer_class()

        if self.request.method == 'PUT':
        
            if isinstance(self.request.data, QueryDict):
                data_dict = self.request.data.dict()

                return serializer(instance=instance, data=data_dict)
         
            return serializer(instance=instance, data=self.request.data)
           
        return serializer(instance=instance)

    def perform_update(self, serializer):        
        serializer.save(updated_by=self.request.user)
                
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data.update(message=_('Reserve successfully edited'))
        return response
