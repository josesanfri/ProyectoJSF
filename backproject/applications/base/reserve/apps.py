from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
    

class ReserveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base.reserve'
    label = 'reserveApp'
    verbose_name = _('Reserve')