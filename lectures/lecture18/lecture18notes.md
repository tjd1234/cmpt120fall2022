## Lecture 18 Notes

This lecture is a case study in the problem of converting to and from binary
numbers.

### Base-10 Numbers

The ordinary numbers we use day-to-day are called **decimal numbers**, or
**base-10 numbers**. In base-10, each **digit** is an integer from 0 to 9, and
the right-most digit is multiplied by 1, the digit to the left of that is
multiplied by 10, the digit to the left of that is multiplied by 100, and so
on. Since the position of the digit matters, this is called [positional
notation](https://en.wikipedia.org/wiki/Positional_notation).

For example, the base-10 number 3503 is interpreted like this:

```
	   3     5     0     3  = 3*1000 + 5*100 + 0*10 + 3*1
	1000   100    10     1
	10^3  10^2  10^1  10^0
```

Notice that the 3 at the start represents 3\*1000 = 3000, while the 3 at the
end is 3\*1 = 3.

**Question** What is 17032 when written out as a sum of powers of 10 as in the
above example?

**Answer**: 17032 = 1\*10^4 + 7\*10^3 + 0\*10^2 + 3\*10^1 + 2\*10^0.


### Base-2 Numbers: Binary

**Base-2**, or **binary**, numbers follow the same idea as base-10 numbers,
but with two main differences:

- Binary uses powers of 2 (instead of powers of 10 in base-10)
- Binary digits are called **bits**, and there are only two of them: 0 and 1.

For example, 10110 is a binary number that is 5-bits long. It is interpreted
like this:

```
	   1     0     1     1    0 = 1*16 + 0*8 + 1*4 + 1*2 + 0*1 = 16 + 4 + 2 = 22
	  16     8     4     2    1
	 2^4   2^3   2^2   2^1  2^0
```

This shows that 10110, which is in base-2, is equal to 22 in base-10.

**Fact** A group of 8 bits is called a **byte**.

**Fact** If a binary number ends with 0, then it is even. If it ends with 1,
then it's odd. On some computers this fact is used to efficiently test if a
number if even or odd.

**Fact** The largest value for an $n$-bit binary number is $2^{n}-1$, when all
the bits are 1s. For example, the largest 5-bit binary number is $11111 = 16 +
8 + 4 + 2 + 1 = 31 = 2^{5} - 1$.


### Converting Binary Numbers to Base-10

Let's write a Python function that converts binary numbers to base-10. For
example, `bit_to_dec('10110')` evaluates to 22.

We will assume the input is a string of bits, i.e. 0s and 1s. Leading 0s are
allowed, e.g. `'00011'` is 3 in base-10.

The idea of `bits_to_dec(bits)` is to go through each each bit in `bits`, one
at a time from left to right. The bit is converted to an `int`, multiplied by
the corresponding power of 2, and then added to the accumulator variable
`result`.

```python
def bits_to_dec(bits):
    """Returns the base-10 int value of bits.
    Assumes bits is a string of 0s and 1s.
    """
    pow = len(bits) - 1
    result = 0
    for b in bits:
        result += int(b) * 2**pow
        pow -= 1   # subtract 1 from pow
    return result
```

Notice that `pow` is initialized to *one less* than the length of `bits`. That's
because, if you count from the right, the powers of the place values start at
0 (not 1).


### The Other Direction: Converting Base-10 Numbers to Binary

To convert a base 10 number to binary, first pick the number of bits you want
the binary number to have. For this example, we will use 5 bits. Suppose we
want to convert 20 to binary. First we write down the first 5 powers of 2:

```
 _ _ _ _ _
16 8 4 2 1
```

16 is less than 20, so we write a 1 above the 16:

```
 1 _ _ _ _
16 8 4 2 1
```

Then we subtract 16 from 20, giving us 4. The next power is 8, which is bigger
than 2, so we write a 0 over the 8:

```
 1 0 _ _ _
16 8 4 2 1
```

The next power of 4 is equal to 4, so we put a 1 over the 4:

```
 1 0 1 _ _
16 8 4 2 1
```

We subtract 4 from 4 to get 0. At this point we are done and can write 0s for
he rest of the bits:

```
 1 0 1 0 0
16 8 4 2 1
```

So the binary representation of 20 is 10100.

**Question** Using the same method as the example, calculate the binary
representation of 25.

Here is a Python function that converts base-10 values to binary (see
[binary.py](binary.py)):

```python
def dec_to_bits(n, num_bits):
    """Returns binary representation of base-10 integer n.
    Assumes n is an int and n >= 0, and num_bits is big enough
    to represent n. A string of num_bits bits is returned.
    """
    result = ''
    for i in range(num_bits):
        pow2 = 2 ** (num_bits - i - 1)
        if n > pow2:
            result += '1'
            n -= pow2
        else:
            result += '0'
    return result
```

The idea is to loop through all the powers of 2, from biggest to smallest. If
`n` is greater than, or equal to, the power, then we add a 1 to the
accumulation variable `result` and subtract the power from `n`. Otherwise, if
`n` is less than the power, we just add a 0 to `result`.

For example, this loop prints the binary representation of the base-10 numbers
from 0 to 20:

```python
for i in range(0, 21): 
    print(i, dec_to_bits(i, 5))
```

The output:

```
0 00000
1 00001
2 00010
3 00011
4 00100
5 00101
6 00110
7 00111
8 01000
9 01001
10 01010
11 01011
12 01100
13 01101
14 01110
15 01111
16 10000
17 10001
18 10010
19 10011
20 10100
```

Here's a useful way to test both `bits_to_dec` and `dec_to_bits`. If you
convert a number to binary using `dec_to_bits`, and then convert it back using
`bits_to_dec`, you always get the same number. For example,
`bits_to_dec(dec_to_bits(i, 5))` should always return `i`. If it doesn't,
there's an error in `bits_to_dec` or `dec_to_bits`.

So this loop should print the numbers from 0 to 20:

```python
for i in range(0, 21):
    print(bits_to_dec(dec_to_bits(i, 5)))
```

And indeed it does:

```
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```
