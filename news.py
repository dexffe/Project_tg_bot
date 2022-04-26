import os
import sqlite3

from db_news import database_start, db_session, create_tables
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


def news_russian_and_game(name_table, number=None):
    global sqlite_connection
    try:
        database_start.database()
        if number is not None:
            number = int(number)
        print(name_table)
        sqlite_connection = sqlite3.connect('db_news/blogs.db')
        cursor = sqlite_connection.cursor()
        sql_select_query = f"""select * from {name_table}"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        s1 = {}
        for row in records[:number]:
            s1.setdefault(row[1], row[2])
        sql_delete_query = f"""DELETE from {name_table}"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        cursor.close()
        return s1

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
