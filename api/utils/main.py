from utils.driver import Driver
import asyncio
import os
import time
import datetime
import pytz


def main():
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    table = "Current News"
    token = os.environ.get("HF_TOKEN")

    driver = Driver(supabase_url, supabase_key, table, token)

    est = pytz.timezone('US/Eastern')
    while True:
        now = datetime.datetime.now(est)
        if now.hour == 17:
            asyncio.run(driver.driver())
            time.sleep(3600)