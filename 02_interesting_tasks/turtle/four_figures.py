import turtle as t
from random import choice, shuffle
from math import sqrt, tan, radians, ceil


t.speed(0)
t.hideturtle()
colors = ['yellow', 'blue', 'purple', 'orange', 'red']
sides = [3, 4, 5, 6]
count_color = 0
count_side = 0

S = 2000
r = sqrt(S)

def draw_figure(n, color):
    angle = 360 / n
    side = sqrt(4 * S * tan(radians(180 / n)) / n)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(n):
        t.forward(side)
        t.right(angle)
    t.end_fill()

step = ceil(r * 3.5)
for y in range(step, -step, -int(step / 2)):
    for x in range(-step, step, int(step / 2)):
        t.penup()
        t.goto(x, y)
        n = sides[count_side]
        count_side = (count_side + 1) % (len(sides))
        color = colors[count_color]
        count_color = (count_color + 1) % (len(colors))
        draw_figure(n, color)
        t.pendown()
    shuffle(sides)
    shuffle(colors)
