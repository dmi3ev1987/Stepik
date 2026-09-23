import turtle as t

bg_color = 'blue'
color = 'Goldenrod'
t.Screen().bgcolor(bg_color)
size = 200
t.penup()
t.hideturtle()
t.tracer(0, 0)

for i in range(size, -size - 1, -1):
    t.goto(0, 0)
    t.dot(size, color)
    t.goto(i, 0)
    t.dot(size, bg_color)
    t.update()
