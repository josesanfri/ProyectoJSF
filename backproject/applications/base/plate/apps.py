from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
    

class PlateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base.plate'
    label = 'plateApp'
    verbose_name = _('Plate')