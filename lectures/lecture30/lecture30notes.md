# Lecture 30 Notes

In programming, a function is **recursive** if it calls itself. For example, `f`
is a recursive function:

```python
def f1(n):
    f1(n)
```

When run, it should, in theory, loop forever and never return a value. However,
Python has a limit on how many times a function can call itself, and if it
reaches that limit, a `RecursionError` exception is raised:

```
>>> f1()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

`f1()` isn't very useful. Here's a slightly more useful recursive function:

```python
def f2():
    print('hello!')
    f2()
```

It's similar to `f1`, but it prints a message before calling itself. When run,
it prints `hello!` many times, and then crashes with a `RecursionError`:

```
>>> f2()
hello!
hello!
hello!
hello!
... lots more ...
hello!

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "recursion.py", line 22, in f2
    f2()
  File "recursion.py", line 22, in f2
    f2()
  File "recursion.py", line 22, in f2
    f2()
  [Previous line repeated 992 more times]
  File "recursion.py", line 21, in f2
    print('hello!')
RecursionError: maximum recursion depth exceeded while calling a Python object
```

In theory, this should loop forever and print `'hello!'` an infinite number of
times. But in practice, Python only has limited time and memory, so it
eventually crashes.

> From now on we'll skip writing out the Traceback message, and just write the
> `RecursionError` line.

How many times is `'hello!` printed? One way to figure this out is to print the
number of each one like this:

```python
count = 0  # count is a global variable

def f3():
    global count  # tell Python that count is the global variable defined outside the function
    print(f'{count}. hello!')
    count += 1
    f3()
```

It prints this:

```python
>>> f3()
1. hello!
2. hello!
3. hello!
4. hello!
... lots more ...
993. hello!
994. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

So we see `'hello!'` is printed 994 times before the program crashes.

A problem with `f3` is that it relies on the global variable `count`. Global
variables are generally a bad idea because other code in the program could
modify `count` in a way that makes `f3` work incorrectly. We also need the ugly
statement `global count` to tell Python that `count` is the global variable
defined outside the function.

How could we re-write `f3` so that it doesn't use a global variable? One way
that *doesn't* work is this:

```python
def f4_bad():
    """A wrong way to implement f3 without using a global variable.
    """
    count = 0
    print(f'{count}. hello!')
    count += 1
    f4_bad()
```

`f4_bad` prints this:

```
>>> f4_bad()
0. hello!
0. hello!
0. hello!
... lots more ...
0. hello!
0. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

`count` is always 0 because every time you call `f4_bad`, it creates a *new*
`count` that is initialized to 0. When `count += 1` is called, that particular
value is never touched again by the function.

Instead of declaring a local variable inside the function, what if we instead
pass it as a parameter?

```python
def f4(count):
    """A correct way to implement f3 without using a global variable.
    """
    print(f'{count}. hello!')
    count += 1
    f4(count)
```

It prints this:

```
>>> f4(0)    # must pass in the 0
1. hello!
2. hello!
3. hello!
... lots more ...
993. hello!
994. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

This works! Well, it still crashes, but we'll fix that in a moment. By passing
the `count` as a parameter, we are able to correctly update it. 

The statement `count += 1` in `f4` is usually deleted, and instead `f4_better`
is called directly with `count + 1`:

```python

```python
def f4_better(count):
    print(f'{count}. hello!')
    f4_better(count + 1)
```

The `+ ` is important in the last line. If you forget it, then `count` is never
incremented:

```python
def f4_bad_again(count):
    print(f'{count}. hello!')
    f4_bad_again(count)  # oops: forgot the + 1
```

This prints:

```
>>> f4_bad_again(0)
0. hello!
0. hello!
0. hello!
... lots more ...
0. hello!
0. hello!

RecursionError: maximum recursion depth exceeded while calling a Python object
```

To be continued ...
