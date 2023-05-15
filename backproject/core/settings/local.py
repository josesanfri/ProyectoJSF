# Local imports
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = DEBUG

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'projectdb',
        'USER': 'josesanfri',
        'PASSWORD': 'admin_',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static_dir/'
STATICFILES_DIRS = [ BASE_DIR / 'static_dir'] 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print("MEDIA ROOT DAD", MEDIA_ROOT)
print("BASE DIR DAD", BASE_DIR)
print("STATIC DIR DAD", STATICFILES_DIRS)

# REST FRAMEWORK LOCAL OPTIONS
REST_FRAMEWORK = REST_FRAMEWORK | {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  
    ]
}