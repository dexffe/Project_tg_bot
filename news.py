import pyowm
from pyowm.utils.config import get_default_config


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
