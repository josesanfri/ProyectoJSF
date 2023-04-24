# Django imports
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Local imports
from applications.base.timestamp.models import Timestamp
from applications.base.user.models import User
from applications.base.location.models import Address
from applications.utils.image.format import restaurant_formatter_image
from .functions import restaurant_image_path

# Put next 3 imports in her place
from django.core.files.base import ContentFile

# Create your models here.
class AbstractRestaurant(Timestamp):
    address = models.ForeignKey(to=Address, on_delete=SET_NULL, null=True, related_name='%(class)s_set', verbose_name=_('Address'))
    name_restaurant = models.CharField('Name Restaurant', max_length=100, null=False)
    square_meters = models.PositiveSmallIntegerField(_('Square meters'), null=False)
    primary_phone = models.CharField(_('Primary phone'), max_length=16, null=False)
    description = models.TextField(_('Description'), null=True, blank=True)
    slug_restaurant = models.SlugField(_('Slug'), max_length=100, unique=True, null=True, blank=True)
    
    def __str__(self):
        return _('%(name_restaurant)s in %(address)s') % {'name_restaurant' : self.name_restaurant, 'address': self.address}

    def save(self, *args, **kwargs):
        super(AbstractRestaurant, self).save(*args, **kwargs)
        if not self.slug_restaurant:
            self.slug_restaurant = slugify(self.name_restaurant + '-' + self.address.street + '-' + self.address.city + '-' + str(self.id))
            self.save()

    class Meta:
        abstract = True

class Restaurant(AbstractRestaurant):
    is_managed = models.BooleanField(_('Managed'), default=False)
    management_user = models.ForeignKey(to=User, on_delete=SET_NULL, null=True, blank=True, related_name="%(class)s_managed", verbose_name=_('Management user'))
    caption_user = models.ForeignKey(to=User, on_delete=SET_NULL, null=True, blank=True, related_name="%(class)s_captured", verbose_name=_('Caption user'))

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')

class MediaRestaurant(Timestamp):
    LOUNGE = "LG"
    TERRACE = "TR"

    IMAGE_TYPE_CHOICES = [
        (LOUNGE, _('Lounge room')),
        (TERRACE, _('Terrace'))
    ]

    restaurant = models.ForeignKey(to=Restaurant, on_delete=CASCADE, related_name='media_restaurant', verbose_name=_('Restaurant'))
    image = models.ImageField(_('Image'), upload_to=restaurant_image_path)
    is_cover = models.BooleanField(_('Cover'), default=False)
    type_image = models.CharField(_('Image type'), max_length=2, blank=True, choices=IMAGE_TYPE_CHOICES)

    def save(self,*args,**kwargs):
            """
            Function to format img before save it using our format function 
            """
            if self.image:
                image , image_io , filename = restaurant_formatter_image(self.image)
                image.save(image_io, format='webp', quality=90)
                self.image.save(filename, ContentFile(image_io.getvalue()), save=False)
            
            super(MediaRestaurant, self).save(*args, **kwargs)

    def __str__(self):
        return _('Image of %(type_image)s from %(restaurant)s') % { 'type_image' : self.get_type_image_display(),'restaurant' : self.restaurant}
    
    class Meta:
        verbose_name = _('Restaurant multimedia')
        verbose_name = _('Restaurants multimedia')