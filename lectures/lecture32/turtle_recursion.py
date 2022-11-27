# turtle_recursion2.py

#
# Recursive trees using turtle graphics.
#

import turtle
import random

#
# helper functions
#
def jump_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def get_turtle_state():
    """Return the turtle state as a list, [(x, y), heading]
    """
    return [turtle.position(), turtle.heading()]

#
# drawing functions
#

def draw_V(x, y, size):
    """Draw a V with the bottom at (x, y).
    Returns the state of the top two points of the V.
    """
    jump_to(x, y)               # (x, y) is the bottom of the V
    turtle.left(30)
    turtle.forward(size)
    left = get_turtle_state()   # remember position and heading
    jump_to(x, y)               # go back to the bottom
    turtle.right(60)
    turtle.forward(size)
    right = get_turtle_state()  # remember position and heading
    #
    # return the position and heading of both the upper-left and upper-right
    # point of the V
    #
    return [left, right]

def draw_fork(x, y, size):
    """Draw a fork-like with the bottom at (x, y).
    Returns a list of the the turtle state of the top two points of the fork.
    """
    jump_to(x, y)

    # the trunk of the fork
    turtle.forward(size)

    mid_pt, mid_heading = get_turtle_state()

    # left part of the fork
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.right(90)
    turtle.forward(size // 2)
    left = get_turtle_state()

    # re-position and re-orient the turtle to the middle of fork
    jump_to(mid_pt[0], mid_pt[1])
    turtle.setheading(mid_heading)

    # right part of the fork
    turtle.right(90)
    turtle.forward(size // 2)
    turtle.left(90)
    turtle.forward(size // 2)
    right = get_turtle_state()

    return [left, right]


def canopy(x, y, size, scale = 3.0):
    """Draw the leafy top of the tree.

    - size is the starting thickness of the branches.
    - scale is overall size of the canopy

    The draw_V function is assumed to return a 2-element list with the positions
    and headings of the next branches. You can get different looking trees by
    changing draw_V, e.g. try replacing it with draw_fork.
    """
    turtle.left(random.randint(-5, 5))
    if size > 3:
        left, right = draw_V(x, y, size * scale)
        turtle.setheading(left[1])
        left_size = random.uniform(0.8, 0.9) * size
        turtle.pensize(5 * left_size / 20)
        canopy(left[0][0], left[0][1], left_size)

        turtle.setheading(right[1])
        right_size = random.uniform(0.7, 0.9) * size
        turtle.pensize(5 * right_size / 20)
        canopy(right[0][0], right[0][1], right_size)
    else:
        if random.random() > 0.9:    # sometimes and an orange at the end of a branch
            turtle.dot(10, 'orange')

def draw_tree(x, y, size, draw_fast=True):
    #
    # set up the turtle
    #
    if draw_fast:
        turtle.Screen().tracer(0)  # don't show any drawing on the screen

    turtle.hideturtle()

    #
    # draw the canopy
    #
    turtle.color('green')        # trees are green, right?
    turtle.setheading(90)        # trees grow upwards
    turtle.pensize(7)            # initial thickness
    canopy(x, y, size)

    #
    # draw the trunk
    #
    # done after the canopy so it looks like it sprouts from the trunk
    # 
    turtle.setheading(90)        # trees grow upwards
    turtle.pensize(15)           # trunk is thicker than the rest of the tree
    turtle.color('brown')
    trunk_len = 50               # set the trunk length
    jump_to(x, y - trunk_len)
    turtle.forward(trunk_len)    # draw the trunk

    if draw_fast:
        turtle.Screen().update() # refresh the screen to see what was drawn

#
# draw three trees
#
draw_tree(   0, -300, 20, 2)
draw_tree(-250,  100, 20, 2)
draw_tree( 350,  200, 20, 2)
