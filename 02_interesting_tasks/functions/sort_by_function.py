athletes = [
    ('Дима', 10, 130, 35),
    ('Тимур', 11, 135, 39),
    ('Руслан', 9, 140, 33),
    ('Рустам', 10, 128, 30),
    ('Амир', 16, 170, 70),
    ('Рома', 16, 188, 100),
    ('Матвей', 17, 168, 68),
    ('Петя', 15, 190, 90),
]


def name(seq):
    return seq[0]


def age(seq):
    return seq[1]


def height(seq):
    return seq[2]


def weight(seq):
    return seq[3]


settings = {1: name, 2: age, 3: height, 4: weight}

athletes.sort(key=settings[int(input())])

for athlet in athletes:
    print(*athlet)
