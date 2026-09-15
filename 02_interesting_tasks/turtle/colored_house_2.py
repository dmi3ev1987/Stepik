import turtle as t

t.hideturtle()
t.speed(10)

size = 100

t.begin_fill()
t.fillcolor('sienna')
t.goto(size, 0)
t.goto(0, size)
t.goto(-size, 0)
t.forward(size/3)
t.end_fill()

size_2 = size/3 * 2 * 2
t.fillcolor('DeepSkyBlue')

t.begin_fill()
for _ in range(4):
    angle = 90
    t.forward(size_2)
    t.right(angle)
    
t.end_fill()
