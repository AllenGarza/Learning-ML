from bs4 import BeautifulSoup
import re
import os
import sys
import requests
import pandas as pd
from datetime import date
import copy


class Webscraper:

    def __init__(self, websites):
        self.news_websites = websites
        self.news_data = {'apnews': None, 'reuters': None, 'washingtonpost': None, 'nytimes': None}
        self.news_article_titles = {}
        self.news_article_topics = {}
        self.df = None
        self.scrape_articles()
        self.clean_article_titles()
        self.create_df()
        self.save_df_as_csv()

    def scrape_articles(self):
        # Grab the date here too using beautiful soup.

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

    def clean_article_titles(self):
        for news_org in self.news_websites:

            if 'apnews' in news_org:
                # if its ap, we know ap delimits by '/'. no categories other than 'article' which is moot.
                article_list = self.news_data['apnews']
                titles = []

                # now that we have a list of strings, we can split them
                for article in article_list:
                    list_of_words = article.split("/")
                    title = list_of_words[-1]
                    titles.append(title)
                self.news_article_titles['apnews'] = titles

            elif 'reuters' in news_org:
                # if its reuters we know there are is a cat and subcat,
                # ex. /world/americas/canadian-police-refuse-provincial-order-make-random-stops-amid-covid-19-surge-2021-04-17/
                # ex. https://www.reuters.com/lifestyle/science/like-godzilla-actually-real-study-shows-t-rex-numbered-25-billion-2021-04-15/

                # well, we know that the date is always last, then title, then subcat, then cat.

                article_list = self.news_data['reuters']
                topics = []
                titles = []
                for article in article_list:
                    list_of_words = article.split('/')
                    cat_and_subcat_topics = (list_of_words[-3], list_of_words[-2])
                    topics.append(cat_and_subcat_topics)
                    titles.append(list_of_words[-1])
                self.news_article_titles['reuters'] = titles
                self.news_article_topics['reuters'] = topics

    def create_df(self):
        # pandas can create a dataframe from a LIST OF DICTS
        #link_df = pd.DataFrame.from_dict(self.news_data, orient='index')
        titles_df = pd.DataFrame.from_dict(self.news_article_titles, orient='index')
        #topics_titles_df = pd.DataFrame.from_dict(self.news_article_topics, orient='index')

        self.df = titles_df

        today = date.today()

    def save_df_as_csv(self):
        self.df.to_csv('articles')
