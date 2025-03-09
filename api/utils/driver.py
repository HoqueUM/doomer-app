"""
Main logic of adding new articles to the database.
"""

from utils.supabase_interface import SupabaseInterface
from utils.scraper import Scraper
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

    async def fetch_doomer(self, session, article):
        url = "https://rhoque-doomer.hf.space/doomer"
        async with session.post(url, json={"title": article["title"]}) as response:
            return await response.json(), article
    
    async def fetch_sentiment(self, session, article):
        url = "https://rhoque-doomer.hf.space/sentiment"
        async with session.post(url, json={"title": article["title"]}) as response:
            return await response.json()

    async def driver(self):
        print("Driver started.")
        print("Scraping articles...")
        articles = self.scraper.get_articles()
        
        print("Scraping complete.")
        print("Starting container...")
    
        #self.api.restart_space(repo_id="rhoque/doomer", token=self.token)

        print("Container started.")
        print("Fetching sentiment...")
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_doomer(session, article) for article in articles]
            doomers = await asyncio.gather(*tasks)
            tasks = [self.fetch_sentiment(session, article) for article in articles]
            sentiments = await asyncio.gather(*tasks)

            print("Sentiment fetched.")
            print("Adding articles to database...")
            for (doomer_response, article), sentiment_response in zip(doomers, sentiments):
                if ((doomer_response["sentiment"] == "doomer" and doomer_response["score"] >= .9948) or (doomer_response["sentiment"] == "not doomer" and (.97 < doomer_response["score"] and doomer_response["score"] < .99))) and sentiment_response["sentiment"] == "Negative":
                    self.supabase.insert_news(article)
            print("Articles added to database.")
            print("Pausing container...")
            #self.api.pause_space(repo_id="rhoque/doomer", token=self.token)
            print("Container paused.")
            print("Driver complete.")

