# scheduling.py

import schedule
import time

def job():
    print("Scheduled job running...")

def schedule_bot_run():
    schedule.every().hour.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
