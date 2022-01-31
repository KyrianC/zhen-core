import os
from .base import *

ALLOWED_HOSTS = ["*"]


CORS_ORIGIN_WHITELIST = (
    "http://localhost:8000",
    "http://localhost:3000",
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# rest auth
LOGIN_URL = "http://localhost:3000/login"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("POSTGRES_ENGINE"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}
