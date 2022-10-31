# Lecture 21 Notes

## String Methods

Python strings come with a number of built-in **methods** that do various
useful things. Here are examples of a few of them. It's important to keep in
mind that none of these methods actually change the string they are operating
on (because strings are immutable in Python), and instead they make copies:

```
>>> s = 'IBM is Big Blue'

>>> s.upper()      # convert to upper case
'IBM IS BIG BLUE'
>>> s.lower()      # convert to lower case
'ibm is big blue'

>>> s.count('B')   # How many 'B's are in the string?
3
>>> s.count('b')   # How many 'b's are in the string?
0
>>> s.count(' ')   # How many spaces are in the string?
0

>>> s.replace(' ', '_')  # Replace spaces with underscores.
'IBM_is_Big_Blue'
>>> s.replace(' ', '')   # Replace all spaces with the empty string.
'IBMisBigBlue'           # Same as removing all spaces.

>>> s.startswith('IBM')  # Does the string start with 'IBM'?
True
>>> s.endswith('Blue.')  # Does the string end with 'Blue.'?
False

>>> s.find('is')         # Where does 'is' appear in the string?
4
>>> s.find('as')         # Where does 'as' appear in the string?
-1                       # -1 returned since it's not in the string

>>> s.split()            # Split s into a list of words.
['IBM', 'is', 'Big', 'Blue']

>>> t = '   Done! \n'
>>> t.strip()   # Remove all whitespace characters at beginning and end
'Done!'
>>> t.lstrip()  # Remove all whitespace characters at beginning
'Done! \n'
>>> t.rstrip()  # Remove all whitespace characters at end
'   Done!'
```

You can combine multiple methods together. For example:

```
>>> s = 'IBM is Big Blue'
>>> s.lower()
'ibm is big blue'
>>> s.lower().count('b')   # Convert s to lowercase, and then
3                          # count how many 'b's it has.

>>> t = '   Done! \n'
>>> t.strip()
'Done!'
>>> t.strip().lower()
'done!'
>>> t.strip().lower().startswith('done') # Remove begin/end whitespace,
True                                     # convert to lower case, and
                                         # check if it starts with 'done'
```

**Question** Suppose the `strip()` method didn't exist. How could you
implement it using `lstrip()` and `rstrip()`?


## Example: Our Own String Equality Checking Function

It's easy to check if two strings are the same using `==` and `!=`:

```
>>> 'Star' == 'Star'
True
>>> 'star' == 'Star'
False

>>> 'Star' != 'Star'
False
>>> 'star' != 'Star'
True
```

It's instructive to write our own version of these operators.

Let's write a function `string_equal(s, t)` that returns `True` if strings `s`
and `t` are the same length, and have the same characters in the same order.
Otherwise, it returns `False`. It should return the same results as `==`.


```python
def strings_equal(s, t):
    """Returns True if strings s and t are the same, False otherwise.
    """
    # string with different lengths can't be equal
    if len(s) != len(t): return False
    
    # len(s) == len(t) at this point
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    
    return True
```

For example:

```
>>> strings_equal('Star', 'Star')
True
>>> strings_equal('star', 'Star')
False
```

`strings_equal` works as follows:

- First it checks if the strings are the same length. If they're *not*, then
  we know the strings can't be the same, and return `False` immediately.

- Second, if the strings are the same length, a loop goes through the
  characters one by one, comparing each pair of characters at the same
  location to see if they are the same. If they're different, we return
  `False` immediately.

- Finally, if we get through the for-loop without returning `False`, then that
  means all the characters in `s` and `t` are the same, and so we return
  `True`.

Notice that the amount of work the function does depends in part on where the
first difference of characters appears. For example, `string_equal('x123456',
'y123456')` returns `False` immediately after checking the first characters.
But `string_equal('123456x', '123456y')` takes a little longer because the
first six characters of each string are checked before getting to the
different characters, `'x'` and `'y'`, at the end. If you are comparing a lot
of very large strings, this speed difference might be noticeable.

With `strings_equal` written, it is easy to implement `strings_not_equal`:

```python
def strings_not_equal(s, t):
    """Returns True if strings s and t are different, False otherwise.
    """
    return not strings_equal(s, t)
```

For example:

```
>>> strings_not_equal('Star', 'Star')
False
>>> strings_not_equal('star', 'Star')
True
```

`strings_not_equal` always returns the opposite value of `strings_equal`, so
we can implement it in a single line.


## Example: Checking if All Characters are the Same

Let's write a function called `all_chars_same(s)` that returns `True` if all
the characters in `s` are the same, and `False` otherwise:

```
>>> all_chars_same('')
True
>>> all_chars_same('a')
True
>>> all_chars_same('aa')
True
>>> all_chars_same('aaaaaaa')
True
>>> all_chars_same('ab')
False
>>> all_chars_same('aaaaa!')
False
```

Here's one way to implement it:

```python
def all_chars_same(s):
    """Returns True if all the characters are the same, and False otherwise.
    Returns True for the empty string.
    """
    if len(s) <= 1: return True
    
    # s has at least 2 characters at this point
    first_char = s[0]
    for c in s:
        if c != first_char:
            return False
    return True
```

First it checks if `s` has length 0 or 1. In either case, that means all the
characters in the string are the same, and `True` can be returned immediately.

If the string is length 2 or greater, then the first character is saved in
`first_char`, and we use a for-loop to go through every character in `s` and
check if it's equal to `first_char`. If not, we can return `False`
immediately. If we get through the entire loop, then all the characters must
be the same, and `True` is returned.


## Example: Checking if All Characters are Equal

Now consider the problem of testing all the characters in a string are
different, i.e. no 2 characters are equal. Unfortunately, this simple function
*doesn't* work:

```python
def incorrect_all_chars_different(s):
	"""Returns True if all characters are different, False otherwise.
	Returns True for the empty string.
	"""
	return not all_same(s)
```

The problem here is that all the characters not being the same doesn't mean
they are all different. For example, the characters in the string `'baaa!` are
not all the same, but they are also not all different (`'a'` is repeated).

So we need another approach. One idea is, for strings with 2 or more
characters, to go through the characters one at a time and then use `not in`
to make sure it doesn't appear in any of the characters after it:


```python
def all_chars_different(s):
    """Returns True if all characters are different, False otherwise.
    Returns True for the empty string.
    """
    n = len(s)
    if n <= 1: return True
    
    for i in range(n-1):    # -1 is important!
        if s[i] in s[i+1:]:
            return False
    return True
```

For example:

```
>>> all_chars_different('')
True
>>> all_chars_different('a')
True
>>> all_chars_different('abc')
True
>>> all_chars_different('abba')
False
>>> all_chars_different('mmm')
False
```

`s[i]` is the character at location `i` in the string, and `s[i+1:]` is a
slice starting at the first character *after* `s[i]` and continuing to the end
of the string. In other wise, `s[i+1:]` is all the characters after `s[i]`.

The range of the loop is only up to `n-1`. If we used `n` instead then, when
`i` is `n-1`, we would get a run-time when evaluating `s[i+1:]` because it
would be the same as `s[(n-1)+1:]`, or `s[n:]`, which is an invalid slice.
