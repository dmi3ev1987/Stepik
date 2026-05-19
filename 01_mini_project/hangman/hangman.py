from random import choice


WORD_LIST = [
    'год',
    'человек',
    'время',
    'дело',
    'жизнь',
    'день',
    'рука',
    'раз',
    'работа',
    'слово',
    'место',
    'лицо',
    'друг',
    'глаз',
]


def get_word():
    return choice(WORD_LIST)


# функция получения текущего состояния
def display_hangman(tries):
    stages = [
        # финальное состояние: голова, торс, обе руки, обе ноги
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """,
        # голова, торс, обе руки, одна нога
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """,
        # голова, торс, обе руки
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        """,
        # голова, торс и одна рука
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,
        # голова и торс
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,
        # голова
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,
        # начальное состояние
        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """,
    ]
    return stages[tries]


def play(word):
    word = word.upper()

    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    count = 0
    print('Давайте играть в угадайку слов!')

    while not guessed:
        print()
        print(display_hangman(tries))
        print(f'Осталось {tries} попыток.')
        print(word_completion)
        print('Отгодайте букву или слово целиком:', end='')
        guess = input().upper()
        if not guess.isalpha():
            print('Нужно вводить только буквы или слово целиком.')
            continue
        if len(guess) == 1:
            if guess in guessed_letters:
                print('Вы уже вводили данную буква, попробуйте ещё раз.')
                continue
            guessed_letters.append(guess)
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        word_completion = (
                            word_completion[:i]
                            + guess
                            + word_completion[i + 1 :]
                        )
                if word_completion == word:
                    guessed = True
            else:
                tries -= 1
        else:
            if guess in guessed_words:
                print('Вы уже вводили данное слово, попробуйте ещё раз.')
                continue
            guessed_words.append(guess)
            if guess == word:
                guessed = True
            else:
                tries -= 1

        count += 1
        if tries == 0:
            print('Вы проиграли=(')
            break

    if guessed:
        print(f'Ура! Вы угадали слово с {count} попытки!')


def play_again():
    if input('Чтобы сыграть еще раз введити "да":').lower() == 'да':
        main()
    print('Спасибо за игру, пока пока=)')


def main():
    play(get_word())
    play_again()


if __name__ == '__main__':
    main()
