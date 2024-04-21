from celery import shared_task
from django.contrib import messages
from .models import CryptoAlert
import requests

@shared_task
def check_crypto_prices():
    alerts = CryptoAlert.objects.all()
    for alert in alerts:
        crypto_id = alert.cryptocurrency
        price = alert.price
        alert_type = alert.alert_type
        current_price = get_current_price(crypto_id)

        if current_price:
            if alert_type == 'below' and current_price <= price:
                send_alert_notification.delay(alert.id, current_price, 'below')
            elif alert_type == 'above' and current_price >= price:
                send_alert_notification.delay(alert.id, current_price, 'above')

def get_current_price(crypto_id):
    url = f"https://rest.coinapi.io/v1/assets/{crypto_id}/"
    headers = {"X-CoinApi-Key": "6E55241E-C793-4CAA-B67F-97816EE62A69"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data_list = response.json()
        if data_list and isinstance(data_list, list) and len(data_list) > 0:
            data = data_list[0]
            return data.get('price_usd')
    return None

@shared_task
def send_alert_notification(alert_id, price, type):
    alert = CryptoAlert.objects.get(pk=alert_id)
    message = f"Nouvelle notification pour l'alerte: {alert.cryptocurrency}, le prix est {type} le prix spécifié: {price}"
    alert.message = message
    alert.save()
