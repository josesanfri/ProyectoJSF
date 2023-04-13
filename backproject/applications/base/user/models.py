# Django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Local imports
from .managers import UserManager
from applications.base.timestamp.models import Timestamp

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, Timestamp):
    CUSTOMER = 'CUS'
    STAFF = 'STF'

    USER_TYPE_CHOICES = [
        (CUSTOMER, _('Customer')),
        (STAFF, _('Staff'))
    ]
   
    email = models.EmailField(unique = True, max_length=254)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'),)
    type_user = models.CharField(_('User type'), max_length=3, choices= USER_TYPE_CHOICES)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_short_name(self):
        return self.email
    