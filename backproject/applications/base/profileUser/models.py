# Python imports
from datetime import date
import uuid

#Django imports
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.translation import gettext_lazy as _

#Local imports
from applications.base.location.models import Address
from applications.base.timestamp.models import Timestamp
from applications.base.user.models import User
from applications.base.department.models import Department
from .functions import profile_image_directory_path
from .managers import ProfileManager

# Create your models here.
class AbstractProfile(Timestamp):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (OTHER, _('Other')),
    ]

    user = models.OneToOneField(User, on_delete=CASCADE, related_name='%(class)s', verbose_name=_('User'))
    image = models.ImageField(_('Image'), upload_to=profile_image_directory_path, blank=True)
    first_name = models.CharField(_('Name'), max_length=100, null=False)
    last_name = models.CharField(_('Last name'), max_length=100, null=False)
    prefix_phone = models.CharField(_('Phone country code'), max_length=6, null=False)
    phone = models.CharField(_('Phone number'), max_length=20, null=False, help_text=_('Personal number phone'))
    birth_date = models.DateField(_('Birth date'), null=False)
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES, blank=True)
    annotation_gender = models.CharField(_('I identify as a:'), max_length=30, blank=True)
    address = models.ForeignKey(to=Address, on_delete=CASCADE, null=True, related_name='%(class)s', verbose_name=_('Address'))

    objects = ProfileManager()

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

    class Meta:
        abstract = True

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - \
        ((today.month, today.day) <
        (self.birth_date.month, self.birth_date.day))
 
        return age

class CustomerProfile(AbstractProfile):
    class Meta:
        verbose_name = _('Customer profile')
        verbose_name_plural = _('Customer profiles')

class StaffProfile(AbstractProfile):
    department = models.ForeignKey(to=Department, on_delete=SET_NULL, null=True, related_name='%(class)s', verbose_name = _('Department'))
    prefix_company_phone = models.CharField(_('Company phone country code'), max_length=5, blank=True)
    company_phone = models.CharField(_('Company phone'), max_length=20, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = _('Staff profile')
        verbose_name_plural = _('Staff profiles')
