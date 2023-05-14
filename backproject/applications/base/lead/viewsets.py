# Third party imports
from rest_framework import viewsets

# Local imports 
from .models import ContactForm, JobApplication
from .serializers import ContactFormSerializer, JobApplicationSerializer

# Create your viewsets here
class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class JobFormViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer