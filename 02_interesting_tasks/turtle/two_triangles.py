import turtle as t


t.hideturtle()
t.speed(10)

size = 150
angle = 120
rd = size / 5

def triangle():
    for _ in range(3):
        t.forward(size)
        t.left(angle)

def draw_circles():
    t.fillcolor('black')
    for _ in range(3):
        t.penup()
        t.backward(rd)
        t.pendown()
        t.right(90)
        t.begin_fill()
        t.circle(rd)
        t.end_fill()
        t.left(90)
        t.penup()
        t.forward(rd)
        t.left(60)
        t.forward(size)
        t.left(angle / 2)


triangle()

t.penup()
t.goto(size / 2, - size / 3)

draw_circles()

t.pendown()
color = 'white'
t.fillcolor(color)
t.pencolor(color)
t.begin_fill()
t.setheading(angle / 2)
triangle()
t.end_fill()
