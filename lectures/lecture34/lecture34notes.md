## Review

All the course topics are listed on the [index page for this
site](https://tjd1234.github.io/cmpt120fall2022/).

How should you study computer science and programming? Here is a suggestion:

- make a list of [all the topics](https://tjd1234.github.io/cmpt120fall2022/)
- for each topic, write one or two key examples of code that explain it
- also, write down the definition of each technical term ([the textbook includes a glossary of many technical terms at the end of each chapter](https://runestone.academy/ns/books/published/120fall2022surrey/index.html))
- [do the practice questions listed at the top of the topics page](https://tjd1234.github.io/cmpt120fall2022/)


## Practice Question

Suppose the file `sample_imports.txt` contains a list of Python `import`
statements like this:

```python
import time
import random
import turtle
import doctest
import turtle
import time
```

For simplicity, assume that every line is an `import` statement formatted as in
the example. There are no blank lines or extra spaces around the words.

Write a program that reads `sample_imports.txt` and prints the imports in
*sorted order*, and with any *duplicates removed*. For example, the above file
gets printed like this:

```python
import doctest
import random
import time
import turtle
```

Of course, `sample_imports.txt` should work with any file of imports, not just
the one in the example.

## Sample Solutions

```python
def solution1():
    """Sample solution using a list to keep track of the modules.
    """
    module_list = []
    file = open('sample_imports.py')
    for line in file:
        line = line.strip()
        tokens = line.split(' ')
        mod = tokens[1]
        if mod not in module_list:
            module_list.append(mod)

    module_list.sort()
    for mod in module_list:
        print(f'import {mod}')

def solution2():
    """Sample solution using a dictionary to keep track of the modules.
    """
    module_dict = {}
    file = open('sample_imports.py')
    for line in file:
        line = line.strip()
        tokens = line.split(' ')
        mod = tokens[1]
        module_dict[mod] = 1

    all_modules = list(module_dict.keys())
    all_modules.sort()
    for mod in all_modules:
        print(f'import {mod}')
```

