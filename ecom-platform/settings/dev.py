from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TODO: CHECAR SECRET KEY

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-aaa&@&ej+194-qsnt)k01v*plu^_+u_!=)8gn#lrj&%^e=z4u&"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
