# Django imports
from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE
from django.utils.translation import gettext_lazy as _

# Local imports
from applications.base.timestamp.models import Timestamp
from .functions import curriculum_path

# Create your models here.
class AbstractLead(Timestamp):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=254, null=False)
    prefix_phone = models.CharField(_('Phone country code'), max_length=5, null=False)
    phone = models.CharField(_('Phone'), max_length=20, null=False)

    class Meta:
        abstract = True

class JobApplication(AbstractLead):
    INTERNSHIP = 'I'
    JOB = 'J'

    JOB_LEAD_TYPE_CHOICES = [
        (INTERNSHIP, _('Internship')),
        (JOB, _('Job'))
    ]

    NIF = models.CharField(_('ID card'), max_length=20)
    age = models.CharField(_('Age'), max_length=5)
    origin = models.CharField(_('How did you hear about us?'), max_length=100)
    type_job = models.CharField(_('Job application type'), choices=JOB_LEAD_TYPE_CHOICES, max_length=1, null=True)
    studies = models.CharField(_('Studies'), max_length=100)
    city = models.CharField(_('City'), max_length=100)
    curriculum = models.FileField(_('Curriculum Vitae'), upload_to=curriculum_path)
    information = models.CharField(_('Leave us a message'), max_length=200)

    class Meta:
        verbose_name = _('Job application')
        verbose_name_plural = _('Job applications')

    def __str__(self):
        return _('%(name)s is looking for a %(type_job)s in %(city)s') % {'name' : self.name, 'type_job' : self.type_job, 'city' : self.city}


class ContactForm (AbstractLead):
    surname = models.CharField(_('Last name'), max_length=100)
    information = models.CharField(_('Leave us a message'), max_length=400)

    class Meta:
        verbose_name = _('Contact form')
        verbose_name_plural = _('Contact forms')

    def __str__(self):
        return _('%(name)s wants contact with us') % {'name' : self.name }