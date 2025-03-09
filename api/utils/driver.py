"""
Main logic of adding new articles to the database.
"""

from supabase_interface import SupabaseInterface
from scraper import Scraper
import aiohttp
import asyncio
import time
from huggingface_hub import HfApi

class Driver:
    def __init__(self, url, key, table, token):
        self.scraper = Scraper()
        self.supabase = SupabaseInterface(url, key, table)
        self.token = token
        self.api = HfApi()

    async def fetch_sentiment(self, session, article):
        url = "https://rhoque-doomer.hf.space/sentiment"
        async with session.post(url, json={"title": article["title"]}) as response:
            return await response.json(), article

    async def driver(self):
        print("Driver started.")
        print("Scraping articles...")
        articles = self.scraper.get_articles()
        
        print("Scraping complete.")
        print("Starting container...")
    
        self.api.restart_space(repo_id="rhoque/doomer", token=self.token)

        print("Container started.")
        print("Fetching sentiment...")
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_sentiment(session, article) for article in articles]
            responses = await asyncio.gather(*tasks)

            print("Sentiment fetched.")
            print("Adding articles to database...")
            for response, article in responses:
                if response["sentiment"] == "doomer" and response["score"] > .998:
                    self.supabase.insert_news(article)
            print("Articles added to database.")
            print("Pausing container...")
            self.api.pause_space(repo_id="rhoque/doomer", token=self.token)
            print("Container paused.")
            print("Driver complete.")

