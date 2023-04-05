# Python imports
import os

# Django imports
from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the %s environment variable' % env_variable
        raise ImproperlyConfigured(error_msg)