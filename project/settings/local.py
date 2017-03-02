from .base import *

DEBUG = True
THUMBNAIL_DEBUG = True

STATIC_ROOT = BASE_DIR + "/static"

# WARNING: do not run with local settings in production. The secret
# key below is a dummy value for use only when you don't care about 
# authentication security (i.e. developing on your local machine).
SECRET_KEY = "unsecure-dummy-development"

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
