from webscraper import Webscraper

def main():
    news_websites = ['https://apnews.com', 'https://www.reuters.com/', 'https://www.washingtonpost.com/', 'https://www.nytimes.com/']
    spoon = Webscraper(news_websites)


if __name__ == '__main__':
    main()