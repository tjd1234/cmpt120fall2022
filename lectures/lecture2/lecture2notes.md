# Lecture 2 Notes

## Euclid's Greatest Common Divisor (GCD) Algorithm

- What's the GCD of 15 and 39?
- What's the GCD of 7 and 5?

What is the algorithm?

1. start with two integers
2. if they are the same, stop: you've found their GCD
3. if they are different, replace the bigger number with the difference
   between it and the smaller number
4. go to step 2


An **algorithm** is precise description of a step-by-step process that solves
a problem.

An algorithm written in English like above is called **pseudocode**. 

What are some questions computer scientists might ask about an algorithm?

- how much memory does it use?
- how many steps does it do to find the GCD (running time)?
- how complicated is it? what sort of basic operations does it assume are
  possible?
- does it always find the correct GCD?
- what happens if you give it non-integer input, or integers that are
  negative?
- can it be sped up?

An algorithm written in a language like Python is called a **program**.

How can we implement this algorithm as a Python program? See
[euclid.py](euclid.py).

Try these numbers in [euclid.py](euclid.py):

- 10 and 9 
- 100 and 99
- 7 and -5
- -7 and -5
- 3.14 and 2.77

## Errors

If you mis-type any characters in your program, or give it the wrong input,
your program could crash (i.e. suddenly stop working) or behave strangely.

Know these three categories of errors:

- **syntax error**: a mistake in the spelling or grammar of your program
  (Python catches some syntax errors *before* a program runs, but not all)

- **runtime error**: an error that occurs while your program is running; if
  you type the string `'five'` into [euclid.py](euclid.py) the program will
  crash with a runtime error

- **semantic error**: an error in the logic of your progam, e.g. you have an
  incorrect algorithm; semantic errors may, or may not, syntax or runtime
  errors


## Practice exercises

- If you haven't already done so, copy [euclid.py](euclid.py) to your own
  computer and try running it in Mu/IDLE.

- Modify [euclid.py](euclid.py) examples of syntax and runtime errors.
