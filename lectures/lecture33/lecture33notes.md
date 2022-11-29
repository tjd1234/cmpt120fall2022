For now, please see [lecture 31](../lecture31/lecture31notes.md) and
[lecture32](../lecture32/lecture32notes.md).

In these notes, we are doing an experiment to test what is the most efficient
way to do linear in Python. [search_test.py](search_test.py) contains all the
functions and test code.

## Multiple Implementations

6 different implementations of a "contains" function that tests if some value
`x` is in a list. There are two important exceptions to be aware of:

  - `contains_recursive_linear` is a simple recursive implementation of linear
    search that only works if the list being searched has less than about 1000
    items. If the list has too many items, then Python automatically stops for
    too many recursive function calls.

  - `contains_recursive_binary` is a recursive implementation of *binary*
    search, so it requires that the list items be in ascending sorted order.

## Correctness Testing

In [search_test.py](search_test.py), the function `test_contains(contains)`
checks that the passed-in `contains` function works correctly by checking that
few cases return the correct answer:

```python
def test_contains(contains):
    print(f'calling test_contains({contains.__name__}) ... ', end='')
    assert contains(3, []) == False
    assert contains(3, [3]) == True
    assert contains(1, [3]) == False
    assert contains(4, [3]) == False
    assert contains(3, [1, 3, 5]) == True
    assert contains(1, [1, 3, 5]) == True
    assert contains(5, [1, 3, 5]) == True
    assert contains(0, [1, 3, 5]) == False
    assert contains(2, [1, 3, 5]) == False
    assert contains(-1, [-1, 3, 51, 100]) == True
    assert contains(100, [-1, 3, 51, 100]) == True
    assert contains(2, [-1, 3, 51, 100]) == False
    assert contains(200, [-1, 3, 51, 100]) == False
    print('passed')
```

Note a couple of things:

- `test_contains` does **unit testing**, i.e. it tests a single function at a
  time, *contains*. Many of the test test cases are "edge" cases, i.e. they test
  values near the start/end of the list. Bugs often hide in such places.

- It's possible that the function could return "passed" for a contains function
  that has a bug in it. That's because no reasonable *finite* amount of testing
  can be taken as proof that a function like this works correctly. It's always
  possible that it fails for a case we didn't think of.

- In Python, if `f` is a function then `f.__name__` is the name of the function
  when it was defined. This is a neat trick that makes it easy to print which
  function is being tested.


## Performance Testing

When we have multiple implementations of a function that we know are correct,
then we may still want to know which one is fastest. So
[search_test.py](search_test.py) contains this function:

```python
def test_performance():
    contains_functions = [contains_builtin, 
                          contains_for_each, 
                          contains_for_range, 
                          contains_while, 
                          #contains_recursive_linear,  
                          contains_recursive_binary]

    lst = list(range(1000000))
    print()
    for contains in contains_functions:
        print(f'testing:  {contains.__name__:25}  ', end='')
        start = time.time()
        for i in range(10):
            contains(-1, lst)
        elapsed_time = time.time() - start
        print(f'{elapsed_time:.2f} seconds')
```

Some things to note:

- The functions being tested are stored in a list. In Python, functions are
  values, and so you can store them in a list. This makes it easy in the
  following code to loop through the list and test each function individually.

- The function `contains_recursive_linear` is commented out because it can't 

- We always search for the value -1, which is guaranteed to *not* be on the
  list. This forces the functions to do the maximum amount of work.

- The function `time.time()` returns the current time in seconds. So calling it
  before and after running the tests lets us calculate the total elapsed time.

