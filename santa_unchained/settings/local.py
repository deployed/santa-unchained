from .base import *

SECRET_KEY = "secret_key"

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "santa_unchained"),
        "USER": env("POSTGRES_USER", "santa_unchained"),
        "PASSWORD": env("POSTGRES_PASSWORD", "santa_unchained"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}

CSRF_TRUSTED_ORIGINS = ["https://*.github.dev"]
