# rand_walk2.py

#
# The turtle does a "random walk" across the screen. If it hits the edge of
# the screen, it immediately jumps back to the center, position (0, 0).
#
# random.uniform(a, b) returns a randomly chosen float from a to b.
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
        turtle.goto(0, 0)
        turtle.down()
    elif turtle.xcor() < min_X: # gone off the left edge?
        turtle.up()
        turtle.goto(0, 0)
        turtle.down()
    elif turtle.ycor() > max_Y: # gone off the bottom edge?
        turtle.up()
        turtle.goto(0, 0)
        turtle.down()
    elif turtle.ycor() < min_Y: # gone off the top edge?
        turtle.up()
        turtle.goto(0, 0)
        turtle.down()
