# Lecture 10 Notes

## Calling a main() Function

It's traditional in programming to call the first function of your program
`main`. In C++ and Java, for example, you *must* have a function called `main`
in every program.

Python doesn't require a `main()` function, but it's usually a good idea
because it tells people who are reading your code where to start. Python
programs can consist of hundreds of functions, and agreeing that `main()` is
the starting function makes it much easier to read.

Here's a program from earlier in the course:

```main
name = 'Bob'
age = 20
gpa = 3.09

print('Student:', name)
print('Age:', age)
print('GPA:', gpa)
```

Re-writing this using a `main()` function looks like this:

```main
def main():
	 name = 'Bob'
	 age = 20
	 gpa = 3.09

	 print('Student:', name)
	 print('Age:', age)
	 print('GPA:', gpa)
```

To run this program you need to type `main()`.


## Example: Re-writing Euclid's GCD Algorithm

Earlier in the course we saw this program for calculating the greatest common
divisor of two numbers:

```python
# euclid.py

# get the input numbers from the user (as strings)
a = input('What is a? ')
b = input('What is b? ')

# convert the strings to integers
a = int(a)
b = int(b)

# find the greatest common divisor
while a != b:
    print(a, b)  # see how and a and b change
    if a > b:
        a = a - b
    else:
        b = b - a

# print the result
print("greatest common divisor:", a)
```

See [euclid.py](euclid.py).


It works fine, but we lets re-structure it using functions.

First, it asks the user to enter a number, which we read as a string and then
convert to an `int`. Let's make a function to do that:

```python
def get_int(prompt):
    result = input(prompt)
    result = int(result)
    return result
```

Now we can get `a` and `b` like this:

```python
a = get_int('What is a? ')
b = get_int('What is b? ')
```

This is both shorter, and more readable (the names of the function say what is
happening). Plus you can save `get_int` to re-use in other programs.

Second, let's put the GCD algorithm in its own function:

```python
def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    # a == b at this point
    return a
```

For example:

```python
>>> gcd(1345, 9038)
1
>>> gcd(2751, 19038)
3
```

With these functions, the original program can be written like this:

```python
a = get_int('What is a? ')
b = get_int('What is b? ')
print("greatest common divisor:", gcd(a, b))
```

> **Challenge** Re-write this program so it uses no variables, and has only
> one statement: a single call to `print`.

This is the code we want to run first, so we can put it in a main function:

```python
# euclid2.py

def main():
    a = get_int('What is a? ')
    b = get_int('What is b? ')
    print("greatest common divisor:", gcd(a, b))

def get_int(prompt):
    result = input(prompt)
    result = int(result)
    return result

def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    # a == b at this point
    return a
```

See [euclid2.py](euclid2.py).

You read this code starting with `main()`, which is short and simple. And
maybe that's all you need to read. If you need more details about `get_int` or
`gcd` works, you can read those next.
