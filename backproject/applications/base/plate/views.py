# Python imports
import json

# Django imports
from django.db.models import Q
from django.http import QueryDict
from django.utils.translation import gettext as _

# Third party imports
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

# Local imports
from .models import Plate
from .serializers import PlatesSerializer
from applications.utils.permissions import IsObjAuthorOrStaff, IsAdminUser

# Create your views here.
class ListPlateView(ListAPIView):
    def get_queryset(self):
        return Plate.objects.all()

    def get_serializer_class(self):
        return PlatesSerializer
    
class CreatePlateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Plate.objects.all()
    
    def get_serializer_class(self):
        return PlatesSerializer

    def perform_create(self, serializer):
        serializer.save(staff=self.request.user, created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data.update(message=_('Plate successfully created'))
        return response
    
class RestrieveUpdateDestroyPlateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsObjAuthorOrStaff]
    queryset = Plate.objects.all()
    lookup_field = 'id'
    
    def get_serializer_class(self):
        return PlatesSerializer

    def get_serializer(self, *args, **kwargs):
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
        response.data.update(message=_('Plate successfully edited'))
        return response
    