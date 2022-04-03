from deep_translator import GoogleTranslator


def translate_text(text, target):
    return GoogleTranslator(source='auto', target=target).translate(text)


# def translate_base(num, to_base=10, from_base=10):
def translate_base(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]

# Number = input()
# Basein = int(input())
# Baseout = int(input())
#
# # перевод из исходной в "10"
# a = int(Number, Basein)
# # перевод из "10" в заданную
# a = translate_base(a, Baseout)
#
# print(a)


def translate_crypto(text):
    return GoogleTranslator(source='auto', target='en').translate(text)