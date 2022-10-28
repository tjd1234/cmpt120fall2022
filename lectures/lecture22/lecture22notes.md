# Lecture 22 Notes

## List Basics

A **list** is a sequence of 0 or more Python values. The values can be of any
type, and don't necessarily need to be all the same. 

**List literals** are start with a `[` and end with `]`, and values are
separated by commas. For example:

```
[]                # the empty list, length 0
[5]
[5, 10, 5]
['hot', 'cold', 'warm', 'dry']
[5, 'five', 5.5]  # lists can contain different types of values
[[1,2], [3,4,5]]  # lists can contain lists
```

`[]` is the empty list, i.e a list of length 0 that has no values.

Recall that a **string** is a sequence of 0 or more *characters*. But a string
is *not* a list:

```
'apple'                     # a string
['a', 'p', 'p', 'l', 'e']   # a list of strings
```

> **Note** Python allowing lists to contain *any* type of value is somewhat
> unusual. In C++, for example, lists can only contain values of the same
> type. In practice, it's not very common to have different types of values on
> the same Python.

The `len(lst)` function returns the **length** of a list:

```
>>> len([])
0
>>> len([5])
1
>>> len(['hot', 'cold', 'warm', 'dry'])
4
>>> len([[1,2], [3,4,5]])
2
>>> len([[[]]])
1
```

## Lists are Mutable

In Python, **mutable** means "changeable", and **immutable** "not changeable".
Python lists are mutable, i.e. you can change the values they contain, or
add/remove items.

This is in contrast to Python strings, which are **immutable**. You can never
modify a Python string.


## List Indexing

Lists follow the same indexing conventions as for strings. If `lst` is a list,
then `lst[i]` is the value at index position `i`. As with strings, the first
index of a list is always 0, i.e. Python lists used **0-based indexing**.

```
>>> scores = [0.88, 0.86, 0.91]
>>> scores[0]
0.88
>>> scores[1]
0.86
>>> scores[2]
0.91
>>> scores[3]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: list index out of range
```

If `lst` is a non-empty list, then `lst[0]` is the first element, and
`lst[len(lst)-1]` is the last element. The last element is at index location
`len(lst) - 1`, and not just `len(lst)`, because the first index is at 0.

If you have lists with lists, then you can get expressions with multiple
indices:

```
>>> table = [[5, 6], [2, 1], [3, 9], [10, 4]]

>>> table[1]
[2, 1]
>>> table[1][0]
2
>>> table[1][1]
1

>>> table[2]
[3, 9]
>>> table[2][0]
3
>>> table[2][1]
9
```

Or strings within lists:

```
>>> words = ['yes', 'no', 'maybe']

>>> words[0]
'yes'
>>> words[0][0]
'y'

>>> words[2]
'maybe'
>>> words[2][3]
'b'
```

## Negative List Indexing

Just as with strings, you can use negative indices to access the elements of a
list. This is useful when you want to access items near the end of the list:

```
>>> lst = [9, 3, 4, 2]
>>> lst[-1]
2
>>> lst[-2]
4
>>> lst[-3]
3
>>> lst[-4]
9
>>> lst[-5]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: list index out of range
```

In general, if `lst` is a non-empty list, then `lst[-1]` is the last element,
`lst[-2]` is the second to last element, and so on down to `lst[-len(lst)]`
(the first element of the list).


## List Membership

You can test if a list contains a particular value using the `in` and `not in`
operators:

```
>>> ages = [3, 4, 3, 3, 2]

>>> 1 in ages
False
>>> 2 in ages
True
>>> 3 in ages
True
>>> 5 in ages
False

>>> 1 not in ages
True
>>> 2 not in ages
False
>>> 3 not in ages
False
>>> 5 not in ages
True
```

Be careful with lists within lists:

```
>>> lst = [1, [2, 3], 4]

>>> 1 in lst
True
>>> 2 in lst
False
>>> 3 in lst
False
>>> [2, 3] in lst
True

>>> 1 not in lst
False
>>> 2 not in lst
True
>>> 3 not in lst
True
>>> [2, 3] not in lst
False
```

## List Slicing

The syntax for getting a slice of a list is the same as for strings. In
general, if `lst` is a list and `begin` and `end` are non-negative integers,
then `lst[begin:end]` is a new list consisting of all the elements from
`lst[begin]` to `lst[end-1]`. If `end` is `len(lst)` or bigger, then the slice
goes up to just the end of the list.

For example:

```
>>> lst = [9, 4, 3, 8, 2]
>>> lst[2:4]
[3, 8]
>>> lst[1:4]
[4, 3, 8]
>>> lst[1:5]
[4, 3, 8, 2]
>>> lst[1:700]
[4, 3, 8, 2]
```

If you leave out the `begin` value, then Python assumes it is 0. If you leave
out the `end` value, Python assumes it is `len(lst)`:

```
>>> lst = [9, 4, 3, 8, 2]
>>> lst[:4]
[9, 4, 3, 8]
>>> lst[4:]
[2]
```

If you leave out both `begin` and `end`, you get a new copy of the entire
list:

```
>>> lst = [9, 4, 3, 8, 2]
>>> lst2 = lst[:]
>>> lst2
[9, 4, 3, 8, 2]
```

## Lists are Mutable

Recall that Python strings are **immutable**, i.e. a Python string can't be
changed in any way. In contrast, Python lists are **mutable**, i.e. they can
be modified:

```
>>> s = 'apple'                                          # strings are immutable
>>> s[0] = 'A'                                           # Python won't let you 
Traceback (most recent call last):                       # modify them
  File "__main__", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> lst = [4, 1, 4, 5]   # lists are mutable (changeable)
>>> lst[0] = 'A'         # you can change values, and add/remove values
>>> lst
['A', 1, 4, 5]
>>> lst[-1] = 'Z'
>>> lst
['A', 1, 4, 'Z']
```

**Aside** You can even do *self-referential* changes like this:

```
>>> lst = [1, 2, 3]
>>> lst[1] = lst
>>> lst
[1, [...], 3]
```

The `[...]` in `[1, [...], 3]` indicates an infinite list. In practice, there
is almost never any reason to create or use self-referential lists. But they
sometimes occur as bugs, so it helpful to be aware of them.

Using slice notation, you can replace an entire slice of a list with a
different slice:

```
>>> lst = [1, 2, 3, 4, 5]
>>> lst[2:4]
[3, 4]
>>> lst[2:4] = ['a', 'b', 'c', 'd']
>>> lst
[1, 2, 'a', 'b', 'c', 'd', 5]
```

To delete a value at location `i` of a list `lst`, you can use the statement
`del lst[i]`:

```
>>> food = ['pear', 'apple', 'toast', 'cereal']
>>> del food[1]
>>> food
['pear', 'toast', 'cereal']
>>> del food[2]
>>> food
['pear', 'toast']
```

`del` can also delete a slice:

```
>>> food = ['pear', 'apple', 'toast', 'cereal']
>>> del food[1:3]
>>> food
['pear', 'cereal']
```

`del` does *not* make a copy of the list. It actually modifies --- *mutates*
--- the existing list. Once something is `del`-ed, it really is gone.

## List Aliasing

When you assign a list to a variable a copy of the list is *not* made:

```
>>> a = [1, 2, 3]      # a and b are both names for the same list
>>> b = a              # changing one of the lists changes the other
>>> a[0] = -1
>>> a
[-1, 2, 3]
>>> b
[-1, 2, 3]

>>> del b[0]
>>> a
[2, 3]
>>> b
[2, 3]
```

This behaviour can be a source of subtle bugs. You always need to be sure if
the lists you are dealing with are the same or different.

Mutability adds a level of flexibility (and complexity!) to lists that we
don't have with strings. Certain operations on lists are now very fast, e.g.
changing a value at a particular index. You can also add/remove values using
methods and functions.


## List Concatenation

If `a` and `b` are lists, then `a + b` is a new list consisting of all the
elements in `a` followed by all the elements in `b`:

```
>>> a = [1, 2]
>>> b = [5, 6, 7, 8]
>>> a + b
[1, 2, 5, 6, 7, 8]
>>> b + a
[5, 6, 7, 8, 1, 2]
```

You can concatenate a list with itself using `+`:

```
>>> a = [1, 2]
>>> a + a
[1, 2, 1, 2]
>>> a + a + a
[1, 2, 1, 2, 1, 2]
```

Or you can use this shorthand with `*`:

```
>>> a = [1,2]
>>> 2 * a
[1, 2, 1, 2]
>>> 3 * a
[1, 2, 1, 2, 1, 2]
```

## List Methods

You can get a list of all the methods that come with lists by typing
`dir([])`:

```
>>> dir([]) 
['__add__', '__class__', '__contains__', '__delattr__',
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy',
'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

Methods that begin with `__` are special, and we will ignore them for now.
Here are the main string methods:

```
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
'remove', 'reverse', 'sort']
```

Let's look at examples of each of these:

```
>>> lst = [1, 2, 3]       # lst.append(x) adds x onto the right end of lst
>>> lst.append('cat')
>>> lst                    
[1, 2, 3, 'cat']
>>> lst.append([4, 5])
>>> lst
[1, 2, 3, 'cat', [4, 5]]


>>> lst = [1, 2, 3]       # lst.clear() removes all values from lst
>>> lst.clear()
>>> lst
[]


>>> lst = [1, 2, 3]       # lst.copy() makes a new copy of lst
>>> lst2 = lst.copy()
>>> lst2
[1, 2, 3]
>>> lst2[0] = -1
>>> lst2
[-1, 2, 3]
>>> lst
[1, 2, 3]


>>> lst = [5, 1, [1, 2], 2, 1, 9, 0, 1]  # lst.count(x) returns the number
>>> lst.count(1)                         # of times x appears in lst
3
>>> lst.count(2)
1
>>> lst.count('shoe')
0


>>> lst = [1, 2, 3]     # lst.extend(other_lst) appends all the values in
>>> lst.extend([4, 5])  # other_lst to the right end of lst
>>> lst
[1, 2, 3, 4, 5]


>>> lst = [4, 7, 5, 4]  # lst.index(x) returns the first index i such that
>>> lst.index(4)        # lst[i] == x; causes an error if x is not in lst
0
>>> lst.index(5)
2
>>> lst.index(6)
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: 6 is not in list


>>> lst = [4, 8, 9]     # lst.insert(i, x) modifies lst by inserting value x
>>> lst.insert(0, 'A')  # before lst[i]
['A', 4, 8, 9]
>>> lst.insert(0, 'B')
>>> lst
['B', 'A', 4, 8, 9]
>>> lst.insert(3, 'C')
>>> lst
['B', 'A', 4, 'C', 3, 9]


>>> lst = [1, 2, 3]    # lst.pop() returns and removes the last item of lst
>>> lst.pop()
3
>>> lst
[1, 2]
>>> lst.pop()
2
>>> lst
[1]
>>> lst.pop()
1
>>> lst
[]
>>> lst.pop()
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: pop from empty list


>>> lst = [1, 2, 3]   # lst.pop(i) modifies lst by removing the item at index i
>>> lst.pop(1)
2
>>> lst
[1, 3]
>>> lst.pop(1)
3
>>> lst
[1]
>>> lst.pop(1)
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: pop index out of range


>>> lst = [5, 1, [1, 2], 2, 1, 9, 0, 1]  # lst.remove(x) removes the first
>>> lst.remove(1)                        # occurrence of x in lst; causes an error
>>> lst                                  # if x is not in lst
[5, [1, 2], 2, 1, 9, 0, 1]
>>> lst.remove(1)
>>> lst
[5, [1, 2], 2, 9, 0, 1]
>>> lst.remove(1)
>>> lst
[5, [1, 2], 2, 9, 0]
>>> lst.remove(1)
Traceback (most recent call last):
  File "__main__", line 1, in <module>
ValueError: list.remove(x): x not in list


>>> lst = [1, 2, 3]     # lst.reverse() modifies lst by re-arranging all its values
>>> lst.reverse()       # into reverse order
>>> lst
[3, 2, 1]
>>> lst.reverse()
>>> lst
[1, 2, 3]

>>> lst = [5, 1, 2, 1, 9, 0, 1]  # lst.sort() modifies lst by re-arranging its values
>>> lst.sort()                   # to be in ascending sorted order (according to the
>>> lst                          # <= operator)
[0, 1, 1, 1, 2, 5, 9]
```

## Looping with Lists

You can loop through the individual elements of a list with a for-loop. For
example:

```
lst = [1, 2, 3]
for x in lst:
    print(10 * x)
```

This prints:

```
10
20
30
```

You can also use while-loops:

```
lst = [1, 2, 3]
i = 0
while i < len(lst):
    print(10 * lst[i])
    i += 1
```

### Example: Counting Even Numbers in a List

Here's a function that uses the loop accumulator pattern to count the number
of *even numbers* in a list:

```python
def count_even(num_lst):
    total = 0
    for x in num_lst:
        if x % 2 == 0:
            total += 1
    return total
```

For example:

```
>>> count_even([9, 2, 4, 2, 7])
3
>>> count_even([])
0
```

### Example: Finding the Min Value of a List

The built-in function `min` returns the minimum value of a list:

```
>>> min([1, 2, 3, 0, 4])
0
>>> min(['bird', 'cat', 'owl', 'ant'])
'ant'
```

For a list of strings, `min` returns the alphabetically first item in the
list.

Let's write our own version of `min`. Assuming `lst` is a non-empty list of
numbers, one way to find the minimum element is first assume that `lst[0]` is
the minimum, and then compare that to each following element. Every time a
following element is smaller, we set it to be the new minimum. When we have
compared every element, we're guaranteed to have the minimum of the entire
list:

```python
def min_list(lst):
    """Returns the smallest element in lst.
    """
    min_so_far = lst[0]
    for x in lst:
        if x < min_so_far:
            min_so_far = x
    return min_so_far
```

For example:

```
>>> min_list([1, 2, 3, 0, 4])
4
>>> min_list(['bird', 'cat', 'owl', 'ant'])
'ant'
```

**Exercise** Create the `max_list(lst)` function, which returns the maximum
value in a list.
