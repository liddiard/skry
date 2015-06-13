from .base import *

DEBUG = True
THUMBNAIL_DEBUG = True

STATIC_ROOT = BASE_DIR + "/static"


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'skry',
        'USER': 'skry',
        'PASSWORD': 'skry',
        'HOST': 'localhost',
        'PORT': '',
    }
}
