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
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)



def main():
    word = get_word()
    play(word)


if __name__ == '__main__':
    main()
