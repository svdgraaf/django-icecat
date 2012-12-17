try:
    from django.conf import settings
except ImportError:
    # We do not need Django to used this package
    settings = {}

# Required settings
API_USERNAME = getattr(settings, 'ICECAT_API_USERNAME', None)
API_PASSWORD = getattr(settings, 'ICECAT_API_PASSWORD', None)
API_LANGUAGE = getattr(settings, 'ICECAT_LANGUAGE_ID', 2)

TMP_PATH = getattr(settings, 'ICECAT_TMP_PATH', '/tmp/')