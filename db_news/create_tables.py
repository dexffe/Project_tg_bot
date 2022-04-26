import sqlalchemy
from db_news.db_session import SqlAlchemyBase


class RussianNews(SqlAlchemyBase):
    __tablename__ = 'Russian_news'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.Text)
    url = sqlalchemy.Column(sqlalchemy.Text)


class GameNews(SqlAlchemyBase):
    __tablename__ = 'Game_news'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.Text)
    url = sqlalchemy.Column(sqlalchemy.Text)