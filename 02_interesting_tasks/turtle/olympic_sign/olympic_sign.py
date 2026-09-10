import turtle as t


def draw_cir(size, p_size, color):
    t.pendown()
    t.pencolor(color)
    t.circle(size)
    t.penup()
    t.forward(size * 2 + p_size)

  
size = 50
p_size = 5

t.speed(7)
t.pensize(p_size)

draw_cir(size, p_size, 'cyan')
draw_cir(size, p_size, 'black')
draw_cir(size, p_size, 'red')

t.goto(size, -size)
draw_cir(size, p_size, 'yellow')
draw_cir(size, p_size, 'green')
