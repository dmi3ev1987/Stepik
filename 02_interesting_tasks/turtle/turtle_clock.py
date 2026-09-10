import turtle

size = 100
line = 20
n = 12
turtle.speed(10)
turtle.Screen().bgcolor('cyan')
turtle.shape('turtle')
turtle.stamp()

for _ in range(n):
    turtle.penup()
    turtle.forward(size)
    turtle.pendown()
    turtle.forward(line * 2)
    turtle.penup()
    turtle.forward(line)
    turtle.stamp()
    turtle.backward(size + line * 3)
    turtle.left(360/n)
