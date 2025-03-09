from bs4 import BeautifulSoup
import requests
import json
from unidecode import unidecode
import praw
import os
from random_user_agent.user_agent import UserAgent


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