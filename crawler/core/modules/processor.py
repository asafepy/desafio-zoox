import argparse
import concurrent.futures
import json
import re
from multiprocessing import Process

from core.db.database import get_engine_db
from core.db.news import News_db
from core.utils.parser import Parser
from core.utils.validation import validate_url
from core.modules.crawler import Crawler

__author__ = 'asafe'


class Processor(object):
    _test = False

    @classmethod
    def get_urls(self):
        news_db = News_db(get_engine_db(self._test))
        news = news_db.get_news_for_status('WAIT')
        return news

    @classmethod
    def parser_and_update(self, key, url):
        content = Parser(url)
        News_db(get_engine_db(self._test)).update_news(
            key, content.get_title(), content.get_description(), 'PROCESSED'
        )

    @classmethod
    def run_processor(self):

        processes = []

        for news in self.get_urls():
            if validate_url(news.url):
                process = Process(target=self.parser_and_update,
                                  args=(news.id, news.url))
                processes.append(process)

        for p in processes:
            p.start()

        for p in processes:
            p.join()


if __name__ == "__main__":

    Processor.run_processor()
