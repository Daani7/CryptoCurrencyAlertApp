# crypto_alerts/celery.py

import os
from celery import Celery

# Réglages de l'environnement Django pour que Celery puisse trouver le projet Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_alerts.settings')

# Création de l'application Celery
app = Celery('crypto_alerts')

# Chargement de la configuration Celery depuis les réglages Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-découverte des tâches Celery dans les applications Django
app.autodiscover_tasks()
