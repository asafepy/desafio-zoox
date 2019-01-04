from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

__author__ = 'asafe'

Base = declarative_base()


STATUS_CHOICES = (
    ('WAIT', 'wait'),
    ('PROCESSED', 'Processed'),
    ('INDEXED', 'Indexed'),
)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String,  nullable=True)
    description = Column(Text,  nullable=True)
    status = Column(ChoiceType(STATUS_CHOICES, impl=String()), default='WAIT')