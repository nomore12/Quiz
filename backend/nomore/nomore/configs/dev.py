from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "27x!$jz&ci=b9*&)kdpzc1y0#%2locoo3$_1sw%)uj(zk9t@@@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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