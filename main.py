import os
import telebot
import random_generator
import interpreter_translate

bot = telebot.TeleBot("5264924778:AAEyAQFfkdpGbMq-vdL6xP0KYgX0aWqxTwg")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard0 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/generator', '/interpreter', '/news', '/image')
keyboard2.row('/info', '/money', '/number', '/l_p')
keyboard3.row('/info', '/translation', '/emoticons', '/crypto')
keyboard4.row('/info', '/Russian', '/English', '/French')
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


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == '/generator':
        bot.send_message(message.from_user.id, '"/money" - орёл/решка' + '\n' + '\n' +
                         '"/number" - число в заданном промежутке' + '\n' + '\n' +
                         '"/l_p" - логин и пароль', reply_markup=keyboard2)
    elif message.text == '/interpreter':
        bot.send_message(message.from_user.id, '"/translation" - перевод текста' + '\n' + '\n' +
                         '"/emoticons" - перевести текст в смайлики' + '\n' + '\n' +
                         '"/crypto" - перевод валюты в криптовалюту', reply_markup=keyboard3)
    elif message.text == '/news':
        bot.send_message(message.from_user.id, 'news')
    elif message.text == '/image':
        bot.send_message(message.from_user.id, 'image')
    try:
        generator(message)
        translate(message)
        news(message)
        image(message)
    except Exception:
        pass


def translate(message):
    if message.text == '/translation':
        bot.send_message(message.from_user.id, 'Введите текст:')
        bot.register_next_step_handler(message, transl)
    elif message.text == '/emoticons':
        bot.send_message(message.from_user.id, interpreter_translate.translate_emoticons(message))
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
    bot.send_message(message.from_user.id, 'lox')


bot.polling()