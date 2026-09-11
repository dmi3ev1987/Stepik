import turtle as t
from random import randint, choice


t.speed(0)
t.Screen().bgcolor('cyan')
t.hideturtle()

colors = [
    'red',
    'blue',
    'yellow',
    'green',
    'purple',
    'orange',
    'pink',
    'brown',
    'gold',
    'gray',
    'black',
    'violet',
    'lime',
    'navy',
    'magenta',
    'coral',
    'salmon',
    'turquoise',
    'olive',
    'teal',
]


def snowflake(size, color, position=(210, 150)):
    t.penup()
    t.goto(position)
    t.pencolor(color)
    t.pendown()
    for _ in range(8):
        for _ in range(3):
            t.forward(size)
            t.right(45)
            t.forward(size)
            t.backward(size)
            t.left(90)
            t.forward(size)
            t.backward(size)
            t.right(45)
        t.forward(size)
        t.backward(size * 4)
        t.left(45)
    t.penup()


for _ in range(randint(50, 55)):
    position = randint(-210, 210), randint(-150, 150)
    snowflake(randint(3, 10), choice(colors), position)
