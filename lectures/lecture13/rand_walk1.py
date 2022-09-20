# rand_walk1.py

#
# The turtle does a "random walk" across the screen. It's possible the turtle
# can walk off the screen and disappear.
#
# random.uniform(a, b) returns a randonly chosen float from a to b.
#

import turtle
import random

for n in range(1000):
    turtle.forward(10)
    angle = random.uniform(-10, 10)
    turtle.left(angle)
