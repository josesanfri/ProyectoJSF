from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
    
class ProfileuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base.profileUser'
    label = 'profileApp'
    verbose_name = _('Profile User')
    