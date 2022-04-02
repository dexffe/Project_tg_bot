from deep_translator import GoogleTranslator


def translate_text(text, target):
    return GoogleTranslator(source='auto', target=target).translate(text)


def translate_base(num, from_base=10, to_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return translate_base(n // to_base, to_base) + alphabet[n % to_base]


def translate_crypto(text):
    return GoogleTranslator(source='auto', target='en').translate(text)