from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
    
class RestaurantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base.restaurant'
    label = 'restaurantApp'
    verbose_name = _('Restaurant')
