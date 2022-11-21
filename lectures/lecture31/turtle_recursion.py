# turtle_recursion.py

#
# Turtle graphics and recursion
#

import turtle

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def star(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

def sequence(shape1, shape2):
    """Return a function that draws shape1, then shape2.
    """
    def fn(size):
        shape1(size)
        shape2(size)
    return fn

def design(size, step, rotate, shape):
    # only draw something when size is big enough
    if size > 0:
        shape(size)
        turtle.right(rotate)
        design(size - step, step, rotate, shape)


def jump_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def get_turtle_state():
    """Return the current turtle state as a tuple.
    """
    return [turtle.position(), turtle.heading()]

SCALE = 3.0

def draw_V(x, y, size):
    """Draw a V with the bottom at (x, y).
    Returns the state of the top points of the V.
    """
    jump_to(x, y)               # go to the bottom
    turtle.left(30)
    turtle.forward(size * SCALE)
    left = get_turtle_state()   # remember position and heading
    jump_to(x, y)               # go back to the bottom
    turtle.right(60)
    turtle.forward(size * SCALE)
    right = get_turtle_state()  # remember position and heading
    return [left, right]

# def tree_test1(x, y, size, color):
#     turtle.color(color)
#     turtle.setheading(90)  # face north
#     if size > 1:
#         left, right = draw_V(x, y, size)
#         tree_test1(left[0], left[1], 3 * size // 4, 'green')
#         tree_test1(right[0], right[1], 3 * size // 4, 'red')

import random

def tree_test2(x, y, size):
    turtle.left(random.randint(-5, 5))
    if size > 1:
        left, right = draw_V(x, y, size)
        turtle.setheading(left[1])
        tree_test2(left[0][0], left[0][1], 3 * size // 5)
        turtle.setheading(right[1])
        tree_test2(right[0][0], right[0][1], 3 * size // 5)

def tree_test3(x, y, size):
    turtle.left(random.randint(-5, 5))
    if size > 5:
        left, right = draw_V(x, y, size)
        turtle.setheading(left[1])
        left_size = random.uniform(0.8, 0.9) * size
        tree_test3(left[0][0], left[0][1], left_size)

        turtle.setheading(right[1])
        right_size = random.uniform(0.8, 0.9) * size
        tree_test3(right[0][0], right[0][1], right_size)

def tree_test4(x, y, size):
    turtle.left(random.randint(-5, 5))
    if size > 5:
        left, right = draw_V(x, y, size)
        turtle.setheading(left[1])
        left_size = random.uniform(0.8, 0.9) * size
        turtle.pensize(5 * left_size / 20)
        tree_test4(left[0][0], left[0][1], left_size)

        turtle.setheading(right[1])
        right_size = random.uniform(0.8, 0.9) * size
        turtle.pensize(5 * right_size / 20)
        tree_test4(right[0][0], right[0][1], right_size)

def canopy(x, y, size):
    turtle.left(random.randint(-5, 5))
    if size > 3:
        left, right = draw_V(x, y, size)
        turtle.setheading(left[1])
        left_size = random.uniform(0.8, 0.9) * size
        turtle.pensize(5 * left_size / 20)
        canopy(left[0][0], left[0][1], left_size)

        turtle.setheading(right[1])
        right_size = random.uniform(0.7, 0.9) * size
        turtle.pensize(5 * right_size / 20)
        canopy(right[0][0], right[0][1], right_size)
    else:
        if random.random() > 0.9:
            turtle.dot(5, 'orange')

def draw_tree(x, y, draw_fast=True):
    if draw_fast:
        turtle.Screen().tracer(0)  # don't show any drawing on the screen

    turtle.hideturtle()
    turtle.color('green')     # trees are green, right?
    turtle.setheading(90)     # trees group upwards

    trunk_len = 50            # set the trunk length
    turtle.pensize(7)         # and thickness
    jump_to(x, y - trunk_len)
    turtle.forward(trunk_len) # draw the trunk
    canopy(x, y, 20)

    if draw_fast:
        turtle.Screen().update()   # refresh the screen to see what was drawn

# draw three trees
draw_tree(0, -300, 20)
draw_tree(-250, 100, 20)
draw_tree(350, 200, 20)
