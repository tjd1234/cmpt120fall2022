# Lecture 28 Notes


## Reading a Text File Character by Character

... coming soon ...


## Reading a Text File Line by Line

[joke.txt](joke.txt) is a text file that contains this:

```
Who’s there?
A broken pencil.
A broken pencil who?
Never mind. It’s pointless.
```

We can read this file line-by-line using this code:

```python
textfile = open('joke.txt')     # assumes joke.txt is in the same folder
for line in textfile:           # as the file this program is in
    print(line)
```

It prints this:

```
Who's there?

A broken pencil.

A broken pencil who?

Never mind. It's pointless.

```

The print-out is double-spaced because each line of `joke.txt` ends with a
`\n` (which causes a new line when printed), and Python's `print` always adds
an `\n` after what it prints. One way to fix this problem is to have `print`
*not* add a final `\n`:

```python
textfile = open('joke.txt')
for line in textfile:
    print(line, end='')     # don't put a \n after line
```

Or you could check which lines end with a `\n` and not print it:

```python
textfile = open('joke.txt')
for line in textfile:
    if line[-1] == '\n':
        print(line[:-1])    # don't print the last character of line
    else:
        print(line)
```

Removing a single `\n` from the end of a string is a common enough operation
that it is useful to write a function that does it for us:

```python
def chop(s):
    """If s ends with a \n, remove it. Otherwise return s unchanged.
    """
    if s == '': 
        return ''
    elif s[-1] == '\n': 
        return s[:-1]
    else:
        return s
```

Now the previous program can be written more simply:

```python
textfile = open('joke.txt')
for line in textfile:
    print(chop(line))
```

These three programs print this:

```
Who's there?
A broken pencil.
A broken pencil who?
Never mind. It's pointless.
```

Something that's often useful to do is to read the lines of file as strings in
a list:

```python
textfile = open('joke.txt')
all_lines = []
for line in textfile:
    all_lines.append(chop(line))  # chop removes a \n at the end line,
                                  # if there is one
print(all_lines)
print()
print(f'number of lines: {len(all_lines)}')
```

This prints:

```
["Who's there?", 'A broken pencil.', 'A broken pencil who?', "Never
mind. It's pointless."]

number of lines: 4
```

This useful enough to put into its own function:

```python
def get_line_list(fname):
    textfile = open(fname)
    all_lines = []
    for line in textfile:
        all_lines.append(chop(line))
    return all_lines
```

Now we can write code like this:

```python
all_lines = get_line_list('joke.txt')
print(all_lines)
print()
print(f'number of lines: {len(all_lines)}')
```

Which prints:

```
["Who's there?", 'A broken pencil.', 'A broken pencil who?', 
"Never mind. It's pointless."]

number of lines: 4
```

Having all the lines in a list makes some operations easy. For example, this
prints the original file:

```python
all_lines = get_line_list('joke.txt')
for line in all_lines:
    print(line)
```

Output:

```
Who's there?
A broken pencil.
A broken pencil who?
Never mind. It's pointless.
```

This prints the file in in reverse order by line:

```python
all_lines = get_line_list('joke.txt')
all_lines.reverse()
for line in all_lines:
    print(line)
```

Output:

```
Never mind. It's pointless.
A broken pencil who?
A broken pencil.
Who's there?
```

This prints the file with line numbers:

```python
all_lines = get_line_list('joke.txt')
line_num = 1
for line in all_lines:
    print(f'{line_num:3} {line}')
    line_num += 1
```

Output:

```
  1 Who's there?
  2 A broken pencil.
  3 A broken pencil who?
  4 Never mind. It's pointless.
```

You can also do simple (and slow!) text searching. For example, this prints
all the lines that contain the string `'pencil'`:

```python
all_lines = get_line_list('joke.txt')
for line in all_lines:
    if 'pencil' in line:
        print(line)
```

Output:

```
A broken pencil.
A broken pencil who?
```

## Writing to a Text File

... coming soon ...
