# Django imports
from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy

from applications.base.plate.models import Plate
from applications.base.timestamp.models import Timestamp

class Menu(Timestamp):
    name = models.CharField(_('Name menu'), max_length=50, null=False)
    starter = models.ManyToManyField(Plate, related_name='starter_menu', limit_choices_to={'type_plate': 'S'})
    main = models.ManyToManyField(Plate, related_name='main_menu', limit_choices_to={'type_plate': 'M'})
    dessert = models.ManyToManyField(Plate, related_name='dessert_menu', limit_choices_to={'type_plate': 'D'})

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')

    def __str__(self):
        return self.name
