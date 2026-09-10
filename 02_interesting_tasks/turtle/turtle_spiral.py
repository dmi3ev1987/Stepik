import turtle

angle = 20
n = 65
turtle.speed(10)
turtle.shape('turtle')
turtle.bgcolor('LightGreen')
turtle.penup()

for i in range(n):
    turtle.stamp()
    turtle.left(angle)
    turtle.forward(i)
