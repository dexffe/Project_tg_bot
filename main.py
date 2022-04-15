import os
from news import news_weather, news_russian_to_day, news_game_to_day
import telebot
import random_generator
from update_image import image_inversion, image_invert, image_blwht
import interpreter_translate

bot = telebot.TeleBot("5264924778:AAEyAQFfkdpGbMq-vdL6xP0KYgX0aWqxTwg")
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard5 = telebot.types.ReplyKeyboardMarkup()
keyboard6 = telebot.types.ReplyKeyboardMarkup()
keyboard7 = telebot.types.ReplyKeyboardMarkup()
keyboard0 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add('/generator', '/interpreter', '/news', '/image')
keyboard2.add('/money', '/number', '/login_password', '/info')
keyboard3.add('/translation', '/num_sys', '/cash', '/info')
keyboard4.add('/Russian', '/English', '/French', '/info')
keyboard5.add('/game_news', '/russian_news', '/weather', '/info')
keyboard6.add('/turn', '/invers', '/bl_wht', '/info')
keyboard7.add('/usd', '/eur', '/cny', '/info')
keyboard0.add('/info')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Привет! Что-бы узнать возможности бота воспользуйтесь командой /info",
                     reply_markup=keyboard0)


@bot.message_handler(commands=['info'])
def send_welcome(message):
    if os.path.isfile("translate_text.txt"):
        os.remove("translate_text.txt")
    bot.send_message(message.from_user.id, "Чем интересуетесь?")
    bot.send_message(message.from_user.id, '"/generator" - рандомная генерация' + '\n' +
                     '"/interpreter" - перевод' + '\n' +
                     '"/news" - новости' + '\n' +
                     '"/image" - работа с картинкой', reply_markup=keyboard1)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == '/generator':
        bot.send_message(message.from_user.id, '"/money" - орёл/решка' + '\n' + '\n' +
                         '"/number" - число в заданном промежутке' + '\n' + '\n' +
                         '"/login_password" - логин и пароль', reply_markup=keyboard2)
    elif message.text == '/interpreter':
        bot.send_message(message.from_user.id, '"/translation" - перевод текста' + '\n' + '\n' +
                         '"/num_sys" - перевод чисел в разные системы счисления' + '\n' + '\n' +
                         '"/cash" - перевод рублей в иностранную валюту', reply_markup=keyboard3)
    elif message.text == '/news':
        bot.send_message(message.from_user.id, '"/russian_news" - о главном в России за сутки' + '\n' + '\n' +
                         '"/game_news" - важные события из игровой индустрии' + '\n' + '\n' +
                         '"/weather" - погода', reply_markup=keyboard5)
    elif message.text == '/image':
        bot.send_message(message.from_user.id, '"/turn" - повернуть картинку на 90' + '\n' + '\n' +
                         '"/invers" - инверсия цвета картинки' + '\n' + '\n' +
                         '"/bl_wht" - перекрашивание картинки в черно-белый', reply_markup=keyboard6)
    try:
        generator(message)
        translate(message)
        news(message)
        image(message)
    except Exception as q:
        print(q)


def image(message):
    if message.text == '/turn':
        bot.send_message(message.from_user.id, 'Отправте фото:')
        bot.register_next_step_handler(message, img_return)
    elif message.text == '/inversion':
        bot.send_message(message.from_user.id, 'Отправте фото:')
        bot.register_next_step_handler(message, img_inver)
    elif message.text == '/bl_wht':
        bot.send_message(message.from_user.id, 'Отправте фото:')
        bot.register_next_step_handler(message, img_blwht)


def img_return(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("file_0.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_photo(message.from_user.id, image_inversion('file_0.jpg'))
    if os.path.isfile("file_0.jpg"):
        os.remove("file_0.jpg")
        os.remove("file_1.jpg")


def img_inver(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("file_0.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_photo(message.from_user.id, image_invert('file_0.jpg'))
    if os.path.isfile("file_0.jpg"):
        os.remove("file_0.jpg")
        os.remove("file_1.jpg")


def img_blwht(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("file_0.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_photo(message.from_user.id, image_blwht('file_0.jpg'))
    if os.path.isfile("file_0.jpg"):
        os.remove("file_0.jpg")
        os.remove("file_1.jpg")


def news(message):
    if message.text == '/game_news':
        for key, value in news_game_to_day().items():
            bot.send_message(message.from_user.id, f'{key}\nПодробнее: {value}')
    elif message.text == '/russian_news':
        for key, value in news_russian_to_day().items():
            bot.send_message(message.from_user.id, f'{key}\nПодробнее: {value}')
    elif message.text == '/weather':
        bot.send_message(message.from_user.id, 'Введите город в котором хотите узнать погоду:')
        bot.register_next_step_handler(message, city)


def city(message):
    bot.send_message(message.from_user.id, news_weather(message))


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
    try:
        tran(message)
        cash2(message)
    except Exception as q:
        print(q)


def cash(message):
    with open('translate_cash.txt', 'w', encoding='utf-8') as q:
        q.write(message.text)
    bot.send_message(message.from_user.id, "В какую волюту перевести?")
    bot.send_message(message.from_user.id, '"/usd" - Доллор' + '\n' + '\n' +
                                           '"/eur" - Евро' + '\n' + '\n' +
                                           '"/cny" - Юань', reply_markup=keyboard7)


def cash2(message):
    with open('translate_cash.txt', encoding='utf-8') as q:
        txt = int(q.read())
    voluts = ['/usd', '/eur', '/cny']
    if message.text in voluts:
        bot.send_message(message.from_user.id, interpreter_translate.translate_cash(txt, message.text[1:]))


def transl(message):
    with open('translate_text.txt', 'w', encoding='utf-8') as q:
        q.write(message.text)
    bot.send_message(message.from_user.id, "На какой язык перевести?")
    bot.send_message(message.from_user.id, '"/Russian" - русский язык' + '\n' + '\n' +
                                           '"/English" - английский язык' + '\n' + '\n' +
                                           '"/French" - французский язык', reply_markup=keyboard4)


def tran(message):
    with open('translate_text.txt', encoding='utf-8') as q:
        text = q.read()
    leng = {'/Russian': 'ru',
            '/English': 'en',
            '/French': 'fr'}
    if message.text in leng.keys():
        bot.send_message(message.from_user.id, interpreter_translate.translate_text(text, leng[message.text]))


def numersys(message):
    with open('translate_numb.txt', 'w', encoding='utf-8') as q:
        q.write(message.text)
    bot.send_message(message.from_user.id, "Из какой системы счисления в какую перевести?" + '\n' +
                     "Напишите 2 числа через пробел.")
    bot.register_next_step_handler(message, numer_sys)


def numer_sys(message):
    with open('translate_numb.txt', encoding='utf-8') as q:
        number = q.read()
    from_base = int(message.text.split()[0])
    to_base = int(message.text.split()[1])
    try:
        a = int(number, from_base)
    except Exception:
        a = number
    bot.send_message(message.from_user.id, interpreter_translate.translate_base(a, to_base))


@bot.message_handler(func=lambda message: True)
def generator(message):
    if message.text == '/money':
        bot.send_message(message.from_user.id, random_generator.generator_money())
    elif message.text == '/number':
        bot.send_message(message.from_user.id, 'Введите 2 числа через пробел:')
        bot.register_next_step_handler(message, num)
    elif message.text == '/login_password':
        bot.send_message(message.from_user.id, random_generator.generator_login_password())


def num(message):
    a = int(message.text.split()[0])
    b = int(message.text.split()[1])
    bot.send_message(message.from_user.id, random_generator.generator_numbers(a, b))


def reg_text(message):
    bot.send_message(message.from_user.id, 'Artemi')


bot.polling()