import random


def generator_numbers(a, b):
    return random.randint(a, b)


def generator_money():
    return random.choice(['Орёл', 'Решка'])


def generator_login_password():
    log = ''
    pas = ''
    for _ in range(random.randint(7, 13)):
        log += random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))
    for _ in range(random.randint(7, 13)):
        pas += random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&$'))
    return '\n'.join(['Логин: ' + log + '@mail.ru', 'Пароль: ' + pas])