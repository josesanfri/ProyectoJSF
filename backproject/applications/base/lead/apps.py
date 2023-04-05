from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class LeadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base.lead'
    label = 'leadApp'
    verbose_name = _('Leads')