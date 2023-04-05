from django.db import models
from django.db.models.deletion import SET_NULL, PROTECT
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

# Local imports
from applications.base.timestamp.models import Timestamp

# Create your models here.
class Zone(Timestamp):
    """
    This class represents an operations area, it allows us to manage the restaurants and filter in main search
    """
    name = models.CharField(_('Zone name'), max_length=100, null=False, unique=True, db_index=True)
    description = models.TextField(_('Description'))
    assigned_postal_codes = ArrayField(models.CharField(max_length=8, blank=True), verbose_name=_('Assigned postal codes'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Zone')
        verbose_name_plural = _('Zones')

class Address(Timestamp):
    country = models.CharField(_('Country'), max_length=100, null=False)
    region = models.CharField(_('Region'), max_length=100, null=False)
    sub_region = models.CharField(_('Sub region'), max_length=100, null=True, blank=True)
    city = models.CharField(_('City'), max_length=100, null=False)
    street = models.CharField(_('Street'), max_length=150, null=False)
    number = models.CharField(_('Number'), max_length=15, null=False)
    floor = models.CharField(_('Floor'), max_length=20, blank=True)
    stair = models.CharField(_('Stair'), max_length=10, blank=True)
    door = models.CharField(_('Door'), max_length=10, blank=True)
    postal_code = models.CharField(_('Postal code'), max_length=10, null=False)
    latitude = models.DecimalField(_('Latitude'), max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(_('Longitude'), max_digits=9, decimal_places=6, null=True)
    zone = models.ForeignKey(to=Zone, on_delete=SET_NULL, null=True, related_name='address', verbose_name=_('Zone'), blank=True, help_text =_('This field is automatically assigned via the postal code.'))

    def __str__(self):
        if self.floor:
            return (f'{self.street} {self.number}, {self.floor}º {self.door}, {self.city}')
        return (f'{self.street} {self.number}, {self.city}')

    def save(self, *args, **kwargs):

        try:
            self.zone = Zone.objects.filter(assigned_postal_codes__contains=[self.postal_code])[0]
        except:
            self.zone = None
        
        return super(Address, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')