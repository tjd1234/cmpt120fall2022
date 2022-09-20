# rand_walk4.py

#
# This is the same as rand_walk4.py, but the jump_to(x, y) has been added
# to simplify the main code.
#

import turtle
import random

max_X = turtle.window_width() / 2
min_X = -max_X

max_Y = turtle.window_height() / 2
min_Y = -max_Y

def jump_to(x, y):
    turtle.up()
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.goto(x, y)
    turtle.speed('normal')
    turtle.showturtle()
    turtle.down()

for n in range(1000):
    turtle.forward(10)
    angle = random.uniform(-10, 10)
    turtle.left(angle)

    if turtle.xcor() > max_X: # gone off the right edge?
        jump_to(min_X, turtle.ycor())
    elif turtle.xcor() < min_X: # gone off the left edge?
        jump_to(max_X, turtle.ycor())
    elif turtle.ycor() > max_Y: # gone off the bottom edge?
        jump_to(turtle.xcor(), min_Y)
    elif turtle.ycor() < min_Y: # gone off the top edge?
        jump_to(turtle.xcor(), max_Y)


