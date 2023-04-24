from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TimestampConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.base.timestamp'
    label = 'timestampApp'
    verbose_name = _('Timestamp')
