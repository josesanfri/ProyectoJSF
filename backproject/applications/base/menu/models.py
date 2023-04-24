# Python imports
from datetime import date

#Django imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

#Local imports
from applications.base.timestamp.models import Timestamp
from applications.base.plate.models import Plate

class Menu(Timestamp):
    name = models.CharField(_('Name'), max_length=100, null=False)
    starter = models.ManyToManyField(to=Plate, related_name='starter', verbose_name=('Starter plate'),  limit_choices_to={'type_plate': 'starter'}, blank=True)
    main = models.ManyToManyField(to=Plate, related_name='main', verbose_name=('Main plate'), limit_choices_to={'type_plate': 'main'}, blank=True)
    dessert = models.ManyToManyField(to=Plate, related_name='dessert', verbose_name=('Dessert plate'), limit_choices_to={'type_plate': 'dessert'}, blank=True)
    slug_menu = models.SlugField(_('Slug'), max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)
        if not self.slug_menu:
            self.slug_menu = slugify(self.name + '-' + str(self.id))
            self.save()

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')