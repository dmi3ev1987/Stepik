def set_param():
    while True:
        direction = input(
            'Выберите направление: (ш = ширование, д = дешифрование)\n'
        )
        if direction == 'ш':
            direction = True
            break
        elif direction == 'д':
            direction = False
            break
        else:
            print('Разрешенные ответы только "ш" или "д".')
    while True:
        alphabet = input('Выберите алфавит: (р = русский, а = английский)\n')
        if alphabet == 'р':
            alphabet = 32
            break
        elif alphabet == 'а':
            alphabet = 26
            break
        else:
            print('Разрешенные ответы только "р" или "а".')
    while True:
        step = input('Шаг сдвига вправо (натуральное число)\n')
        if step.isdigit():
            step = int(step)
            break
        else:
            print('Введите натуральное число.')

    return direction, alphabet, step


def main():
    print(set_param())


main()
