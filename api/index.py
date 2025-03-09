from flask import Flask
import threading
import os
import dotenv
import aiohttp
import asyncio
import time
from supabase import create_client
from huggingface_hub import HfApi
from random_user_agent.user_agent import UserAgent
from bs4 import BeautifulSoup
import requests
import praw

class SupabaseInterface:
    def __init__(self, url, key, table):
        self.supabase = create_client(url, key)
        self.table = table

    def insert_news(self, article):
        """Insert article into the table."""
        try:
            self.supabase.table(self.table).insert(article).execute()
        except Exception as e:
            if "duplicate key value violates unique constraint" in str(e):
                pass
            else:
                raise
    
    def upsert_news(self, article):
        """Upsert article into the table."""
        self.supabase.table(self.table).upsert(article, on_conflict=["title"]).execute()    
    def get_news(self):
        """Get all news currently in the table."""
        response = self.supabase.table(self.table).select("*").execute()
        return response.data
    
    def delete_news(self, title):
        """Delete news with the specified title."""
        self.supabase.table(self.table).delete().eq("title", title).execute()


class Scraper:
    def __init__(self):
        self.ua = UserAgent()
    def get_brutalist_report(self, url):
        response = requests.get(url, headers={'User-Agent': self.ua.get_random_user_agent()})
        soup = BeautifulSoup(response.text, 'html.parser')
        lis = soup.find('div', class_='brutal-grid').find_all('li')

        hrefs = []

        for li in lis:
            hrefs.append(li.find('a'))

        result = []

        for href in hrefs:
            if href:
                title = href.get_text()
                result.append({"title": title.strip('...'), "link": href['href']})

        return result

    def get_alltop_news(self, url):
        response = requests.get(url, headers={'User-Agent': self.ua.get_random_user_agent()})
        soup = BeautifulSoup(response.text, 'html.parser')
        hrefs = soup.find_all('a', class_='one-line-ellipsis')

        result = []

        for href in hrefs:
            title = href.get_text()
            if 'twitter' in href['href']:
                break
            result.append({"title": title, "link": href['href']})

        return result


    def get_timef(self, url):
        response = requests.get(url, headers={'User-Agent': self.ua.get_random_user_agent()})
        soup = BeautifulSoup(response.text, 'html.parser')
        hrefs = soup.find('div', class_='postList').find_all('a')

        result = []

        for href in hrefs:
            title = href.get_text()
            if '.com' in title:
                continue
            result.append({"title": title, "link": href['href']})

        return result

    def get_reddit(self):
        client = os.environ.get("REDDIT_CLIENT_ID")
        secret = os.environ.get("REDDIT_SECRET")

        reddit = praw.Reddit(client_id=client, client_secret=secret, user_agent='doomer/1.0 by u/Your-Simp-Card')

        subreddit = reddit.subreddit('collapse').hot(limit=100)

        result = []

        for submission in subreddit:
            if not submission.is_self and "redd.it" not in submission.url:
                result.append({"title": submission.title, "link": submission.url})
            if len(result) == 10:
                break
        return result

    def get_articles(self):
        return self.get_brutalist_report('https://brutalist.report/topic/science?') + self.get_brutalist_report('https://brutalist.report/topic/politics?') + self.get_alltop_news('https://alltop.com/news') + self.get_alltop_news('https://alltop.com/politics') + self.get_timef('https://timef.com/') + self.get_reddit()

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

def main():
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    table = "Current News"
    token = os.environ.get("HF_TOKEN")

    driver = Driver(supabase_url, supabase_key, table, token)

    while True:
        asyncio.run(driver.driver())
        time.sleep(3600)

dotenv.load_dotenv()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
table = "Current News"


supabase = SupabaseInterface(supabase_url, supabase_key, table)

app = Flask(__name__)



@app.route("/api/get_news")
def hello_world():
    return supabase.get_news()

thread = threading.Thread(target=main)

thread.start()


if __name__ == "__main__":
    app.run(port=5328)