import os
from news import news_weather, news_russian_and_game
import telebot
import random_generator
from update_image import image_inversion_invert_blwht
import interpreter_translate

bot = telebot.TeleBot("5264924778:AAEyAQFfkdpGbMq-vdL6xP0KYgX0aWqxTwg")
functions = [['/generator', '/interpreter', '/news', '/image'],
             ['/money', '/number', '/login_password'],
             ['/translation', '/num_sys', '/cash'],
             ['/Russian', '/English', '/French'],
             ['/game_news', '/russian_news', '/weather'],
             ['/turn', '/inversion', '/bl_wht'],
             ['/usd', '/eur', '/cny'],
             ['/info']]

keyboard0 = telebot.types.ReplyKeyboardMarkup().add(*functions[7])
keyboard1 = telebot.types.ReplyKeyboardMarkup().add(*functions[0])
keyboard2 = telebot.types.ReplyKeyboardMarkup().add(*functions[1], '/info')
keyboard3 = telebot.types.ReplyKeyboardMarkup().add(*functions[2], '/info')
keyboard4 = telebot.types.ReplyKeyboardMarkup().add(*functions[3], '/info')
keyboard5 = telebot.types.ReplyKeyboardMarkup().add(*functions[4], '/info')
keyboard6 = telebot.types.ReplyKeyboardMarkup().add(*functions[5], '/info')
keyboard7 = telebot.types.ReplyKeyboardMarkup().add(*functions[6], '/info')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Привет! Что-бы узнать возможности бота воспользуйтесь командой /info",
                     reply_markup=keyboard0)


@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Чем интересуетесь?")
    bot.send_message(message.from_user.id, '"/generator" - рандомная генерация' + '\n' +
                                           '"/interpreter" - перевод' + '\n' +
                                           '"/news" - новости' + '\n' +
                                           '"/image" - работа с картинкой',
                     reply_markup=keyboard1)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == '/generator':
        bot.send_message(message.from_user.id, '"/money" - орёл/решка' + '\n' + '\n' +
                                               '"/number" - число в заданном промежутке' + '\n' + '\n' +
                                               '"/login_password" - логин и пароль',
                         reply_markup=keyboard2)

    elif message.text == '/interpreter':
        bot.send_message(message.from_user.id, '"/translation" - перевод текста' + '\n' + '\n' +
                                               '"/num_sys" - перевод чисел в разные системы счисления' + '\n' + '\n' +
                                               '"/cash" - перевод рублей в иностранную валюту',
                         reply_markup=keyboard3)

    elif message.text == '/news':
        bot.send_message(message.from_user.id, '"/russian_news" - о главном в России за сутки' + '\n' + '\n' +
                                               '"/game_news" - важные события из игровой индустрии' + '\n' + '\n' +
                                               '"/weather" - погода',
                         reply_markup=keyboard5)

    elif message.text == '/image':
        bot.send_message(message.from_user.id, '"/turn" - повернуть картинку на 90' + '\n' + '\n' +
                                               '"/inversion" - инверсия цвета картинки' + '\n' + '\n' +
                                               '"/bl_wht" - перекрашивание картинки в черно-белый',
                         reply_markup=keyboard6)

    if message.text not in [j for i in functions for j in i]:
        bot.send_message(message.from_user.id, 'что?')

    try:
        generator(message)
        translate(message)
        news(message)
        image(message)
    except TypeError as q:
        print(q)


def image(message):
    if message.text in functions[5]:
        with open("img_type.txt", 'w') as img_type:
            img_type.write(message.text[1:])
        bot.send_message(message.from_user.id, 'Отправте фото:')
        bot.register_next_step_handler(message, image_2)


def image_2(message):
    try:
        with open('img_type.txt', encoding='utf-8') as q:
            img_type = q.read()
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("file_0.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_photo(message.from_user.id, image_inversion_invert_blwht('file_0.jpg', img_type))
        if os.path.isfile("file_0.jpg"):
            os.remove("file_0.jpg")
            os.remove("file_1.jpg")
            os.remove("img_type.txt")
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def number_news(message):
    try:
        with open('name_news.txt', encoding='utf-8') as q:
            name_table = q.read()
        if message.text is not None and 0 <= int(message.text) <= len(news_russian_and_game(name_table).keys()):
            message.text = int(message.text)
            for key, value in news_russian_and_game(name_table, message.text).items():
                bot.send_message(message.from_user.id, f'{key}\nПодробнее: {value}')
        else:
            bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def news(message):
    list_names = {
                  '/game_news': 'Game_news',
                  '/russian_news': 'Russian_news'
                 }
    if message.text in list_names:
        bot.send_message(message.from_user.id,
                         f'У нас имеется {len(news_russian_and_game(list_names[message.text]).keys())} новостей')
        bot.send_message(message.from_user.id, 'Введите число, сколько хотите получить новостей:')

        with open("name_news.txt", 'w') as name:
            name.write(list_names[message.text])

        bot.register_next_step_handler(message, number_news)

    elif message.text == '/weather':
        bot.send_message(message.from_user.id, 'Введите город в котором хотите узнать погоду:')
        bot.register_next_step_handler(message, city)


def city(message):
    try:
        count = 0
        for i in list(message.text):
            if i in '1234567890':
                count = 1

        if count != 1:
            bot.send_message(message.from_user.id, news_weather(message))
        else:
            bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')

    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def translate(message):
    if message.text == '/translation':
        bot.send_message(message.from_user.id, 'Введите текст:')
        bot.register_next_step_handler(message, transl)

    elif message.text == '/num_sys':
        bot.send_message(message.from_user.id, 'Введите число:')
        bot.register_next_step_handler(message, numersys)

    elif message.text == '/cash':
        bot.send_message(message.from_user.id, 'Введите сумму в рублях:')
        bot.register_next_step_handler(message, cash)


def cash(message):
    try:
        int(message.text)

        with open('translate_cash.txt', 'w', encoding='utf-8') as q:
            q.write(message.text)

        bot.send_message(message.from_user.id, "В какую волюту перевести?")
        bot.send_message(message.from_user.id, '"/usd" - Доллор' + '\n' + '\n' +
                                               '"/eur" - Евро' + '\n' + '\n' +
                                               '"/cny" - Юань',
                         reply_markup=keyboard7)
        bot.register_next_step_handler(message, cash2)
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def cash2(message):
    with open('translate_cash.txt', encoding='utf-8') as q:
        txt = int(q.read())
    if message.text in functions[6]:
        bot.send_message(message.from_user.id, interpreter_translate.translate_cash(txt, message.text[1:]))
    os.remove("translate_cash.txt")


def transl(message):
    try:
        with open('translate_text.txt', 'w', encoding='utf-8') as q:
            q.write(message.text)

        bot.send_message(message.from_user.id, "На какой язык перевести?")
        bot.send_message(message.from_user.id, '"/Russian" - русский язык' + '\n' + '\n' +
                                               '"/English" - английский язык' + '\n' + '\n' +
                                               '"/French" - французский язык',
                         reply_markup=keyboard4)
        bot.register_next_step_handler(message, tran)
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def tran(message):
    try:
        with open('translate_text.txt', encoding='utf-8') as q:
            text = q.read()
        if message.text in functions[3]:
            bot.send_message(message.from_user.id, interpreter_translate.translate_text(text, message.text[1:3].lower()))
        os.remove("translate_text.txt")
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def numersys(message):
    try:
        int(message.text)
        with open('translate_numb.txt', 'w', encoding='utf-8') as q:
            q.write(message.text)
        bot.send_message(message.from_user.id, "Из какой системы счисления в какую перевести?" + '\n' +
                         "Напишите 2 числа через пробел.")
        bot.register_next_step_handler(message, numer_sys)
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def numer_sys(message):
    try:
        with open('translate_numb.txt', encoding='utf-8') as q:
            number = q.read()
        from_base = int(message.text.split()[0])
        to_base = int(message.text.split()[1])
        try:
            a = int(number, from_base)
        except TypeError:
            a = number
        bot.send_message(message.from_user.id, interpreter_translate.translate_base(a, to_base))
        os.remove("translate_numb.txt")
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


def generator(message):
    if message.text == '/money':
        bot.send_message(message.from_user.id, random_generator.generator_money())
    elif message.text == '/number':
        bot.send_message(message.from_user.id, 'Введите 2 числа через пробел:')
        bot.register_next_step_handler(message, num)
    elif message.text == '/login_password':
        bot.send_message(message.from_user.id, random_generator.generator_login_password())


def num(message):
    try:
        a = int(message.text.split()[0])
        b = int(message.text.split()[1])
        if a > b:
            a, b = b, a
        bot.send_message(message.from_user.id, random_generator.generator_numbers(a, b))
    except TypeError:
        bot.send_message(message.from_user.id, 'Некорректный ввод, давай по новой.')


bot.polling()
