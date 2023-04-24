# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

from . import viewsets 
from .views import (JobApplicationListView, JobApplicationCreateView, RetrieveUpdateDeleteJobApplicationView,
                    ContactFormListView, ContactFormCreateView, RetrieveUpdateDestroyContactFormView)

# Create your urls here.
urlpatterns = [
    # Job applications
    path('api/lead/job/', JobApplicationListView.as_view(), name='job-application-list'),
    path('api/lead/job/create/', JobApplicationCreateView.as_view(), name='job-application-create'),
    path('api/lead/job/<int:pk>', RetrieveUpdateDeleteJobApplicationView.as_view(), name='job-application-update'),

    # Contact form
    path('api/lead/contact/', ContactFormListView.as_view(), name='contact-form-list'),
    path('api/lead/contact/create/', ContactFormCreateView.as_view(), name='contact-form-create'),
    path('api/lead/contact/<int:id>', RetrieveUpdateDestroyContactFormView.as_view(), name='contact-form-update'),
]
