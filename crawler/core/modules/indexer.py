import csv

from config.config_file import appconfig
from crawler.core.db.database import get_engine_db
from crawler.core.utils.file_util import create_file
from crawler.core.db.news import News_db


__author__ = 'asafe'


class Indexer(object):
    _test = False

    @classmethod
    def export_data_to_csv(cls, file_name, list_news):

        header = ['url', 'título', 'descrição']
        create_file(file_name, header)
        keys = []
        with open(file_name, 'a') as csvfile:
            for news in list_news:
                spam = csv.writer(csvfile, delimiter=',')
                spam.writerow([news.url, news.title, news.description])
                keys.append(news.id)

        News_db(get_engine_db(cls._test)).update_status_news(keys, 'INDEXED')


if __name__ == '__main__':

    news_db = News_db(get_engine_db())
    news = news_db.get_news_for_status('PROCESSED')
    Indexer.export_data_to_csv(appconfig['local_file_name'], news)
