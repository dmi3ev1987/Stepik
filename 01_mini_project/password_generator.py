import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
uncommon_chars = 'il1Lo0O'


def get_password_lenght():
    return int(input('Введите длину пароля:'))


def get_password_qyantity():
    return int(input('Введите количество паролей для генерации:'))


def allowed_chars():
    chars = ''
    print('Задайте символы из которых будет состоять пароль.')
    print('Отвечайте "да" если хотите использовать предложенные символы.')

    if input('Включать ли цифры 0123456789?\n').lower() == 'да':
        chars += digits
    if (
        input(
            'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n'
        ).lower()
        == 'да'
    ):
        chars += uppercase_letters
    if (
        input(
            'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?\n'
        ).lower()
        == 'да'
    ):
        chars += lowercase_letters
    if input('Включать ли символы !#$%&*+-=?@^_?\n').lower() == 'да':
        chars += punctuation
    if input('Исключать ли неоднозначные символы il1Lo0O?\n').lower() == 'да':
        for char in 'il1Lo0O':
            chars = chars.replace(char, '')
    return chars


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


def main():
    quantity = get_password_qyantity()
    length = get_password_lenght()
    chars = allowed_chars()
    for _ in range(quantity):
        print(generate_password(length, chars))


main()
