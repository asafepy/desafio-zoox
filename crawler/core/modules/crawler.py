import re
import requests
import concurrent.futures

from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from crawler.core.db.database import get_engine_db
from crawler.core.db.model import News


__author__ = 'asafe'


class Crawler(object):

    def __init__(self, urls, workers=3):
        self.urls = urls
        self.workers = workers
        self.session = requests.Session()

    def conn_url(self, url):
        return self.session.get(url)

    @staticmethod
    def get_content(page):
        return BeautifulSoup(page, "html.parser")

    @staticmethod
    def get_links(page):
        return page.find_all('a', href=re.compile("^https://www.oantagonista.com/brasil"))

    @staticmethod
    def save_on_db(links, db):
        for link in links:
            url = link.get('href')
            news = db.query(News).filter_by(url=url)
            if len(list(news)) == 1:
                continue

            news = News(url=link.get('href'))
            db.add(news)
            db.commit()

    def run(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
            db = Session(bind=get_engine_db())
            future_to_url = {executor.submit(self.conn_url, url): url for url in self.urls}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    page = future.result()
                    links = self.get_links(self.get_content(page.content))
                    self.save_on_db(links, db)
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))


if __name__ == '__main__':
    
    urls = ['https://www.oantagonista.com/']
    crawler = Crawler(urls)
    crawler.run()

