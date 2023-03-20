import turtle
import random


def create_rectangle(pen, color, x, y, width, height):
    pen.penup()
    pen.color(color)
    pen.fillcolor(color)
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()

    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)

    pen.end_fill()
    # Reset the orientation of the turtle
    pen.setheading(0)


def create_circle(pen, x, y, radius, color):
    pen.penup()
    pen.color(color)
    pen.fillcolor(color)
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def create_star(pen, x, y, color, size):
    pen.penup()
    pen.color(color)
    pen.goto(x, y)
    pen.begin_fill()
    pen.pendown()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()


turtle.bgcolor("darkblue")
turtle.title("Merry Christmas")
turtle.setup(width=1.0, height=1.0)
pen = turtle.Turtle(shape="turtle")
pen.speed(2)

y = -100

# create tree trunk
create_rectangle(pen, "red", -15, y-60, 30, 60)

# create tree
width = 240
pen.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width / 2
    create_rectangle(pen, "green", x, y, width, height)
    y = y + height

# create a star a top of tree
pen.speed(1)
create_star(pen, -20, y+10, "yellow", 40)

tree_height = y + 40

# create moon in sky
# 1- create a full circle
create_circle(pen, 230, 180, 60, "white")
# 2- overlap with full circle of BG color to make a crescent shape
create_circle(pen, 220, 180, 60, "darkblue")

# now add few stars in sky
pen.speed(10)
number_of_stars = random.randint(20, 30)
# print(number_of_stars)
for _ in range(number_of_stars):
    x_star = random.randint(-(turtle.window_width()//2), turtle.window_width()//2)
    y_star = random.randint(tree_height, turtle.window_height()//2)
    size = random.randint(5, 20)
    create_star(pen, x_star, y_star, "white", size)

# print greeting message
pen.speed(1)
pen.penup()
pen.goto(0, -200)  # y is in minus because tree trunk was below x axis
pen.color("white")
pen.pendown()
msg = "Merry Christmas from PyLearn family"
pen.write(msg, move=False, align="center", font=("Arial", 15, "bold"))

pen.hideturtle()
turtle.done()
