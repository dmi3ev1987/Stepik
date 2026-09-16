import turtle as t


t.hideturtle()
t.speed(10)

size = 100

t.fillcolor('black')

t.begin_fill()
t.right(90)
t.forward(size * 1.5)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size * 3)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size * 1.5)
t.end_fill()

t.left(90)

t.penup()
t.goto(size / 2, -size / 3)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(size / 3)
t.end_fill()

t.penup()
t.goto(size / 2, size - size / 3)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.circle(size / 3)
t.end_fill()

t.penup()
t.goto(size / 2, -size / 3 - size)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.circle(size / 3)
t.end_fill()
