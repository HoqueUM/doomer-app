from driver import Driver
import asyncio
import dotenv
import os

dotenv.load_dotenv()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
table = "Current News"
token = os.environ.get("HF_TOKEN")

driver = Driver(supabase_url, supabase_key, table, token)

asyncio.run(driver.driver())