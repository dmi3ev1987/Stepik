import turtle


colors = ['green', 'purple', 'orange', 'red', 'blue', 'yellow']
turtle.hideturtle()
turtle.speed(10)
step = 5
size = 0
angle = 45
n = 45

for i in  range(n):
    size += 0.5
    turtle.pensize(size)
    turtle.pencolor(colors[i % len(colors)])
    turtle.forward(step)
    turtle.left(angle)
    step += 3
