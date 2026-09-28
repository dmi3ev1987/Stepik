import turtle as t
from random import randint


t.hideturtle()
t.speed(10)
t.tracer(0)


def draw_triangle(size):
    angle = 120
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.right(angle)
    t.penup()
    t.forward(size)
    t.left(60)


def draw_star():
    side = randint(5, 10)
    t.setheading(randint(0, 180))
    color = '#{:02x}{:02x}{:02x}'.format(
        randint(0, 255), randint(0, 255), randint(0, 255)
    )
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(6):
        draw_triangle(side)
    t.end_fill()
    t.update()


for _ in range(500):
    t.penup()
    t.goto(randint(-250, 250), randint(-200, 200))
    draw_star()
