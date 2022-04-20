import pyowm
from pyowm.utils.config import get_default_config
import requests
from bs4 import BeautifulSoup


def news_weather(message):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = pyowm.OWM('3797200c7bbaabbc49357e9321f0a021', config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = f"В городе {message.text} сейчас {w.detailed_status}\n"
    answer += "Температура в районе " + str(round(temp)) + " градусов"

    return answer


def news_russian_to_day():
    url = 'https://newsapi.org/v2/top-headlines?country=ru&apiKey=a6e2efa325634852b598a4a3e04fddcb'
    soup = requests.get(url).json()

    s1 = {}
    for key in soup.get('articles')[:5]:
        s1.setdefault(key.get('title'), key.get('url'))

    return s1


def news_game_to_day():
    url = 'https://www.igromania.ru/news/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    news = soup.find_all('a', class_='aubli_name')

    s1 = {}
    for link in news[:5]:
        s1.setdefault(link.text, 'https://www.igromania.ru' + link['href'][:-5])

    return s1
