import os
from news import news_weather
import telebot
import random_generator
import interpreter_translate
from update_image import revers

bot = telebot.TeleBot("5264924778:AAEyAQFfkdpGbMq-vdL6xP0KYgX0aWqxTwg")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard6 = telebot.types.ReplyKeyboardMarkup(True)
keyboard0 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/generator', '/interpreter', '/news', '/image')
keyboard2.row('/info', '/money', '/number', '/l_p')
keyboard3.row('/info', '/translation', '/num_sys', '/crypto')
keyboard4.row('/info', '/Russian', '/English', '/French')
keyboard5.row('/info', '/#####', '/#####', '/weather')
keyboard6.row('/info', '/turn', '/invers', '/bl_wht')
keyboard0.row('/info')


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


@bot.message_handler(content_types=['photo'])
def img_return(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'files/' + file_info.file_path
    with open(src, 'wb') as new_file:
        mes = new_file.write(downloaded_file)

    bot.send_photo(message.from_user.id, revers(mes))
    if os.path.isfile("file_0.jpg"):
        os.remove("file_0.jpg")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == '/generator':
        bot.send_message(message.from_user.id, '"/money" - орёл/решка' + '\n' + '\n' +
                         '"/number" - число в заданном промежутке' + '\n' + '\n' +
                         '"/l_p" - логин и пароль', reply_markup=keyboard2)
    elif message.text == '/interpreter':
        bot.send_message(message.from_user.id, '"/translation" - перевод текста' + '\n' + '\n' +
                         '"/num_sys" - перевод чисел в разные системы счисления' + '\n' + '\n' +
                         '"/crypto" - перевод валюты в криптовалюту', reply_markup=keyboard3)
    elif message.text == '/news':
        bot.send_message(message.from_user.id, '"/######" - о главном в России за сутки' + '\n' + '\n' +
                         '"/######" - важные события из игровой индустрии' + '\n' + '\n' +
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
    except Exception:
        pass


def image(message):
    if message.text == '/turn':
        bot.send_message(message.from_user.id, 'Отправте фото:')
        bot.register_next_step_handler(message, img_turn)
    elif message.text == '/invers':
        bot.send_message(message.from_user.id, 'Отправте фото:')
        bot.register_next_step_handler(message, img_inver)
    elif message.text == '/bl_wht':
        bot.send_message(message.from_user.id, 'Отправте фото:')
        bot.register_next_step_handler(message, img_blwht)


def news(message):
    if message.text == '/########':
        pass
    elif message.text == '/#########':
        pass
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
    elif message.text == '/crypto':
        bot.send_message(message.from_user.id, interpreter_translate.translate_crypto(message))
    try:
        tran(message)
    except Exception:
        pass


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
    if message.text == '/Russian':
        bot.send_message(message.from_user.id, interpreter_translate.translate_text(text, 'ru'))
    elif message.text == '/English':
        bot.send_message(message.from_user.id, interpreter_translate.translate_text(text, 'en'))
    elif message.text == '/French':
        bot.send_message(message.from_user.id, interpreter_translate.translate_text(text, 'fr'))


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
    bot.send_message(message.from_user.id, 'Введите число:')
    bot.register_next_step_handler(message, numersys)


@bot.message_handler(func=lambda message: True)
def generator(message):
    if message.text == '/money':
        bot.send_message(message.from_user.id, random_generator.generator_money())
    elif message.text == '/number':
        bot.send_message(message.from_user.id, 'Введите 2 числа через пробел:')
        bot.register_next_step_handler(message, num)
    elif message.text == '/l_p':
        bot.send_message(message.from_user.id, random_generator.generator_login_password())


def num(message):
    a = int(message.text.split()[0])
    b = int(message.text.split()[1])
    bot.send_message(message.from_user.id, random_generator.generator_numbers(a, b))


def reg_text(message):
    bot.send_message(message.from_user.id, 'Artemi')


bot.polling()