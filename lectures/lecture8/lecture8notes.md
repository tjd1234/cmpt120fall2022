# Lecture 8 Notes

## Functions

A **function** is a named group of statements. Functions can receive input and
return output.

This function draws a square:

```python
import turtle

def square(n):
	for i in range(4):
		turtle.forward(n)
		turtle.left(90)
```

Note a few things:

- `def square(n):` is called the **function header**. The three indented lines
  of code after it are called the **function body**.

- `def` is short for *definition*.

- The function's name is `square`, and it takes one input that it calls `n`.
  Function names follow essentially the same rules for variable names, e.g.
  they must consist of letters, digits, and underscores, and they *can't*
  start with a digit or be the same as a Python keyword.

- The function header ends with a `:`.

- The code in a function body must be consistently indented underneath the
  header.

- `square` takes one input value `n`, which is used in the statement
  `turtle.forward(n)`. Thus `n` must be a number.

- `square` does *not* return a value. Instead, it makes the turtle draw a
  picture. So it is different than a mathematical function (which would always
  return a value).


# Function Documentation

It's often a good idea to **document** a function, i.e. to explain what it
does and how it works. For example:

```python
import turtle

def square(n):
  """ Draws a square with side of length n.
  Assumes the turtle module has been imported.
  """
	for i in range(4):
		turtle.forward(n)
		turtle.left(90)
```

Here we've put a **doc-string** after the header and before the body, indented
the same amount as the body.

`"""` in Python are **triple quotes**, and they are useful here because they
let you write multi-line strings.

You can also put documentation before a function using source code comments:

```python
import turtle

# Draws a square with side of length n.
# Assumes the turtle module has been imported.
def square(n):
	for i in range(4):
		turtle.forward(n)
		turtle.left(90)
```

## Functions that Return Values

This function both takes an input (the radius of a circle), and returns an
output value (the area of the circle):

```python
def circle_area(radius):
	return 3.14 * radius ** 2
```

The `return` keyword causes the function to immediately stop, and the value of
the return expression is the output of the function.

This function returns the sum of the numbers from 1 to $$n$$ using the formula
$\frac{n(n+1)}{2}$:

```python
def add_nums(n):
	return n * (n + 1) / 2
```

This function takes two inputs and returns a single value (the area of the
triangle):

```python
def triangle_area(base, height):
	return base * height / 2
```

Here's a function that returns a string:

```python
def exclaim(s, n):
	""" Returns a string with n exclamation marks after s.
	"""
	return s + '!' * n
```

For example:

```python
>>> exclaim('Yes', 5)
'Yes!!!!!'
>>> exclaim('No', 2)
'No!!'
```

You can create new variables inside functions if it's useful to do so:

```python
def cube_surface_area(side):
	""" Returns the surface area of a cube.
	side is the length of an edge.
	"""
	face = side ** 2
	return 6 * face
```

`face` is called a **local variable**, or sometimes a **temporary variable**.
It is only used inside of `cube_surface_area`. When the function ends, Python
automatically deletes `face`.

Here's a function that returns a value, but doesn't take any input:

```python
import random

def roll_die():
	""" Randomly returns 1, 2, 3, 4, 5, or 6.
	"""
	return random.randrange(1, 7)
```

Every time you call `roll_die()` it returns a randomly chosen value form 1 to
6:

```python
>>> roll_die()
4
>>> roll_die()
1
>>> roll_die()
6
>>> roll_die()
6
```
