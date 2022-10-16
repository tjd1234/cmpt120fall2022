## Lecture 19 Notes

### String Basics

In Python, a string is a sequence of 0 or more characters. The type of a
string in Python is `str`:

```python
>>> type('cat')
<class 'str'>
```

A **string literal** is represented using single-quotes, double-quotes, or
triple quotes. Here are 4 examples of string literals:

```python
'you can put a " in single-quote strings'

"you can put a ' in double-quotes strings"

"""Triple-quotes strings can span
multiple lines. They are often use a doc strings
for functions.
"""

'''This is also a triple-quoted string,
using single-quotes instead of double-quotes.
'''
```

As mentioned in the examples, you *cannot* split a regular single-quoted or
double-quoted string across multiple lines.

The **empty string** is a string with 0 characters, i.e. of length 0. These
all represent the empty string:

```
''

""

""""""

''''''
```

We will often need to treat the empty string as a special case when processing
strings.

The *order* of the characters in a string matters. For example, `'abc'` and
`'bac` are *different* strings.

The *case* of a letter in a string *matters*. For example, `'M'` and `'m'` are
*different* string, and `'Cat'` and `'cat'` are also different.

**Note** Some programming languages have a special data type for single
characters. For example, in C++ the `char` data type represents single
characters. However, Python does *not* have a special character data type.
Single-character strings like `'h'` or `'!'` are regular strings of length 1.

The **length** of a string is the number of characters it contains, and in
Python the built-in `len` function returns the length of a string:

```python
>>> len('')
0
>>> len('log')
3
>>> len('a b c')
5
```


### Special Characters

In a string literal, any '`\`' indicates that the next character is special in
some way. For example, `'\n` is an escape character called **newline** that
represents a command to send the cursor to the next line. For example:

```python
>>> print('one\ntwo')
one
two
```

The string `'one\ntwo'` has length 7 (not 8!). Even though `'\n'` consists of
two symbols, `\` and `n`, it counts as single character. Similarly, the string
`'\n\n\n'` has length 3:

```python
>>> len('\n\n\n')
3
```

Here are the most common escape characters that you will see in Python
strings:

|    |   **name**   |                                     **common use**                                    | **example**                            |
|:--:|:------------:|:-------------------------------------------------------------------------------------:|----------------------------------------|
| \n |    newline   | blank line                                                                            | >>> print('a\nb')<br>a<br>b            |
| \t |      tab     | fixed-width space, for formatting;<br>width of a tab is **not** defined by <br>Python | >>> print('\thello!')<br>    hello!    |
| \\\ |   backslash  | \ as a literal character                                                              | >>> print('root\\\\users')<br>root\users |
| \\' | single quote | ' as a literal character                                                           | >>> print('\\'-quote')<br>'-quote       |
| \\" | double quote | " as a literal character                                                           | >>> print("\\"-quote")<br>"-quote       |


**Example 1** Can you make a string, that when printed, displays this?

```
special characters: ' " \
```

Here's one way to do it:

```
print('special characters: \' " \\')
```

**Example 2** Can you make a string, that when printed, displays three backslashes?

```
\\\
```

Each printed `\` needs double-`\` in the string:

```python
print('\\\\\\')  # 6 backslashes
```

Note that 5 backslashes *doesn't* work:

```
>>> print('\\\\\')        # oops: 5 backslashes
  File "<stdin>", line 1
    print('\\\\\')
                 ^
SyntaxError: EOL while scanning string literal
```

The problem here is that Python reads the string as these three characters:
`\\`, `\\`, and `\\'`. This means there is no `'`-quote to end the string, and
so the error.


### Whitespace

A **whitespace character** is a character that doesn't have a visual
representation (and so, when "printed" on a piece of white paper will look
like a white space). While there are many such characters in Python, the three
most common whitespace characters are:

- `' '`, a regular space
- `\n`, a newline
- `\t`, a tab

When programmers refers to "whitespace", they mean characters like this.
Sometimes whitespace matters, sometimes it doesn't. For instance, we can say
that the indentation in a Python program is "significant whitespace". When we
read strings from the user, we often remove whitespace characters at the
beginning and the end, e.g. the string `'  done\n'` becomes `'done'`.

### Strings are Immutable

In Python, **mutable** means "changeable", and **immutable** "not changeable".
Python strings are immutable, i.e. there is way to modify them or change their
length. While it might sometimes seem like you are changing a Python string,
you can never change them, you can only make a copy.


### String Concatenation

**Concatenating** two strings means to combine them together to make a new
string. This is easily done in Python with the `+` operator:

```
>>> 'cat' + 'nap'
'catnap'
>>> 'Elon' + ' ' + 'Musk'
'Elon Musk'
>>> 'ha' + 'ha' + 'ha'
'hahaha'
```

The last example with `'ha'` is an example of concatenating a string with
itself. In Python you can also do that with the `'*'` operator:

```
>>> 3 * 'ha'
'hahaha'
>>> 'Boat' * 5
'BoatBoatBoatBoatBoat'
```

### String Comparisons

If `s` and `t` are variables that refer to strings, then:

- `s == t` evaluates to `True` if `s` and `t` are the same length, and have
  exactly the same characters in the same order. Otherwise, it evaluates to
  `False`.

- `s != t` evaluates to `True` if `s` and `t` are different, and to `False` if
  `s == t`.

- `s < t` evaluates to `True` if `s` comes alphabetically before `t`, and
  `False` otherwise. `s > t` evaluates to the same value as `t < s`.

- `s <= t` evaluates to `True` if either `s < t` or `s == t`, and `False`
  otherwise. `s >= t` evaluates to the same value as `t <= s`.

For example:

```
>>> s = 'cat'
>>> t = 'dog'

>>> s == t
False
>>> s == s
True
>>> ('c' + 'at' ) == s
True
>>> s != t
True

>>> s < t
True
>>> s <= t
True

>>> s > t
False
>>> s >= t
False
```

### String Indexing

Consider the string `'s'`:

```python
s = 'apple'
```

We can access individual characters in `s` using **string indexing**:

```python
>>> s[0]
'a'
>>> s[1]
'p'
>>> s[2]
'p'
>>> s[3]
'l'
>>> s[4]
'e'
>>> s[5]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: string index out of range
```

In Python, string indexing *always* starts at 0, meaning the first character
of a string is at location 0. This is known as **0-based indexing**. The index
of the last character is always *one less* than the length of the string
(because the indices start at 0). If you try to access an index location past
the last one, then you get an "index out of range" run-time error as shown in
the last example above.

Diagrams are helpful for understanding indexing:

```
       0     1     2     3     4
    +-----+-----+-----+-----+-----+
 s  | 'a' | 'p' | 'p' | 'l' | 'e' |
    +-----+-----+-----+-----+-----+
     s[0]  s[1]  s[2]  s[3]  s[4] 
```

In general, if `s` is any *non-empty* string, then `s[0]` is its first
character, and `s[len(s)-1]` is its last character. Evaluating `s[len(s)]`
causes an "index out of range" run-time error.

If `s` is the empty string, then *all* of `s[0]`, `s[len(s)-1]`, and
`s[len(s)]` cause index out of range errors. For the empty string, `s[i]` is
an out of range error for any index `i`.

Since Python strings are immutable (i.e. not changeable), it is an error to
assign a new character to a string:

```
>>> s = 'apple'
>>> s[0] = 'A'
Traceback (most recent call last):
  File "__main__", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

If you want the string `'Apple`, then you must use some combination of string
slice or string methods (discussed later) to create a new string.

You can access every character in a string with this style of for-loop:

```python
s = 'apple'
for i in range(len(s)):
	print(s[i])
```

Or the same thing using a while-loop:

```python
s = 'apple'
i = 0
while i < len(s):  # < is important; <= would be wrong
	print(s[i])
	i += 1         # += adds a value to a variable
```

More simple, you can directly loop over the characters of a string like this:

```python
s = 'apple'
for c in s:
	print(c)
```

In general, this kind of loop is often preferable to the other two because it
is short and clear, and you don't need to worry about the index variable.


### Negative Indices

If `s` is a non-empty string, then `s[len(s)-1]` is it's last character. The
index `len(s)-1` is bit a long, and it's easy to mis=type. So Python lets you
write `s[-1]` instead. For any non-empty string `s`, `s[-1]` is its last
character, `s[-2]` is its second to last character, `s[-3]` is its third to
last character and so on.

So every character of a string has both negative indices as well as
non-negative indices:

```
      -5    -4    -3    -2    -1
       0     1     2     3     4
    +-----+-----+-----+-----+-----+
 s  | 'a' | 'p' | 'p' | 'l' | 'e' |
    +-----+-----+-----+-----+-----+
     s[0]  s[1]  s[2]  s[3]  s[4]
     s[-5] s[-4] s[-3] s[-2] s[-1] 
```

For example:

```
>>> s = 'apple'
>>> s[-1]
'e'
>>> s[-2]
'l'
>>> s[-3]
'p'
>>> s[-4]
'p'
>>> s[-5]
'a'
>>> s[-6]
Traceback (most recent call last):
  File "__main__", line 1, in <module>
IndexError: string index out of range
```

In practice, negative indexing is often used to access characters near the
right end of the string. It's not usually used for characters near the
beginning.

**Question** If `s` is a non-empty string, is `s[-len(s)]` the *first*
character of `s`?

#### Example: Pluralizing a String

Here's a simple rule for pluralizing English words:

- If the word doesn't end with an *s*, then add an *s* to the end of it. For
  example, *toy* becomes *toys*.
- If the word ends with an *s*, then do nothing (we assume it's already
  pluralized). For example, *birds* becomes *birds*.

While this pluralization rule is simple, it doesn't always give the right
answer. For example, the rule says the plural of *try* is *trys*. But the
correct plural is *tries*. We'll ignore such problems and implement the rule
as given:

```python
def pluralize(word):
    """Adds an 's' to the end of the string. 
    If it already ends with an 's', then it is returned
    unchanged.
    """
    if word == '': return s
    if word[-1] == 's':
        return word
    else:
        return word + 's'
```

For example:

```
>>> pluralize('toy')
'toys'
>>> pluralize('toys')
'toys'
```

### String Slicing

**String slicing** is a generalization of string indexing that lets you get an
entire substring within a string, instead of just a single character. For
example:

```
>>> s = 'apple'
>>> s[1:3]
'pp'
```

`s[1:3]` is a **string slice**, and it refers to the sequence of characters in
`s` that *start* at index location 1, and end at index location 3 (not 2!).
Here are a few more examples:

```
>>> s[0:4]
'appl'
>>> s[3:6]
'le'
>>> s[0:1]
'a'
>>> s[1:2]
'p'
>>> s[2:3]
'p'
>>> s[3:4]
'l'
>>> s[4:5]
'e'
```

Notice that in the slice `s[4:5]` the value 5 is *not* a valid index for `s`,
i.e. `s[5]` causes an out of range error. But it is okay to use it as the
second number in a slice. In fact, this second number in a slice can be bigger
than the string length without causing an out of range error:

```
>>> s[4:5]
'e'
>>> s[4:6]
'e'
>>> s[4:7]
'e'
>>> s[4:500]
'e'
```

You can also do slicing with negative indices, but we will not cover that in
these notes. While slicing with negative indices does have it's uses, it often
results in tricky expressions that can be hard to understand.

In general, for a non-empty string `s`, a string slice has the form
`s[begin:end]`. The *first* character of the slice is `s[begin]`, and the
*last* character of the slice is `s[end-1]` (*not* `s[end]`). `begin` should
be a valid (non-negative) index for `s`, and `end` either a valid
(non-negative) index *or* equal to the length of the string. Also, the length
of the slice `s[begin:end]` is `end - begin`. In other words,
`len(s[begin:end]) == (end - begin)`

As with indexing, since strings are immutable (i.e. not changeable), you
*cannot* assign a string to a slice:

```
>>> s = 'apple'
>>> s[1:3] = 'dd'
Traceback (most recent call last):
  File "__main__", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

There are a couple of short expressions for string slicing that you can use:

```
>>> s = 'apple'

>>> s[0:3]
'app'
>>> s[:3]   # same as s[0:3], 0 is optional
'app'

>>> s[3:5]
'le'
>>> s[3:]   # same as s[3:5], 5 is optional
'le'

>>> s[3:] + s[:3]
'leapp'

>>> s[:]    # makes a copy of s
'apple'
```

Slices have an optional third argument called `step` that can skip characters.
For example:

```
>>> s = '012345678'
>>> s[2:8]
'234567'
>>> s[2:8:2]  # every 2nd character starting at 2, and less than 8
'246'
>>> s[2:8:3]  # every 3rd character starting at 2, and less than 8
'25'
>>> s[2:8:4]  # every 4th character starting at 2, and less than 8
'26'
```

Slices with a step are only occasionally useful, and so don't appear often in
most Python programs. Perhaps the most common use of the step parameter is to
reverse a string:

```
>>> s = 'apple'
>>> s[::-1]   # reverses s
'elppa'
>>> 'star loop'[::-1]
'pool rats'
```

`[::-1]` isn't very readable notation, but it is short and can be a convenient
way to reverse a string if you can remember it.

**Trivia** `[::-1]` applied twice gives you the original string:

```
>>> 'start loop'[::-1][::-1]
'start loop'
```


### The in and not in Operators

It's easy to test if a string contains, or doesn't contain, a particular
substring:

```
>>> 'off' in 'post office'
True
>>> 'to' in 'post office'
False

>>> 'm' in 'Computer'
True
>>> 'm' not in 'Computer'
False

>>> 'CPU' in 'Computer'
False
>>> 'CPU' not in 'Computer'
True
```

`in` and `not in` only tell you if a substring is in a string or not. If it is
in the string, they don't say where in the string. For that you need to use a
string method such as `find`, discussed in the next section.


### String Methods

Python strings come with a number of built-in **methods** that do various
useful things. Here are examples of a few of them. It's important to keep in
mind that none of these methods actually change the string they are operating
on (because strings are immutable in Python), and instead they are making
copies:

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


### Example: Our Own String Equality Checking Function

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


## Example: Checking if All Characters are Equal

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

