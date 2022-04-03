from deep_translator import GoogleTranslator


def translate_text(text, target):
    return GoogleTranslator(source='auto', target=target).translate(text)


def translate_base(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]


def translate_crypto(text):
    return GoogleTranslator(source='auto', target='en').translate(text)