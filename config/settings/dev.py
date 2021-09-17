from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# rest auth
LOGIN_URL = "http://localhost:3000/login"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Zhen",
        "USER": "kyrian",
        "HOST": "127.0.0.1",
    }
}
