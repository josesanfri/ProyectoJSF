from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
    

class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base.menu'
    label = 'menuApp'
    verbose_name = _('Menu')
