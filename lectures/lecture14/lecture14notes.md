# Lecture 14 Notes

### For-loops

A Python for-loop can repeat a block of code some of number of times. For
example:

```python
n = input('How many "hello"s do you want? ')
n = int(n)

for i in range(n):
    print(f'{i+1}. hello')
```

For example:

```
How many "hello"s do you want? 4
1. hello
2. hello
3. hello
4. hello
```

It can also be used to go through the items on a list:

```python
colors = ['red', 'green', 'yellow', 'orange']

for c in colors:
    print(f'{c} is a nice color')
```

For example: 

```
red is a nice color
green is a nice color
yellow is a nice color
orange is a nice color
```

You can also use for-loops in a way that combines the above two styles:

```python
colors = ['red', 'green', 'yellow', 'orange']

i = 0
for c in colors:
    print(f'{i+1}. {c} is a nice color')
    i += 1
```

For example:

```python
1. red is a nice color
2. green is a nice color
3. yellow is a nice color
4. orange is a nice color
```

**Optional aside** This last style of for-loop is so common that Python
provides special syntax to handle it:

```python
> colors = ['red', 'green', 'yellow', 'orange']

for i, c in enumerate(colors):
    print(f'{i+1}. {c} is a nice color')
```

The output is the same as the previous example:

```python
1. red is a nice color
2. green is a nice color
3. yellow is a nice color
4. orange is a nice color
```

### while Loops

A Python while-loop repeats a block of code until some condition is `False`.
For example, this prints the numbers from 1 to 5:

```python
i = 0
while i < 5:    # while-loop header
    print(i+1)  # while-loop body is indented under the header
    i += 1

print('Go!')
```

This prints:

```
1
2
3
4
5
Go!
```

In the program code, `i < 5` is called the **while-loop condition**, or
**condition** for short. A while-loop condition should always be a boolean
expression (i.e. and expression that returns `True` or `False`).

In general, the way a while-loop runs is as follows:

- If the condition is `True`, the statements in the while-loop body are all
  executed, one after the other.
- Next, the while-loop condition is evaluated again. If it's `True`, the loop
  body is run again. If it's `False`, Python immediately jumps to the first
  statement *after* the while loop.

Whenever a while-loop body is executed, the condition is evaluated to see if
the body should be executed again.

**Example.** Here's a variation of the above while-loop:

```python
i = 1          # i is initialized to 1 (not 0)
while i <= 5:  # <= is used, not <
    print(i)   # just i, not i + 1
    i += 1

print('Go!')
```

It prints the same thing as the previous while-loop:

```
1
2
3
4
5
Go!
```

In the program, time `i` is initialized to 1 instead of 0, and the condition
uses `<=` instead of `<`.


**Example.** This while-loop counts *down* from 5 to 1:

```python
i = 5
while i > 0:
    print(i)
    i -= 1     # -= means "subtract from", i.e. subtract 1 from i

print('Blast off!')
```

This prints:

```
5
4
3
2
1
Blast off!
```

**Example.** This while-loop sums the numbers from 1 to 100:

```python
total = 0
i = 1
while i <= 100:
    total += i
    i += 1

print(total)
```

**Example.** This while-loop prints just the multiples of 5 from 1 to 100:

```python
i = 5            # i is initialized to 5
while i <= 100:
    print(i)
    i += 5       # i is incremented by 5
```

This prints:

```
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
```


### A Basic while-loop Pattern

Many (not not all!) while-loops follow this basic pattern:

```
initialization_statement   # before the while-loop header

while <some-condition>:
    statement_1
    statement_2
    statement_3
    # ...

    increment_statement    # last statement of the body
```

Typically, before a while-loop header, one or more **loop-control variables**
are initialized. For instance, a common initialization statement is `i = 0`.

The loop condition typically checks the value of the loop control variables.

The last statement of a while-loop body is often an increment statement that
increments (or decrements, if the loop is counting down) the variable from the
initialization statement.

In general, this a good pattern to try to follow whenever you are writing a
while-loop.


### Infinite Loops

You can use a while-loop to make an **infinite-loop**, i.e. a loop that never
ends. For example, this prints "hello!" forever:

```python
while True:          # infinite loop
    print('hello!')
```

This loop prints numbers forever:

```python
i = 1
while True:   # infinite loop
    print(i)
    i += 1
```

Infinite loops are often a sign of a bug in your program. For instance, it is
easy to forget the increment statement in a while-loop body, resulting in an
infinite loop:

```python
i = 0
while i < 5:
    print(i+1)
               # oops: forgot i += 1, infinite loop!

print('Go!')   # never printed
```
