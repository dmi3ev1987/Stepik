import turtle as t


def draw(n, size, color):
    angle = 360 / n
    t.pendown()
    t.fillcolor(color)
    # t.pencolor(color)
    t.begin_fill()
    for _ in range(n):
        t.forward(size)
        t.right(angle)
    t.penup()
    t.end_fill()

t.speed(0)
t.hideturtle()
size = 50
colors = ('black', 'white')
x, y = -2.5 * size, 2.5 * size
q = 5

t.penup()
for i in range(q):
    for j in range(q):
        t.goto(x, y)
        color = colors[(i + j) % 2]
        draw(4, size, color)
        x += size
    x -= size * 5
    y -= size
