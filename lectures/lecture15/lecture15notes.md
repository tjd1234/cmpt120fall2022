## Lecture 15 Notes

In what follows we give a few more examples of programs that use loops.

### Example: Random Turtle Walk

In a previous lecture we saw this program for making a turtle do a "random
walk" around the screen. When the turtle hits an edge, it "wraps around" to
the opposite side of the screen:


```python
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
    x, y = turtle.position()

    if x > max_X: # gone off the right edge?
        jump_to(min_X, y)
    elif x < min_X: # gone off the left edge?
        jump_to(max_X, y)
    elif y > max_Y: # gone off the bottom edge?
        jump_to(x, min_Y)
    elif y < min_Y: # gone off the top edge?
        jump_to(x, max_Y)
```

The for-loop makes the turtle move exactly 1000 times. If we wanted it to walk
*forever*, we can replace the for-loop header with a while-loop:

```python
# ...

while True:
    # ...
```

### Example: Calculating a Square Root

The easiest way to calculate a square root in Python is to use `math.sqrt`:

```python
import math

print(math.sqrt(5))  # 2.23606797749979
```

Here's another way to do it using method based on [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method):

```python
def newton_sqrt(x):
    """ Returns the square root of x, for x > 0.
    Uses Newton's method to estimate the square root.
    """
    approx = 0.5 * x
    better = 0.5 * (approx + x / approx)
    while better != approx:
        #print(f'  {approx}')
        approx = better
        better = 0.5 * (approx + x / approx)
    return approx
```

For this course, we won't worry about *why* this finds the square root, or how
the method was discovered. We use it as an example of a while-loop that is not
just a simple counting loop. 

The loop condition is `better != approx`, and ahead of time we don't how many
times the loop will iterate. So we couldn't write this as a for-loop.

It's instructive to uncomment the `print` statement in `newton_sqrt` to see
the intermediate values that are calculated.


### Example: Sentinel Loops

A **sentinel loop**, or **sentinel value loop**, is a loop that stops when
some final (sentinel) value is encountered. For example:

```python
count = 0
total = 0.0
num = input('Please enter a number ("done" to end): ')
while num != 'done':
    total += float(num)
    count += 1
    num = input('Please enter a number ("done" to end): ')

print()
print(f'You entered {count} numbers.')
print(f'Their total is {total}.')
print(f'Their average is {total / count :.2f}.')
```

In this example `'done'` is the sentinel value that makes the loop stop. The
user can enter any number of numbers.
