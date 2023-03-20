import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')

t.penup()
# t.goto(50, 40)
t.pendown()

i = 0
while i < 360:
    for j in range(len(colors)):
        t.pencolor(colors[j])
        t.width(i / 100 + 1)
        t.forward(i)
        t.left(59)
        i += 1

turtle.done()
