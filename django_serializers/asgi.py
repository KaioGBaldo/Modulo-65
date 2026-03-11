# django_serializers/asgi.py
import os
from django.core.asgi import get_asgi_application

# Ajustado para o nome correto do seu diretório de configurações
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_serializers.settings')

application = get_asgi_application()