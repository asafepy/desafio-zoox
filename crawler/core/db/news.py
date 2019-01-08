from sqlalchemy.orm import Session

from crawler.core.db.model import News

__author__ = 'asafe'


class News_db(object):

    __instance = None
    _db = None

    def __init__(self, engine):
        self._db = Session(bind=engine)

    def get_news_for_status(self, status):
        return self._db.query(News).filter_by(status=status)

    def update_status_news(self, keys, status):
        list_news = self._db.query(News).filter(News.id.in_(keys))
        for news in list_news:
            news.status = status
            self._db.add(news)

        self._db.commit()

    def update_news(self, key, title, description, status):
        news = self._db.query(News).get(key)
        news.title = title
        news.description = description
        news.status = status
        self._db.add(news)
        self._db.commit()
