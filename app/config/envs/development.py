from .common import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS  =  [
   'daphne',
   'drf_spectacular',
] + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB', 'django_db'),
        'USER': environ.get('POSTGRES_USER','django_user'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD','123456'),
        'HOST': 'postgres',
        'PORT': '5432',
        


    }
}
