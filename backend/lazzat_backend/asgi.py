"""
ASGI config for lazzat_backend project.
Supports WebSocket connections via Daphne.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lazzat_backend.settings')

application = get_asgi_application()
