# Lecture 28 Notes

Reading and writing files is a common Python task. There are two main kinds of
files: **text files**, that consist plain text and can viewed and edited in an
editor like Mu; and **binary files**, which is every other kind of file, e.g.
image files, video files, specially formatted files for particular applications,
and so on.

While there are many ways to process files, in these notes we only discuss
reading text files line-by-line.


## Determining What Folder You're In

A tricky aspect of using files is that it can sometimes be unclear if you are
using the right folder or directory (they mean the same) thing. You can check
what folder Python will uses with this code:

```
>>> import os
>>> os.getcwd()
'C:\\Users\\james\\Documents\\courses\\cmpt120fall2022'

>>> os.listdir(os.getcwd())
['a1.py', 'a2.py', 'lectures']
```

`os.getcwd()` returns the *current working directory*, i.e. the directory that
Python will read files from by default.

`os.listdir(os.getcwd())` returns a list of all the files and folders in the
current working directory.


## Reading a Text File Line by Line

[joke.txt](joke.txt) is a text file that contains this:

```
Who’s there?
A broken pencil.
A broken pencil who?
Never mind. It’s pointless.
```

This code reads it line-by-line:

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

The print-out is *double-spaced* because each line of `joke.txt` ends with a
`\n` (which causes a new line when printed), and Python's `print` always adds a
`\n` after what it prints. One way to fix this problem is to have `print` *not*
add a final `\n`:

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
that it is useful to write a function to do it:

```python
def chop(s):
    """If s ends with a \n, remove it. Otherwise returns s unchanged.
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

It prints this:

```
Who's there?
A broken pencil.
A broken pencil who?
Never mind. It's pointless.
```

## Reading Lines of Text File into a List

Something that's often useful to do is to read the lines of file as strings in a
list:

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

This prints the file in reverse order by line:

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

You can also do simple (and slow!) text searching. For example, this prints all
the lines that contain the string `'pencil'`:

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

## Challenge: Checking if Any Lines in a File are Too Long

Write a program that takes the name of a text file as input, and prints just the
lines in the file that are *longer* than 100 characters. 

Print the line number at the start of the line so that the user knows where to
look for it in the file.

If the file has no lines over 100 characters, then print a helpful message like
'No lines with more than 100 characters!'.

**Sample solution** See [long_lines.py](long_lines.py).
[test_long_lines.py](test_long_lines.py) is the file it uses for testing.


## Writing to a Text File

Basic writing to a text file is straightforward. For example
([file_writing.py](file_writing.py)):

```python
# open a file for writing
outfile = open('output.txt', 'w')  # 'w' means write

# write some lines
outfile.write('This is a line 1\n')   # \n is needed to end the line
outfile.write('This is a line 2\n')
outfile.write('\n')
outfile.write('The line above is blank\n')

outfile.close()
```

**Careful!** If `output.txt` already exists, this will be overwrite it, i.e.
delete the previous contents. If it doesn't exist, then it will be created.

Here is are the contents of `output.txt` after running the code:

```
This is a line 1
This is a line 2

The line above is blank
```

## Reading a Web Page

Finally, we note that it is easy to read the contents of a web page as string. For example:

```python
import urllib.request

def get_web_page(url):
    """ Retrieve the contents of a web page.
    """
    socket = urllib.request.urlopen(url)
    return socket.read()

page = get_web_page('https://www.sfu.ca/')
print(page)
```

This returns the web page *as a string*, which may be quite unreadable! If you
want to create your own web
[scraper](https://en.wikipedia.org/wiki/Web_scraping) or browser, then this is a
good start.
