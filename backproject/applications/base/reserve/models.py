# Python imports
from datetime import datetime

# Django imports
from django.apps import apps
from django.db import models
from django.db.models.deletion import SET_NULL
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy
from django.core.validators import MaxValueValidator, MinValueValidator

# Local imports
from applications.base.restaurant.models import Restaurant
from applications.base.user.models import User
from applications.base.timestamp.models import Timestamp


# Create your models here.
class Reserve(Timestamp):
    WEB = 'W'
    RESTAURANT = 'R'
    RESERVE_TYPE_CHOICES = [ 
        (WEB, _('Web')),
        (RESTAURANT, _('Restaurant')),
    ]

    CONFIRMED = 'C'
    DENIED = 'D'
    RESERVE_STATUS_CHOICES = [ 
        (CONFIRMED, pgettext_lazy('Reserve confirmed', 'Confirmed')),
        (DENIED, _('Denied')),
    ]
   
    restaurant = models.ForeignKey(to=Restaurant, on_delete=SET_NULL, null=True, related_name='%(class)s', verbose_name=_('Restaurant'))
    customer = models.ForeignKey(to=User, on_delete=SET_NULL, null=True, related_name='%(class)s', verbose_name=_('Main customer'))
    num_customers = models.IntegerField(default=2, validators=[MaxValueValidator(13),MinValueValidator(1)], null=False)
    confirmed_date = models.DateTimeField(_('Confirmation date'), null=True, blank=True)
    type_reserve = models.CharField(_('Reserve type'), max_length=1, null=False, choices=RESERVE_TYPE_CHOICES, default=WEB)
    status = models.CharField(_('Status'), max_length=1, null=False, choices=RESERVE_STATUS_CHOICES, default=CONFIRMED)
    intern_note = models.TextField(_('Intern note'), null=True, blank=True, help_text=_('You can write a note here that might be of interest to your colleagues.'))

    class Meta:
        verbose_name = _('Reserve')
        verbose_name_plural = _('Reserves')

    def __str__(self):
        return _('%(customer)s reserve over %(restaurant)s') % {'customer' : self.customer, 'restaurant' : self.restaurant}
    
    def save(self, *args, **kwargs):
        # When we confirm a Reserve, we must do some related busines logic
        if self.status == Reserve.CONFIRMED:
            if self.confirmed_date is None:
                self.confirmed_date = datetime.now()
                    
            return super(Reserve, self).save(*args, **kwargs)
        
        else:
            super(Reserve, self).save(*args, **kwargs)