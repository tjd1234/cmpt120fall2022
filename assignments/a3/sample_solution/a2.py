# a2_solution.py

import turtle
import math
import random

turtle.speed(0)
turtle.hideturtle()
turtle.color('purple')

def polygon(n, size):
    if n < 3:
        print('polygon error: n must be 3 or more')
        return
    elif size <= 0:
        print('polygon error: size must be >= 0')
        return

    angle = 360 / n
    for i in range(n):
        turtle.forward(size)
        turtle.left(angle)

def jump_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def jump_to_test():
    m = 50
    jump_to(-m, m)
    polygon(5, 50)
    jump_to(m, -m)
    polygon(5, 50)
    jump_to(m, m)
    polygon(5, 50)
    jump_to(-m, -m)
    polygon(5, 50)

def jump_to_delta(dx, dy):
    x, y = turtle.position()
    jump_to(x + dx, y + dy)

# size = 2 * radius * sin(pi/n)
def circle(radius):
    n = 50
    size = 2 * radius * math.sin(math.pi / n)
    polygon(n, size)

def circle_test():
    circle(30)
    circle(50)
    circle(80)
    circle(100)

def eye(radius):
    turtle.begin_fill()
    circle(radius)
    turtle.end_fill()
    circle(2 * radius)

def eye_test():
    jump_to(-105, 0)
    eye(50)
    jump_to(105, 0)
    eye(50)

def mouth(size, style):
    if style == 'happy':
        turtle.setheading(0)
        turtle.right(40)
        turtle.forward(size)
        turtle.left(80)
        turtle.forward(size)
    elif style == 'sad':
        turtle.setheading(0)
        turtle.left(40)
        turtle.forward(size)
        turtle.right(80)
        turtle.forward(size)
    elif style == 'surprised':
        jump_to_delta(0.90 * size, 0)
        turtle.circle(size / 2.5)
    else:
        turtle.setheading(0)
        turtle.forward(size)

def mouth_test():
    size = 50
    jump_to(-150, 0)
    mouth(size, 'happy')
    jump_to(-25, 0)
    mouth(size, 'sad')
    jump_to(120, 0)
    mouth(size, 'surprised')
    jump_to(200, 0)
    mouth(size, 'neutral')

def nose(size):
    turtle.setheading(0)
    turtle.left(5)
    turtle.forward(size/2)
    turtle.left(130)
    turtle.forward(size)

def nose_test():
    nose(100)

def head_helper(size, smile_style):
    x, y = turtle.position()
    eye(size/5)
    jump_to(x + size, y)
    eye(size/5)

    jump_to(x + 0.7*size, y - 0.85 * size)
    nose(size)

    jump_to(x + 0.025*size, y - 1.75*size)
    mouth(size, smile_style)

    jump_to(x + 0.5*size, y - 2.8*size)
    turtle.setheading(0)
    circle(2 * size)

def head(size):
    style = random.choice(['happy', 'sad', 'surprised', 'neutral'])
    head_helper(size, style)

def head_test():
    head_helper(50, 'surprised')

def stick_figure(size):
    x, y = turtle.position()
    head(size)
    turtle.right(90)
    height = random.randrange(size, 3*size)
    turtle.forward(height)

    xb, yb = turtle.position()
    turtle.left(random.randrange(20, 60))
    turtle.forward(size)
    jump_to(xb, yb)
    turtle.setheading(270)
    turtle.right(random.randrange(20, 60))
    turtle.forward(size)

    jump_to(xb, yb + height/2)
    turtle.setheading(0)
    xm, ym = turtle.position()
    turtle.left(random.randrange(20, 60))
    turtle.forward(size)
    jump_to(xm, ym)
    turtle.setheading(180)
    turtle.right(random.randrange(20, 60))
    turtle.forward(size)


def crowd(n, min_size, max_size):
    for i in range(n):
        x = random.randrange(-400, 400)
        y = random.randrange(-400, 400)
        jump_to(x, y)
        size = random.randrange(min_size, max_size + 1)
        stick_figure(size)

#turtle.Screen().tracer(0)
#crowd(100, 5, 20)
#turtle.Screen().update()