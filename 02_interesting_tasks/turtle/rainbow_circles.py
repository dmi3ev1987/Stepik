import turtle as t


t.hideturtle()
t.speed(10)

colors = [
    'red',
    'orange',
    'yellow',
    'green',
    'LightGreen',
    'cyan',
    'DeepSkyBlue',
    'blue',
    'purple',
    'DeepPink',
]
size = 150
step = size / len(colors)


for i in range(len(colors)):
    t.penup()
    t.goto(0, -size)
    t.fillcolor(colors[i])
    t.pencolor(colors[i])
    t.begin_fill()
    t.pendown()
    t.circle(size)
    t.end_fill()
    size -= step
