import requests
import bot_config

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_config.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": bot_config.TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)
    