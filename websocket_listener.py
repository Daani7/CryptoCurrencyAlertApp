import os
import django
from django.conf import settings

# Configuration des paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_alerts.settings')
django.setup()

# Maintenant, vous pouvez importer les modèles Django
from alerts.models import CryptoAlert
from django.core.mail import send_mail
from django.template.loader import render_to_string
import websocket
import json

def on_message(ws, message):
    print(message)
    data = json.loads(message)
    crypto_id = data.get('symbol_id')
    price = data.get('price')
    alerts = CryptoAlert.objects.filter(cryptocurrency=crypto_id, email_sent=False)
    for alert in alerts:
        if alert.alert_type == 'below' and price <= alert.price:
            alert.message = f"Le prix de {alert.cryptocurrency} est en dessous de {alert.price}"
            alert.save()
            send_alert_email(alert)
            alert.email_sent = True  # Marquer l'e-mail comme envoyé
            alert.save()
        elif alert.alert_type == 'above' and price >= alert.price:
            alert.message = f"Le prix de {alert.cryptocurrency} est au-dessus de {alert.price}"
            alert.save()
            send_alert_email(alert)
            alert.email_sent = True  # Marquer l'e-mail comme envoyé
            alert.save()

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def send_alert_email(alert):
    subject = f"Nouvelle alerte pour: {alert.name}"
    message = f"""
    Alerte Cryptomonnaie

    Nom de l'alerte: {alert.name}
    Cryptomonnaie: {alert.cryptocurrency}
    Date de création: {alert.created_date.strftime('%d/%m/%Y %H:%M:%S')}
    Prix: {alert.price}
    Message: {alert.message}
    """
    send_mail(subject, message, 'dani.derbala77210@gmail.com', [alert.user.email])

def on_open(ws):
    subscription_request = {
        "type": "hello",
        "apikey": "6E55241E-C793-4CAA-B67F-97816EE62A69",
        "subscribe_data_type": ["trade"],
        "subscribe_filter_symbol_id": ["KRAKEN_SPOT_BTC_USD", "KRAKEN_SPOT_BTC_EUR"]
    }
    ws.send(json.dumps(subscription_request))

def start_websocket_listener():
    ws = websocket.WebSocketApp("wss://ws.coinapi.io/v1",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    start_websocket_listener()
