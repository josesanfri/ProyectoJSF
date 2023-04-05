# Third party import
from rest_framework import serializers

# Local imports
from .models import JobApplication , ContactForm

class JobApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        fields = '__all__'

class ContactFormSerializer (serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'