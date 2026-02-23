import os
from django.core.asgi import get_asgi_application

# Ajustado de 'django_serializers.settings' para 'setup_django.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup_django.settings")

application = get_asgi_application()
