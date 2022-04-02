from deep_translator import GoogleTranslator


def translate_text(text, target):
    return GoogleTranslator(source='auto', target=target).translate(text)


def translate_emoticons(text):
    return GoogleTranslator(source='auto', target='en').translate(text)


def translate_crypto(text):
    return GoogleTranslator(source='auto', target='en').translate(text)