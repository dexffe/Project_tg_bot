from deep_translator import GoogleTranslator
from pycbrf import ExchangeRates
from datetime import datetime


def translate_text(text, target):
    return GoogleTranslator(source='auto', target=target).translate(text)


def translate_base(num, base):
    try:
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b = alpha[num % base]
        while num >= base:
            num = num // base
            b += alpha[num % base]
        return b[::-1]
    except Exception:
        return hex(num)


def translate_cash(number, message):
    message_norm = message.strip().lower()
    if message_norm in ['usd', 'eur', 'cny']:
        rates = ExchangeRates(datetime.now())
        num = number / rates[message_norm.upper()].rate
        return round(num, 2)


