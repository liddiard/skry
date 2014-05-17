from .base import *

DEBUG = True

STATIC_ROOT = BASE_DIR + "/static"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']


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
