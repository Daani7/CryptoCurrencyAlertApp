# CryptoAlerts

## Description
CryptoAlerts is a Django web application for managing cryptocurrency alerts. It allows users to create, read, update, and delete alerts for various cryptocurrencies. Additionally, the application provides a mechanism for listening to cryptocurrency price changes in real-time and sending alerts to users.

## Features
- Create, read, update, and delete cryptocurrency alerts
- Real-time monitoring of cryptocurrency price changes
- Notification mechanism (display or email) for alert triggers

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:Daani7/CryptoCurrencyAlertApp.git

2. Navigate to the project directory:
cd CryptoAlerts

3. Install dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python3 manage.py migrate

5. Start the Django server:
python3 manage.py runserver

6. Start the WebSocket listener
python3 websocket_listener.py

## Usage
- Visit the web application in your browser: http://localhost:8000/register
- Sign up or log in to create and manage cryptocurrency alerts.
- Set your desired price thresholds for alerts.
- Receive notifications when cryptocurrency prices meet your specified criteria.

## Dependencies
- Django
- Django Channels (for WebSocket support)

## License
MIT License

Ce README.md décrit comment installer, exécuter et utiliser votre application CryptoAlerts.
