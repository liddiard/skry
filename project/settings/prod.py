from .base import *
from .secret import SECRET_KEY

DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'dailybruin', 
        'USER': 'dailybruin',
        'PASSWORD': 'bruin111',
        'HOST': 'localhost',
        'PORT': '',
    }
}
