import turtle


turtle.hideturtle()
turtle.speed(10)

turtle.pencolor('green')
dot_size = 10
turtle.dot(dot_size, 'red')

def draw_lines(n):
    start = 200
    for i in range(-start, start + 1, (start * 2) // n):
        turtle.goto(i, -start)
        turtle.dot(dot_size, 'blue')
        turtle.setposition(0, 0)

draw_lines(10)
