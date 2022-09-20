# rand_walk3.py

#
# The turtle does a "random walk" across the screen. If it hits the edge of
# the screen, it jumps to the opposite side, i.e. it "wraps around".
#
# To make the jumping faster, we hide the turtle and set its movement speed
# to max while it's jumping. After the jump we reset its speed and make
# it visible again.
#
# random.uniform(a, b) returns a randonly chosen float from a to b.
#

import turtle
import random

max_X = turtle.window_width() / 2
min_X = -max_X

max_Y = turtle.window_height() / 2
min_Y = -max_Y

for n in range(1000):
    turtle.forward(10)
    angle = random.uniform(-10, 10)
    turtle.left(angle)

    if turtle.xcor() > max_X: # gone off the right edge?
        turtle.up()
        turtle.hideturtle()
        turtle.speed('fastest')
        turtle.goto(min_X, turtle.ycor())
        turtle.speed('normal')
        turtle.showturtle()
        turtle.down()
    elif turtle.xcor() < min_X: # gone off the left edge?
        turtle.up()
        turtle.hideturtle()
        turtle.speed('fastest')
        turtle.goto(max_X, turtle.ycor())
        turtle.speed('normal')
        turtle.showturtle()
        turtle.down()
    elif turtle.ycor() > max_Y: # gone off the bottom edge?
        turtle.up()
        turtle.hideturtle()
        turtle.speed('fastest')
        turtle.goto(turtle.xcor(), min_Y)
        turtle.speed('normal')
        turtle.showturtle()
        turtle.down()
    elif turtle.ycor() < min_Y: # gone off the top edge?
        turtle.up()
        turtle.hideturtle()
        turtle.speed('fastest')
        turtle.goto(turtle.xcor(), max_Y)
        turtle.speed('normal')
        turtle.showturtle()
        turtle.down()

