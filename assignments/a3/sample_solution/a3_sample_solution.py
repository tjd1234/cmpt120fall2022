# a3_sample_solution.py

import turtle
import random
import a2   # assignment 2, has stick figure

def is_int(n):
    """ Returns True if n is string formatted as an int, or a number
    that can be converted to an int. Other, False is returned.

    >>> is_int('5')
    True
    >>> is_int('5.6')
    False
    """
    try:
        int(n)
        return True
    except ValueError:
        return False

def ask_int1(prompt):
    """Prints prompt on the screen and returns the int entered as an int.
    If a non-int is entered, the program asks again.
    """
    s = input(prompt)
    while not is_int(s):
        s = input(prompt)
    return int(s)

def ask_int2(prompt):
    """Prints prompt on the screen and return the int entered.
    If a non-int is entered, the program asks again.

    >>> ask_int2('Please enter a number: ')
    Please enter a number: 2.4
    Sorry,  don't know what int 2.4 is. Please try again.
    Please enter a number: three
    Sorry,  don't know what int three is. Please try again.
    Please enter a number: -343
    -343
    """
    s = input(prompt)
    while not is_int(s):
        print(f"Sorry, I don't know what int {s} is. Please try again.")
        s = input(prompt)
    return int(s)

def ask_int_between(lo, hi):
    """Gets an integer from the user in the range lo to hi, inclusive.
    If a non-int is entered, or if the int is less than lo or greater than
    hi, the program asks again.

    >>> ask_int_between(2, 6)
    Please enter a number from 2 to 6: 1
    Please try again: 1 is too low.
    Please enter a number from 2 to 6: 7
    Please try again: 7 is two high.
    Please enter a number from 2 to 6: 7.8
    Sorry,  don't know what int 7.8 is. Please try again.
    Please enter a number from 2 to 6: 2
    2

    Note that often it's a bad idea to use while True. But in this case it is
    not too bad: the code is readable and efficient, and there is only one
    return in the body of the final else.
    """
    prompt = f'Please enter a number from {lo} to {hi}: '
    s = input(prompt)
    while True:
        if not is_int(s):
            print(f"Please try again: I don't know what int {s} is.")
            s = input(prompt)
        else:
            n = int(s)
            if n < lo:
                print(f"Please try again: {n} is too low.")
                s = input(prompt)
            elif n > hi:
                print(f"Please try again: {n} is two high.")
                s = input(prompt)
            else:
                return n

def jump_to(x, y):
    """Moves the turtle to (x, y) without drawing a line.
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def pentagon_at(x, y, size):
    """Draws a pentagon. (x, y) is the lower-left corner.
    The turtle ends up facing in the same direction as just
    before the function was called.
    """
    jump_to(x, y)
    for i in range(5):
        turtle.forward(size)
        turtle.left(72)

def pentagon_test():
    turtle.showturtle()
    turtle.speed('slowest')
    pentagon_at(0, 0, 100)

def pentagonal_flower(x, y, size):
    n = ask_int_between(5, 50)
    angle = 360 / n
    for i in range(n):
        pentagon_at(x, y, size)
        turtle.right(angle)
    turtle.hideturtle()

# This function is not required. It's only used for fun, to give the figures a
# little more variety.
def draw_figure_rand(size):
    dx = random.uniform(-5, 5)
    dy = random.uniform(-5, 5)
    x, y = turtle.position()
    jump_to(x + dx, y + dy)
    a2.stick_figure(size)

def figure_row(x, y, n):
    for c in range(n):
        jump_to(x + c * 50, y)
        turtle.setheading(0)
        draw_figure_rand(10)

def figure_grid(x, y, rows, cols):
    for r in range(rows):
        print(f'row {r}')
        figure_row(x, y + r * 100, cols)

turtle.Screen().tracer(0)
figure_grid(-300, -400, 10, 10)
turtle.Screen().update()

