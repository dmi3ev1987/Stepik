def set_param():
    while True:
        direction = input(
            'Выберите направление: (ш = ширование, д = дешифрование)\n'
        )
        if direction == 'ш':
            direction = 1
            break
        elif direction == 'д':
            direction = -1
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


def cipher(direction, alphabet, step, text):
    result = ''
    step *= direction
    if alphabet == 32:
        lower_letter = ord('а')
        upper_letter = ord('А')
    else:
        lower_letter = ord('a')
        upper_letter = ord('A')
    for char in text:
        if char.isalpha():
            if char.islower():
                start_letter = lower_letter
            else:
                start_letter = upper_letter
            result += chr(
                (ord(char) + step - start_letter) % alphabet + start_letter
            )
        else:
            result += char
    return result


def main(text):
    direction, alphabet, step = set_param()
    print(cipher(direction, alphabet, step, text))


text = 'Блажен, кто верует, тепло ему на свете!'

main(text)
