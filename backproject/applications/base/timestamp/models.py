from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Timestamp(models.Model):
    """Base class to create Timestamps linked to a user

    Args:
        models ([Model]): Base Model
    """
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name=_('Created by'))
    updated_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name=_('Updated by'))

    class Meta:
        abstract = True
