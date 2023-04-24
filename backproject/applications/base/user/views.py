# Django imports
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _

# Third party imports
from rest_framework.serializers import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict

# Local imports
from .serializers import RegisterSerializer, LoginSerializer, EmailUserSerializer
from .models import User
from applications.utils.permissions import IsCustomerOrAdminUser

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def user_register(request):
    try:    
        data = {}
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            if serializer.data['type_user'] in (User.CUSTOMER):
    
                user = serializer.create(request.data)
                token = Token.objects.get_or_create(user=user)[0].key  
                data["message"] = _('User registered successfully')
                data["email"] = user.email
                data["user_id"] = user.id
                data['user_type'] = user.type_user
                data["token"] = 'Token ' + token
                stat = status.HTTP_201_CREATED
                user_login(request.stream)

            else:
                data["type_user"] = _('%(choice)s is not a valid choice') % {'choice': serializer.data.get('type_user')}
                stat = status.HTTP_400_BAD_REQUEST

            return Response(data, status=stat)
        
        else:
            data = serializer.errors
            stat = status.HTTP_400_BAD_REQUEST
            
            return Response(data, status=stat)

    except Exception as e:
        print (e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    data = {}
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
        email_ser = serializer.data['email']
        password = serializer.initial_data['password']
        
        try:
            user = User.objects.get(email=email_ser)
            data['email'] = user.email
            data['user_id'] = user.id
            data['user_type'] = user.type_user
        except Exception as e:
            raise ValidationError(_('Incorrect credentials, check if the email and password entered are correct.'))

        token = Token.objects.get_or_create(user=user)[0].key
        data["token"] = 'Token ' + token
        
        if not authenticate(email=email_ser, password=password):
            raise ValidationError(_('Incorrect credentials, check if the email and password entered are correct.'))
        
        login(request, user)

        data["message"] = _('User loged in successfully')
    
        return Response(data, status=status.HTTP_200_OK)
    else:
        
        data = serializer.errors   
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):

    data = {}
    request.user.auth_token.delete()

    logout(request)

    data['message'] = _('User logged out')

    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCustomerOrAdminUser,],)
def check_customer(request):
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser,],)
def check_staff(request):
    serializer = EmailUserSerializer(data=request.data)
    
    if serializer.is_valid():
        if(serializer.initial_data['email'] == request.user.email):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
