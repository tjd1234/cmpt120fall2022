# recursion.py

def f1():
    """In theory, this should loop forever an never return. But in practice Python stops
    the recursion after a certain number of calls.

    >>> f()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in f
    File "<stdin>", line 1, in f
    File "<stdin>", line 1, in f
    [Previous line repeated 996 more times]
    RecursionError: maximum recursion depth exceeded
    """
    f1()

def f2():
    """Similar to f1, but prints a message before each call.
    """
    print('hello!')
    f2()


count = 0
def f3():
    """This is like f2(), but prints how many times it has been called.
    """
    global count  # tell Python that count is the global variable defined outside the function
    print(f'{count}. hello!')
    count += 1
    f3()

def f4_bad():
    """A wrong way to implement f3 without using a global variable.
    """
    count = 0
    print(f'{count}. hello!')
    count += 1
    f4_bad()

def f4(count):
    """A correct way to implement f3 without using a global variable.
    """
    print(f'{count}. hello!')
    count += 1
    f4(count)

def f4_better(count):
    """A better way to implement f4.
    """
    print(f'{count}. hello!')
    f4_better(count + 1)

def f4_bad_again(count):
    print(f'{count}. hello!')
    f4_bad_again(count)  # oops: forgot the + 1
