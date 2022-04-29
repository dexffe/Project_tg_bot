from flask import Flask
from db_news import db_session
import requests
from db_news.create_tables import RussianNews, GameNews
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def database():
    db_session.global_init("db_news/blogs.db")
    url = 'https://newsapi.org/v2/top-headlines?country=ru&apiKey=a6e2efa325634852b598a4a3e04fddcb'
    soup = requests.get(url).json()
    for key in soup.get('articles'):
        rus = RussianNews()
        rus.content = key.get('title')
        rus.url = key.get('url')
        db_sess = db_session.create_session()
        db_sess.add(rus)
        db_sess.commit()

    url = 'https://www.igromania.ru/news/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all('a', class_='aubli_name')
    for link in news:
        game = GameNews()
        game.content = link.text
        game.url = 'https://www.igromania.ru' + link['href'][:-5]
        db_sess = db_session.create_session()
        db_sess.add(game)
        db_sess.commit()
