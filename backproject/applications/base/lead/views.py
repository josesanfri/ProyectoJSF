# Django imports
from django.utils.translation import gettext as _
from requests import request

# Third party imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView ,RetrieveUpdateDestroyAPIView

# Local imports
from .serializers import JobApplicationSerializer , ContactFormSerializer
from .models import JobApplication , ContactForm

# Create your views here
## VIEWS FOR JOB APPLICATIONS
class JobApplicationListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    
class JobApplicationCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data.update(message=_('Job Application successfully created'))
        return response

class RetrieveUpdateDeleteJobApplicationView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data.update(message=_('Job application successfully edited'))
        return response
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        data = {}
        data.update(message=_('Job application successfully deleted'))
        return Response (data=data , status = status.HTTP_200_OK)


## VIEWS FOR CONTACT FORMS
class ContactFormCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactFormSerializer

class ContactFormListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class RetrieveUpdateDestroyContactFormView(RetrieveUpdateDestroyAPIView) :
    permission_classes = [IsAdminUser]
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data.update(message=_('Contact form successfully edited'))
        return response
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        data = {}
        data.update(message=_('Contact form successfully deleted'))
        return Response (data=data , status = status.HTTP_200_OK)
    