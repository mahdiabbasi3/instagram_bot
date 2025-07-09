import schedule
import time
from telegram_bot import send_telegram_message
from report_generator import generate_report

def job():
    report = generate_report()
    send_telegram_message(report)

schedule.every().day.at("20:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)