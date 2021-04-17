from bs4 import BeautifulSoup
import re
import os
import sys
import requests
import pandas as pd
from datetime import date


class Webscraper:

    def __init__(self, websites):
        self.news_websites = websites
        self.news_data = {'apnews': None, 'reuters': None, 'washingtonpost': None, 'nytimes': None}
        self.df = None
        self.scrape_articles()
        self.clean_articles()
        self.create_df()
        self.save_df_as_csv()

    def scrape_articles(self):
        for news_org in self.news_websites:
            res = requests.get(news_org)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, features='lxml')
            links = soup.find_all('a')  # 'a' tags implies URL
            article_list = []

            if 'apnews' in news_org:
                for link in links:
                    link_str = link.get('href')
                    if 'article' in str(link_str):
                        article_list.append(link_str)
                self.news_data['apnews'] = article_list

            elif 'reuters' in news_org:
                for link in links:
                    link_str = str(link.get('href'))
                    match = re.match(r"(.)+(\d\d\d\d-\d\d-\d\d)(.)+", link_str)
                    if match:
                        article_list.append(link_str)
                self.news_data['reuters'] = article_list

            elif 'washingtonpost' in news_org:
                for link in links:
                    link_str = link.get('href')
                    match = re.match('(.)+(\d\d\d\d/\d\d/\d\d)(.)+', link_str)
                    if match:
                        article_list.append(link_str)
                    self.news_data['washingtonpost'] = article_list

            elif 'nytimes' in news_org:
                for link in links:
                    link_str = link.get('href')
                    match = re.match('(.)+(\d\d\d\d/\d\d/\d\d)(.)+', link_str)
                    if match:
                        article_list.append(link_str)
                self.news_data['nytimes'] = article_list

    def clean_articles(self):
        for news_org in self.news_websites

    def create_df(self):
        df = pd.DataFrame.from_dict(self.news_data, orient='index')
        df.drop_duplicates(inplace=True)
        self.df = df.transpose()
        print(df.describe())

        today = date.today()

    def save_df_as_csv(self):
        self.df.to_csv('articles')
