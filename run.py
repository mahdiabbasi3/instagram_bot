from telegram_bot import send_telegram_message
from report_generator import generate_report

if __name__ == '__main__':
    send_telegram_message(generate_report())