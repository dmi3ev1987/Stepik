import turtle as t


t.speed(10)
t.hideturtle()

head_size = 75

t.circle(head_size)
t.circle(head_size/2)

t.penup()
t.left(90)
t.forward(head_size/5)
t.pendown()
t.forward(head_size/2)
t.right(90)
t.circle(head_size/10)

t.penup()
t.goto(head_size/2, head_size)
t.dot(head_size/5)
t.goto(-head_size/2, head_size)
t.dot(head_size/5)

t.goto(0, head_size)
t.left(45)
t.forward(head_size)
t.pendown()
t.right(90)
t.circle(head_size/3)

t.penup()
t.goto(0, head_size)
t.left(180)
t.forward(head_size)
t.pendown()
t.right(90)
t.circle(head_size/3)
