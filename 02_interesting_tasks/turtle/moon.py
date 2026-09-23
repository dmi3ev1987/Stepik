import turtle as t


t.speed(10)
t.hideturtle()

bg_color = 'DarkBlue'
t.Screen().bgcolor(bg_color)
size = 100

t.penup()
t.goto(0, -100)

t.pendown()
color = 'Goldenrod'
t.pencolor(color)
t.fillcolor(color)
t.begin_fill()
t.circle(size)
t.end_fill()

t.penup()
t.forward(size/4)

t.pendown()
t.pencolor(bg_color)
t.fillcolor(bg_color)
t.begin_fill()
t.circle(size)
t.end_fill()
