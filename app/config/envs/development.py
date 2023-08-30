from .common import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS  =  [
   'daphne',
   'drf_spectacular', #for writing document | make a swagger for us
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

REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
