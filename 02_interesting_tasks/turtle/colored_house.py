import turtle as t

t.hideturtle()
t.speed(10)

size = 150

t.begin_fill()
t.fillcolor('sienna')

for i in range(3):
    angle = 120
    t.forward(size)
    t.left(angle)

t.end_fill()

t.penup()
size_2 = size / 6
t.goto(size_2, 0)
t.pendown()
t.fillcolor('DeepSkyBlue')

t.begin_fill()
for _ in range(4):
    angle = 90
    t.forward(size - (size_2) * 2)
    t.right(angle)
    
t.end_fill()
