from django.conf import settings

from .base import *


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "27x!$jz&ci=b9*&)kdpzc1y0#%2locoo3$_1sw%)uj(zk9t@@@"

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = []

# https://django-debug-toolbar.readthedocs.io/en/latest/index.html
# INSTALLED_APPS.append("debug_toolbar")
# MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = [
    "127.0.0.1",
]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "localdb",
        "USER": "postgres",
        "PASSWORD": "nsh0288",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
