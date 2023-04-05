# Python imports
import json
import os

# Django imports
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

# Third party imports
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveUpdateDestroyAPIView , RetrieveAPIView
from rest_framework.response import Response

# Local imports
from .serializers import ( RestaurantModelSerializer, RetrieveRestaurantSerializer , ListRestaurantSerializer , ExtendedRestaurantSerializer ,
                            MediaRestaurantSerializer )
from .models import Restaurant , MediaRestaurant
from .filters import RestaurantFilter
from applications.utils.permissions import IsAdminUser, IsObjAuthorOrStaff

# Create your views here.
## RESTAURANT LIST VIEWS ##
class ListRestaurantView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListRestaurantSerializer
    filterset_class = RestaurantFilter

    def get_queryset(self):
        return Restaurant.objects.all()

## RESTAURANT CREATE VIEWS ## 
class CreateRestaurantView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        """Overwritted method to include a success message, we call super method and later update de data dictionary
            with the message        
        Returns:
            Response: response with the models data and a success message 
        """
        response = super().create(request, *args, **kwargs)
        response.data.update(message=_('Restaurant successfully created'))
        return response

    def get_serializer(self, *args, **kwargs):
        """We need to parse self.request.data in case it is a dict or a querydict

        Returns:
            ModelSerializer: serializer for Restaurant
        """
        if isinstance(self.request.data, QueryDict):
            data_dict = self.request.data.dict()

            key_list = ['address']

            for key in key_list:
                if key in self.request.data:
                    data_dict[key] = json.loads(self.request.data.get(key))    
                    
            return RestaurantModelSerializer(data=data_dict)
        
        else:   
            return RestaurantModelSerializer(data=self.request.data)

## RESTAURANT RUD VIEWS ##
class RetrieveUpdateDestroyRestaurantView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    multiple_lookup_fields = ('id', 'slug_restaurant')

    
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes == [AllowAny]
        else:
            self.permission_classes == [IsAuthenticated]

        return super(RetrieveUpdateDestroyRestaurantView, self).get_permissions()
    

    def get_serializer(self, *args, **kwargs):
        """We need to parse self.request.data in case it is a dict or a querydict

        Returns:
            ModelSerializer: serializer for Restaurant
        """
        instance = self.get_object()
        
        if self.request.method == 'PUT':
            if isinstance(self.request.data, QueryDict):
        
                data_dict = self.request.data.dict()

                key_list = ['address']

                for key in key_list:
                    if key in self.request.data:
                        data_dict[key] = json.loads(self.request.data.get(key))    
                
                return RestaurantModelSerializer(instance=instance, data=data_dict)
            
        return RetrieveRestaurantSerializer(instance=instance)

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}

        for field in self.multiple_lookup_fields:
            
            try:   # Get the result with one or more fields.
                filter[field] = self.kwargs[field]
            except Exception:
                pass

        obj = get_object_or_404(queryset, **filter)
        return obj

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data.update(message=_('Restaurant successfully edited'))
        return response

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        data = {}
        data['message']=_('Restaurant successfully deleted')
        return Response(data=data, status=status.HTTP_200_OK)

## MEDIA RESTAURANT VIEWS ##
class CreateRestaurantImageView(CreateAPIView):
    """ 
    View for create a restaurant restaurant image
    """
    permission_classes = [IsAdminUser]
    serializer_class = MediaRestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def create(self, request, *args, **kwargs):
        request.data["restaurant"] = kwargs["restaurant"]
        return super().create(request, *args, **kwargs)

class RetrieveUpdateDeleteImageView(RetrieveUpdateDestroyAPIView):
    """ 
    View for Update and Delete restaurant image
    """
    permission_classes = [IsObjAuthorOrStaff]
    serializer_class = MediaRestaurantSerializer
    queryset = MediaRestaurant.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        """
         when we update the img we need to delete the old path 
        """
        try:
            request.data["restaurant"] = kwargs["restaurant"]
            img_path = MediaRestaurant.objects.get(id=kwargs['id']).image
            os.remove("media/"+str(img_path))
        except:
            pass
        
        """
         We should have only one cover IMG , in other case the old cover img will be update to false
        """
        image_cover = MediaRestaurant.objects.filter(restaurant=request.data["restaurant"]).filter(is_cover=True)
       
        if image_cover :
            try:
                image_cover.update(is_cover=False)
            except:
                pass

        response = super().update(request, *args, **kwargs)
        response.data.update(message=_('Restaurant image successfully edited'))
        return response

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        try:
            img_path = MediaRestaurant.objects.get(id=kwargs['id']).image
            os.remove("media/"+str(img_path))
        except:
            pass
        
        super().delete(request, *args, **kwargs)
        data = {}
        data['message']=_('Restaurant image successfully deleted')
        return Response(data=data, status=status.HTTP_200_OK)


