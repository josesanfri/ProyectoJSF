# Django imports
from django.apps import apps
from django.db import models
from django.db.models.deletion import SET_NULL
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy

from applications.base.timestamp.models import Timestamp
from applications.utils.validators import validate_positive_value


class Plate(Timestamp):
    STARTER = 'S'
    MAIN = 'M'
    DESSERT = 'D'
    PLATES_TYPE_CHOICES = [ 
        (STARTER, _('Starter')),
        (MAIN, _('Main')),
        (DESSERT, _('Dessert')),
    ]

    type_plate = models.CharField(_('Plate type'), max_length=1, null=False, choices=PLATES_TYPE_CHOICES)
    name = models.CharField(_('Name'), max_length=100, null=False)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, validators=[validate_positive_value])
    ingredients = models.TextField(_('Ingredients'), null=True, blank=True, help_text=_('You can write the plate ingredients.'))

    def __str__(self):
        return _('%(type_plate)s in %(name)s') % {'type_plate' : self.get_type_plate_display(), 'name': self.name}

    class Meta:
        verbose_name = _('Plate')
        verbose_name_plural = _('Plates')

