from random import randint


def get_number_to_guess(number):
    return randint(1, number)


def is_valid(number_to_check, max_number):
    if not number_to_check.isdigit():
        return False
    elif int(number_to_check) < 1 or int(number_to_check) > max_number:
        return False
    return True


def get_max_number_to_guess():
    print('Задайте максимальную гарницу случайного числа')
    input_string = input()
    if input_string.isdigit():
        return int(input_string)
    else:
        print('Необходимо ввести число, а не тескт')
        get_max_number_to_guess()


def game(number_to_guess, max_number):
    print('Добро пожаловать в числовую угадайку')
    print(f'Введите целое число от 1 до {max_number}')
    count_try = 0
    while True:
        user_number = input()
        count_try += 1
        if not is_valid(user_number, max_number):
            print(f'А  может быть все-таки введем целое число от 1 до {max_number}?')
            continue
        user_number = int(user_number)
        if user_number < number_to_guess:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > number_to_guess:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали число {number_to_guess} за {count_try} попыток, поздравляем!')
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    play_again()


def play_again():
    print('Чтобы сыграть еще раз введите "да"')
    if input().lower() == 'да':
        main()
    else:
        print('Ждем вас снова.')


def main():
    max_number = get_max_number_to_guess()
    number_to_guess = get_number_to_guess(max_number)
    game(number_to_guess, max_number)

main()
